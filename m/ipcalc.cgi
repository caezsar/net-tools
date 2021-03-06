#!/bin/bash

POST=$(</dev/stdin)
 
./head.cgi

	# read in our parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
  FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
  FOLDER5=`echo "$POST" | sed -n 's/^.*folder5=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	
	
	# test if any parameters were passed

	if [[ -z "$FOLDER4" ]]
    then
echo > /dev/null
    else

echo "<div id="text" align="center"><p>IP class information for $FOLDER4:</p></div>"
	echo "<div id="block" align="left"><pre>"
       		ipcalc "$FOLDER4" "$FOLDER5"
			
			echo "sIP Calculation:"
			sipcalc "$FOLDER4"
			
	echo "</div>"				  
		
	fi	  	                
	echo "</div>"
			  
			  
### SEARCH BLOCK ###	
echo "<div class="search_block">"	

####  SEARCH FORMS ###
cat << EOF
<div class="left">
<form method=POST>
<input id="searchbox" type=text placeholder="192.168.10.20/24" name=folder4>
<span id="af"> To </span><input id="searchbox2" type=text placeholder="24" name=folder5>
<input id="submit" value="calculate" type=submit>
</form>
</div>		
EOF

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "

./footer.cgi
