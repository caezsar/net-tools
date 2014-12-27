#!/bin/bash

cat << EOF
	
	<!--Start SUB HEAD Content-->			

		

	<div id="footer" align="center">
	
		<small><p>$HTTP_USER_AGENT</p>
		<p>Information generated at: `date`</p>
<p> A website created by <a id="af" target="_blank" href="https://github.com/caezsar/"> caezsar.</a> 
&copy; Copyright `date +"%Y"` <a id="af" target="_blank" href="http://tecmint.com"> Tecmint.com </a></p>
            </small></div>



<!--End Container-->
<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<!--<script src="http://code.jquery.com/jquery.js"></script>-->
<script src="plugins/jquery/jquery.min.js"></script>
<script src="plugins/jquery/jquery.min.js"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="plugins/bootstrap/bootstrap.min.js"></script>

<!-- All functions for this theme + document.ready processing -->
<script src="js/devoops.js"></script>
</body>
</html>

EOF
