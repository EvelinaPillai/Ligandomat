<%inherit file='ligandomat:templates/layout.mako'/>

<form method="post" >


<div id='content'>
<form action="/query" method="post">
  <table >



   <!-- SEARCH FOR A SUBSEQUENCE -->
   <tr>
   <td>Search for a sequence:</td>
   <td><input style="font-size:14px" name="subsequence" type="text" /></td>
   </tr>

   <tr>
   <td>Sort the result by: <select style="font-size:14px" name="sorting_pat">
       <option value="sequence" selected="selected">sequence</option>
       <option value="sourcename">source</option>
       <option value="runname">runname</option>
       </select></td>
   <td><form>
    <p>
    <input type="button" name="wildcard-info" value="Wildcard Info"
  onclick="alert('For each character use _ as wildcard, for many characters use % as wildcard');">
    </p>
    </form>
    <input style="font-size:14px" value="Go!" type="submit" name="search_by_subsequence" /></td>
   </tr>

   <td>&nbsp;</td>

    <!-- SEARCH FOR MS_RUNS -->
   <tr>
   <td>Search for ms_runs:</td>

   <td><input style="font-size:14px" name="runname_subsequence" type="text" /></td>
   </tr>

   <tr>
   <td>Sort the result by: <select style="font-size:14px" name="sorting_runname">
       <option value="sequence" selected="selected">sequence</option>
       <option value="sourcename">source</option>
       <option value="runname">runname</option>
       </select></td>
   <td><form>
    <p>
    <input type="button" name="wildcard-info" value="Wildcard Info"
  onclick="alert('For each character use _ as wildcard, for many characters use % as wildcard');">
    </p>
    </form><input style="font-size:14px" value="Go!" type="submit" name="search_by_runname" /></td>
   </tr>


   <td>&nbsp;</td>

        <!-- SEARCH FOR organ -->
   <tr>
   <td>Search for organ:</td>

   <td><input style="font-size:14px" name="organ_subsequence" type="text" /></td>
   </tr>

   <tr>
   <td>Sort the result by: <select style="font-size:14px" name="sorting_organ">
       <option value="sequence" selected="selected">sequence</option>
       <option value="sourcename">source</option>
       <option value="runname">runname</option>
       </select></td>
   <td><form>
    <p>
    <input type="button" name="wildcard-info" value="Wildcard Info"
  onclick="alert('For each character use _ as wildcard, for many characters use % as wildcard');">
    </p>
    </form><input style="font-size:14px" value="Go!" type="submit" name="search_by_organ" /></td>
   </tr>



   <td>&nbsp;</td>
    <!-- SEARCH FOR tissue -->
   <tr>
   <td>Search for tissue:</td>

   <td><input style="font-size:14px" name="tissue_subsequence" type="text" /></td>
   </tr>

   <tr>
   <td>Sort the result by: <select style="font-size:14px" name="sorting_tissue">
       <option value="sequence" selected="selected">sequence</option>
       <option value="sourcename">source</option>
       <option value="runname">runname</option>
       </select></td>
   <td><form>
    <p>
    <input type="button" name="wildcard-info" value="Wildcard Info"
  onclick="alert('For each character use _ as wildcard, for many characters use % as wildcard');">
    </p>
    </form><input style="font-size:14px" value="Go!" type="submit" name="search_by_tissue" /></td>
   </tr>



   <td>&nbsp;</td>

    <!-- SEARCH FOR ALL PEPTIDES -->
    <tr>
   <td>Get all peptides from the database:</td>
   <td><input style="font-size:14px" value="Go!" type="submit" name="search_all" /></td>
   </tr>

   </table>
</form>
</div>

<%doc>
<table>
	<tr>
		<td> PEPTIDE
		</td>
	</tr>

	<tr>
		<td>
			List of all Peptides : 
		</td>
		<td>
		</td>
		<td>
			<input type='submit' name='button_peptide_all' value='All Peptides'>
		</td>
	</tr>
	<tr>
		<td>
			Get Info about the peptide :
		</td>
		<td>
			${form.peptide_info} 
		</td>
		<td>
			<input type="submit" name="button_peptide_info" value="Get info" />
		</td>
	</tr>
	<tr>
		<td>
			Get all Peptides with Pattern :
		</td>
		<td>
			${form.peptide_pattern} 
		</td>
		<td>
			<input type="submit" name="button_peptide_pattern" value="Get PatternPeptides" />
		</td>
	</tr>
	<tr>
		<td> * * * * *
		</td>
	</tr>
	<tr>
		<td> SOURCE
		</td>
	</tr>
	<tr>
		<td>
			Show details of source : 
		</td>
		<td>
			${form.source_detail}
		</td>
		<td>
			<input type='submit' name='button_source_detail' value='Source details'>
		</td>
	</tr>
	<tr>
		<td>
			Show peptides of source : 
		</td>
		<td>
			${form.source_peptides}
		</td>
		<td>
			<input type='submit' name='button_source_peptides' value='Source peptides'>
		</td>
	</tr>
	
</table>
<br><br><br>

<input type='submit' name='button_get_mining_csv' value='Get mining csv'>



</form>

<style type="text/css">
td {
	height:30px;
}

a {
	text-decoration:none;
}
</style>

</%doc>
