#!/bin/bash

cat << EOF
	
	<!--Start SUB HEAD Content-->			

<div id="googlead" align="center">

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Tools_Top_720x90_Ad -->
<ins class="adsbygoogle"
     style="display:inline-block;width:720px;height:90px"
     data-ad-client="ca-pub-2601749019656699"
     data-ad-slot="3790603779"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>	

</div>
		

	<div id="footer" align="center">
	
		<small><p>$HTTP_USER_AGENT</p>
		<p>Information generated at: `date`</p>
<p> A website created by <a id="af" target="_blank" href="https://github.com/caezsar/"> caezsar.</a> 
&copy; Copyright `date +"%Y"` <a id="af" target="_blank" href="http://tecmint.com"> Tecmint.com </a></p>
            </small></div>



<!--End Container-->

<script src="../plugins/jquery/jquery.min.js"></script>
<script src="../plugins/bootstrap/bootstrap.min.js"></script>
<script src="../js/devoops.js"></script>
</body>
</html>

EOF
