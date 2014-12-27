#!/bin/bash

POST=$(</dev/stdin)

./head.cgi

check_port() {
         if test "$#" != "2" ; then
                echo -e " Use script like this:\n"$O" host port "
                exit 1
        else
           nc -z -w 5 $1 $2 2> /dev/null
                result=`echo $?`
				
        case "$result" in 
        
        1)
cat << EOF       
<h4 align="center"><strong><a style="color:#AE0C32">FAILURE!</a></strong></h4>
<h4 align="center"><strong>Port<a style="color:#AE0C32"> "$2" </a>not open on host<a style="color:#AE0C32"> "$1"</a>!</strong></h4>
EOF
        ;;
        
        0)
cat << EOF       
<h4 align="center"><strong><a style="color:#00BE49">SUCCESS!</a></strong></h4>
<h4 align="center"><strong>Port<a style="color:#00BE49"> "$2" </a>open on host<a style="color:#00BE49"> "$1"</a>!</strong></h4>
EOF
		;;
		
       *)
         echo -e "Error...!\nPort "$2" not open on host "$1"!"
        ;;
                esac
        fi
}

	# read CMD in our parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER7=`echo "$POST" | sed -n 's/^.*folder7=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER5=`echo "$POST" | sed -n 's/^.*folder5=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER6=`echo "$POST" | sed -n 's/^.*folder6=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
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
					<span> Scan results for <strong> $REMOTE_ADDR </strong></span>
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
<strong><p>`/usr/bin/nmap -T4 -F -n "$REMOTE_ADDR" 2> /dev/null` </p></strong>
</pre>
</div>	
</div></div></div>
EOF

		  ;;
				
            port)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Scan result for <strong> $FOLDER4 </strong> on port <strong> $FOLDER5 </strong></span>
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
`check_port "$FOLDER4" "$FOLDER5" 2> /dev/null`
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
<form method=POST>
<p><input type=radio name=cmd value=port checked> <input id="searchbox_portd" type=text placeholder="domain.tld" name=folder4> <input id="searchbox_port" type=text name=folder5 placeholder="80">
<input id="submit" value="check port" type=submit></p>       
<p><input type=radio name=cmd value=nmap> <input id="searchbox" type=text value="$REMOTE_ADDR" name=folder6>
<input id="submit" value="scan" type=submit></p>		
</form>
		</div>	
</div>

EOF

./footer.cgi
 