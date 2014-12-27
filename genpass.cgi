#!/bin/bash

POST=$(</dev/stdin)

./head.cgi

	#### read in our parameters ###
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER1=`echo "$POST" | sed -n 's/^.*folder1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
 
	
	#### test if any parameters were passed ###
	if [ $CMD ]
	then
	  case "$CMD" in

            complex)

genpassc() {
        local l=$1
        [ "$l" == "" ] && l="$FOLDER1"
        tr -dc A-Za-z0-9_\!\(\)\-\.\?\[\]\{\}\~\`\!@\#\$\%\&\* 2> /dev/null < /dev/urandom | head -c ${l} 2> /dev/null | xargs 2> /dev/null
}		
	
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Your complex password has<strong> $FOLDER1 </strong>characters lenght</span>
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
<strong><h3 align="center"><span style="color:#AE0C32">`genpassc`</span> </h3></strong>                                   
</pre>
</div>	
</div></div></div>
EOF

		  ;;
				
            simple)          
genpasss() {
        local l=$1
        [ "$l" == "" ] && l="$FOLDER"
        tr -dc A-Za-z0-9 2> /dev/null < /dev/urandom | head -c ${l} 2> /dev/null | xargs 2> /dev/null
}			
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Your simple password has<strong> $FOLDER </strong>characters lenght</span>
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
        <strong><h3 align="center"><span style="color:#AE0C32">`genpasss`</span></h3></strong>                          
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
<p><input type=radio name=cmd value=simple checked> <input id="searchbox" type=text placeholder="8" name=folder>
<input id="submit" value="simple" type=submit></p>       
<p><input type=radio name=cmd value=complex> <input id="searchbox" type=text placeholder='8' name=folder1>
<input id="submit" value="complex" type=submit></p>
		
</form>
		</div>	
</div>

EOF

./footer.cgi
 