#!/bin/bash

POST=$(</dev/stdin)

./head.cgi

	# read $CMD Parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER1=`echo "$POST" | sed -n 's/^.*folder1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
    FOLDER2=`echo "$POST" | sed -n 's/^.*folder2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER3=`echo "$POST" | sed -n 's/^.*folder3=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`

	# read $CMD1 in our parameters
	CMD1=`echo "$POST" | sed -n 's/^.*cmd1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDERA=`echo "$POST" | sed -n 's/^.*foldera=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	
	#### test if any parameters were passed ###
	if [ $CMD ]
	then
	  case "$CMD" in

            ping)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Ping result for <strong> $FOLDER </strong></span>
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
<strong> <p>`/bin/ping -c4 "$FOLDER" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF

		  ;;
				
            traceroute)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Traceroute result for <strong> $FOLDER1 </strong></span>
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
<strong> <p>`/usr/bin/traceroute "$FOLDER1" 2> /dev/null` </p></strong>
	</pre>
</div>
</div></div></div>
EOF
			  
              ;;
 
			tracerouten)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Traceroute numerical result for <strong> $FOLDER2 </strong></span>
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
<strong> <p>`/usr/bin/traceroute -n "$FOLDER2" 2> /dev/null` </p></strong>
	</pre>
</div>
</div></div></div>
EOF
		;;

			tracepath)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Tracepath result for <strong> $FOLDER3 </strong></span>
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
<strong> <p>`/usr/bin/tracepath "$FOLDER3" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF
		  
              ;;			  
		
 			tracepathn)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> Tracepath numerical for <strong> $FOLDER4 </strong></span>
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
<strong> <p>`/usr/bin/tracepath -n "$FOLDER4" 2> /dev/null` </p></strong>
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



	# test MTR parameters were passed
	if [ $CMD1 ]
	then
	  case "$CMD1" in

            dns)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> MTR for <strong> $FOLDERA </strong></span>
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
<strong> <p>`mtr --report "$FOLDERA" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF

				;;
				
            nodns)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> MTR numerical for <strong> $FOLDERA </strong></span>
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
<strong> <p>`mtr --report --no-dns "$FOLDERA" 2> /dev/null` </p></strong>
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
<p><input type=radio name=cmd value=ping checked> <input id="searchbox" type=text placeholder="$REMOTE_ADDR" name=folder>
<input id="submit" value="ping" type=submit></p>       
<p><input type=radio name=cmd value=traceroute> <input id="searchbox" type=text name=folder1>
<input id="submit" value="traceroute" type=submit></p>
<p><input type=radio name=cmd value=tracerouten> <input id="searchbox" type=text name=folder2>
<input id="submit" value="tracerouten" type=submit></p>
<p><input type=radio name=cmd value=tracepath> <input id="searchbox" type=text name=folder3>
<input id="submit" value="tracepath" type=submit></p>
<p><input type=radio name=cmd value=tracepathn> <input id="searchbox" type=text name=folder4>
<input id="submit" value="tracepathn" type=submit></p>		
</form>


<form method=POST>
	<select id="select" name="cmd1" value=cmd1>
		<option value="nodns">Output</option>
			<option value="nodns">No DNS</option>
			<option value="dns">Normal</option>
	</select>
		<input id="searchboxmtr" type=text placeholder="domain.tld"  name=foldera>
		<input id="submitmtr" value='mtr' type=submit>
</form>

		</div>	
</div>
		
		
		



EOF

./footer.cgi
 