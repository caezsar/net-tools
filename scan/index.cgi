#!/bin/bash

./head.cgi


	# read in our parameters
	CMD=`echo "$QUERY_STRING" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER7=`echo "$QUERY_STRING" | sed -n 's/^.*folder7=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER4=`echo "$QUERY_STRING" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER5=`echo "$QUERY_STRING" | sed -n 's/^.*folder5=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER6=`echo "$QUERY_STRING" | sed -n 's/^.*folder6=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	#### test if any parameters were passed ###
	if [ $CMD ]
	then
	  case "$CMD" in

            nmap)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> SCAN result for <strong> $FOLDER6 </strong></span>
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
<strong> <p>`/usr/bin/nmap -T4 -F -n "$FOLDER6" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF

		  ;;
				
            nmap1)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Scan++ result for <strong> $FOLDER7 </strong></span>
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
<strong> <p>`/usr/bin/nmap -T4 -A -F -n "$FOLDER7" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF
			  
              ;;
 
			nmap2)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> No Ping Scan result for <strong> $FOLDER4 </strong></span>
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
<strong> <p>`/usr/bin/nmap -n -Pn "$FOLDER4" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF
		;;

			nmap3)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> No Ping Scan++ result for <strong> $FOLDER5 </strong></span>
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
<strong> <p>`/usr/bin/nmap -n -Pn -A "$FOLDER5"  2> /dev/null` </p></strong>
</pre>
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
<form method=GET>
<p><input type=radio name=cmd value=nmap checked> <input id="searchbox" type=text placeholder="domain.tld" name=folder6>
<input id="submit" value="scan" type=submit></p>       
<p><input type=radio name=cmd value=nmap1> <input id="searchbox" type=text name=folder7>
<input id="submit" value="scan++" type=submit></p>
<p><input type=radio name=cmd value=nmap2> <input id="searchbox" type=text name=folder4>
<input id="submit" value="no ping scan" type=submit></p>
<p><input type=radio name=cmd value=nmap3> <input id="searchbox" type=text name=folder5>
<input id="submit" value="no ping scan++" type=submit></p>		
</form>
		</div>	
</div>

EOF

./footer.cgi
 