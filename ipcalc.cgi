#!/bin/bash

POST=$(</dev/stdin)

./head.cgi

	# read in our parameters in form method get
  FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
  FOLDER5=`echo "$POST" | sed -n 's/^.*folder5=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
         if [[ -z "$FOLDER4" ]]
    then
        echo " "
    else

cat << EOF

<div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> IP calculation result for <strong> $FOLDER4 </strong> network</span>
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
                <pre class="prettyprint" id="block"><strong><p>
`ipcalc "$FOLDER4" "$FOLDER5"`

</strong><div>
`echo "sIP Calculation:"`

`sipcalc "$FOLDER4"`
</div>
</p>
</pre>
</div>	
</div></div></div>
EOF

		fi	  
		

cat << EOF

<div class="col-sm-5">
		<div>
<form method=POST>
<input id="searchbox" type=text placeholder="192.168.10.20/24" name=folder4>
<span id="af"> To </span><input id="searchbox_port" type=text placeholder="24" name=folder5>
<input id="submit" value="calculate" type=submit>
</form>
		</div>	
</div>

EOF

./footer.cgi
 