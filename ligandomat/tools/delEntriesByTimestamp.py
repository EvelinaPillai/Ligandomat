import MySQLdb
import sys
from ligandomat import config

#deleted entries by timestamp in case of upload error
def deleteEntriesbyTimestamp(timestamp_name):
	_dbconnection = MySQLdb.connect(host = config.host, user = config.user, passwd = config.passwd, db = config.db, port = config.port)
	_dbconnection.autocommit(False)
	cursor = _dbconnection.cursor()
	
	try:
# SQL query to DELETE entries by timestamp
		cursor.execute("""delete from ms_run where timestamp=%s""",(timestamp_name))
		print ('Affected rows in ms_run: ', cursor.rowcount)
		
		cursor.execute("""delete from source_hlatyping where timestamp=%s""",(timestamp_name))
		print ('Affected rows in source_hlatyping: ', cursor.rowcount)
		
		#maximal one row in source
		cursor.execute("""delete from source where timestamp=%s""",(timestamp_name))
		print ("Affected rows in source: ", cursor.rowcount)
		
		#maximal one row in mhcpraep
		cursor.execute("""delete from mhcpraep where timestamp=%s""",(timestamp_name))
		print ("Affected rows in mhcpraep: ", cursor.rowcount)
		
		cursor.execute("""delete from spectrum_hit where timestamp=%s""",(timestamp_name))
		print ("Affected rows in spectrum_hit: ", cursor.rowcount)
		
		cursor.execute("""delete from intern_data where timestamp=%s""",(timestamp_name))
		print ("Affected rows in intern_data: ", cursor.rowcount)
		
		cursor.execute("""delete from peptide where timestamp=%s""",(timestamp_name))
		print ("Affected rows in peptide: ", cursor.rowcount)
		
		#delete from log_file
		#cursor.execute("""delete from LigandosphereDB_toy.log_file where tmp_name=%s""",(timestamp_name))
		# Commit your changes in the database
		_dbconnection.commit()
				
		print "All entries have been removed successfully"
		
	except MySQLdb.Error, e:
		# Rollback in case there is any error
		_dbconnection.rollback()
		print "An error has been passed. %s" %e
    	
	
		
		
	# close the cursor object
	cursor.close ()
	# close the db
	_dbconnection.close ()
	# exit the program
	sys.exit()

if __name__ == '__main__':

    deleteEntriesbyTimestamp(sys.argv[1])
