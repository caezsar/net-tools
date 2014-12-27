#!/bin/bash

POST=$(</dev/stdin)

./head.cgi


	# read in our parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
		


	# test if any parameters were passed
	if [ $CMD ]
	then
	  case "$CMD" in

            a)

cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> A DNS records for <strong> $FOLDER </strong></span>
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
<strong> <p>`/usr/bin/host -t a "$FOLDER" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF

				;;
				
            mx)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> MX DNS records for <strong> $FOLDER </strong></span>
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
<strong> <p>`/usr/bin/host -t mx "$FOLDER" 2> /dev/null` </p></strong>
</pre></div>
</div></div></div>
EOF

              ;;
 
			spf)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> SPF DNS records for <strong> $FOLDER </strong></span>
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
<strong> <p>`/usr/bin/host -t txt "$FOLDER" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF
 
              ;;

			ns)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> NameServer DNS records for <strong> $FOLDER </strong></span>
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
<strong> <p>`/usr/bin/host -t ns "$FOLDER" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF
 				
              ;;			  

			soa)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> SOA DNS records for <strong> $FOLDER </strong></span>
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
<strong> <p>`/usr/bin/host -t soa "$FOLDER" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF
			
              ;;		
			
			cname)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> CNAME DNS records for <strong> $FOLDER </strong></span>
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
<strong> <p>`/usr/bin/host -t cname "$FOLDER" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF
				
              ;;		
          
			ttl)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> TTL DNS records for <strong> $FOLDER </strong></span>
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
<strong> <p>`/usr/bin/host -v "$FOLDER" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF
	  
              ;;		
			all)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> All DNS records for <strong> $FOLDER </strong></span>
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
<strong> <p>`/usr/bin/host -a "$FOLDER" 2> /dev/null` </p></strong>
</pre>
</div>
</div></div></div>
EOF

              ;;		              
			trace)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> DNS Trace result for <strong> $FOLDER </strong></span>
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
<strong><p> `/usr/bin/dig +trace "$FOLDER" 2> /dev/null` </p></strong>
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
	



			
<form role="form" method="POST">		
	<div class="col-sm-3">
			<select class="form-control" name="cmd" value=cmd>
		<option value="----">Select DNS Record</option>
		<option value="a">A</option>
        <option value="mx">MX</option>
		<option value="spf">SPF</option>
        <option value="ns">NS</option>
        <option value="soa">SOA</option>
        <option value="cname">CNAME</option>
        <option value="ttl">TTL</option>
        <option value="all">ALL</option>
        <option value="trace">TRACE</option>
			</select>      
	</div>
<div class="col-sm-4">
	<div class="form-group">
		<div class="input-group">
<input type="text" name="folder" class="form-control" placeholder="domain.tld">
<span class="input-group-btn">
<button type="submit" value="record" class="btn btn-primary btn-xs" type="button"> dns record </button>
</span>
		</div>
	</div>
</form>		
</div>

EOF

./footer.cgi
 