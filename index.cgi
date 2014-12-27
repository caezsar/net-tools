#!/bin/bash

POST=$(</dev/stdin)

./head.cgi

ip_func() {
	result=`/usr/bin/dig +short "$FOLDER4" 2> /dev/null`
         while read -r line; do
        echo "<div align="center">$line</div>"
        done <<< "$result" 	
}



	#### read in our parameters ###
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER1=`echo "$POST" | sed -n 's/^.*folder1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
    FOLDER2=`echo "$POST" | sed -n 's/^.*folder2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER3=`echo "$POST" | sed -n 's/^.*folder3=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	#### test if any parameters were passed ###
	if [ $CMD ]
	then
	  case "$CMD" in

            dig)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> DIG result for <strong> $FOLDER </strong></span>
				</div>
				<div class="box-icons">
					<a class="collapse-link">
						<i class="fa fa-chevron-up"></i>
					</a>
					<a class="expand-link">
						<i class="fa fa-expand"></i>
					</a>
					<a class="close-link">
						<i class="fa fa-times"></i>
					</a>
				</div>
				<div class="no-move"></div>
			</div>
		        <div class="box-content">
                <pre class="prettyprint" id="block">
<strong> <p>`/usr/bin/dig "$FOLDER" 2> /dev/null` </p></strong>
</pre>
</div>
<div align="center"
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
</div></div></div>
EOF

		  ;;
				
            host)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Host result for <strong> $FOLDER1 </strong></span>
				</div>
				<div class="box-icons">
					<a class="collapse-link">
						<i class="fa fa-chevron-up"></i>
					</a>
					<a class="expand-link">
						<i class="fa fa-expand"></i>
					</a>
					<a class="close-link">
						<i class="fa fa-times"></i>
					</a>
				</div>
				<div class="no-move"></div>
			</div>
		        <div class="box-content">
                <pre class="prettyprint" id="block">
<strong> <p>`/usr/bin/host "$FOLDER1" 2> /dev/null` </p></strong>
</pre>
</div>
<div align="center"
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
</div></div></div>
EOF
			  
              ;;
 
			nslookup)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Nslookup result for <strong> $FOLDER2 </strong></span>
				</div>
				<div class="box-icons">
					<a class="collapse-link">
						<i class="fa fa-chevron-up"></i>
					</a>
					<a class="expand-link">
						<i class="fa fa-expand"></i>
					</a>
					<a class="close-link">
						<i class="fa fa-times"></i>
					</a>
				</div>
				<div class="no-move"></div>
			</div>
		        <div class="box-content">
                <pre class="prettyprint" id="block">
<strong> <p>`/usr/bin/nslookup "$FOLDER2" 2> /dev/null` </p></strong>
</pre>
</div>
<div align="center"
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
</div></div></div>
EOF
		;;

			whois)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Whois result for <strong> $FOLDER3 </strong></span>
				</div>
				<div class="box-icons">
					<a class="collapse-link">
						<i class="fa fa-chevron-up"></i>
					</a>
					<a class="expand-link">
						<i class="fa fa-expand"></i>
					</a>
					<a class="close-link">
						<i class="fa fa-times"></i>
					</a>
				</div>
				<div class="no-move"></div>
			</div>
		        <div class="box-content">
                <pre class="prettyprint" id="block">
<div align="center"
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
<strong> <p>`/usr/bin/whois "$FOLDER3" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF
		  
              ;;			  
		
 			ip)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> IP Address for <strong> $FOLDER4 </strong></span>
				</div>
				<div class="box-icons">
					<a class="collapse-link">
						<i class="fa fa-chevron-up"></i>
					</a>
					<a class="expand-link">
						<i class="fa fa-expand"></i>
					</a>
					<a class="close-link">
						<i class="fa fa-times"></i>
					</a>
				</div>
				<div class="no-move"></div>
			</div>
		        <div class="box-content">
			 <pre id="block">
<strong> <h3><p align="center">`/usr/bin/dig +short "$FOLDER4" 2> /dev/null`</p></h3></strong>
</pre>
<div align="center"
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
</div>
</div></div></div>
EOF
 			  
              ;;	
                             
	     *)
	      echo " "
	      ;;
	  esac
	fi

cat << EOF

<div class="col-sm-5">
		<div>
<form method=POST>
<p><input type=radio name=cmd value=ip checked> <input id="searchbox" type=text placeholder="domain.tld" name=folder4>
<input id="submit" value="address" type=submit></p>       
<p><input type=radio name=cmd value=dig> <input id="searchbox" type=text placeholder=' ' name=folder>
<input id="submit" value="dig" type=submit></p>
<p><input type=radio name=cmd value=host> <input id="searchbox" type=text name=folder1>
<input id="submit" value="host" type=submit></p>
<p><input type=radio name=cmd value=nslookup> <input id="searchbox" type=text name=folder2>
<input id="submit" value="nslookup" type=submit></p>
<p><input type=radio name=cmd value=whois> <input id="searchbox" type=text name=folder3>
<input id="submit" value="whois" type=submit></p>		
</form>
		</div>	
</div>

EOF

./footer.cgi
 