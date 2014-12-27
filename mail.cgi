#!/bin/bash

POST=$(</dev/stdin)


./head.cgi

smtp() {
nc -w 20 $FOLDER 25 2> /dev/null << EOF
EHLO $FOLDER
MAIL FROM:<postmaster@$FOLDER>
RCPT TO:<test@domain.tld>
QUIT
EOF
}

smtp_ssl() {
nc -w 20 $FOLDER1 465 2> /dev/null << EOF
EHLO $FOLDER1
MAIL FROM:<postmaster@$FOLDER1>
RCPT TO:<test@domain.tld>
QUIT
EOF
}

smtp_tls() {
nc -w 20  $FOLDER2 587 2> /dev/null << EOF
EHLO $FOLDER2
MAIL FROM:<postmaster@$FOLDER2>
RCPT TO:<test@domain.tld>
QUIT
EOF
}

pop3() {
nc -w 20 $FOLDER3 110 2> /dev/null << EOF
USER postmaster@$FOLDER3
PASS password
LIST
QUIT
EOF
}

pop3s() {
openssl s_client -connect $FOLDER4:995 2> /dev/null << EOF
USER postmaster@$FOLDER4
PASS password
QUIT
EOF
}

imap() {
nc -w 20 $FOLDER5 143 2> /dev/null << EOF
a1 LOGIN postmaster@$FOLDER5 password
a2 LOGOUT
EOF
}

imaps() {
openssl s_client -connect $FOLDER6:993 2> /dev/null << EOF
a1 LOGIN postmaster@$FOLDER6 password
a2 LOGOUT
EOF
}

	# read MAIL in our parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER1=`echo "$POST" | sed -n 's/^.*folder1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
    FOLDER2=`echo "$POST" | sed -n 's/^.*folder2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER3=`echo "$POST" | sed -n 's/^.*folder3=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER5=`echo "$POST" | sed -n 's/^.*folder5=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER6=`echo "$POST" | sed -n 's/^.*folder6=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`	
	FOLDER7=`echo "$POST" | sed -n 's/^.*folder7=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`	
	FOLDER8=`echo "$POST" | sed -n 's/^.*folder8=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`		



	# test if any parameters were passed
	if [ $CMD ]
	then
	  case "$CMD" in

            25)

cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> SMTP test for <strong> $FOLDER </strong></span>
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

<strong><p>`smtp "$FOLDER" 2> /dev/null`</p></strong>

</pre>
</div>	
</div></div></div>
EOF

				;;
				
            465)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> SMTP SSL test for <strong> $FOLDER1 </strong></span>
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
<strong><p>`smtp_ssl "$FOLDER1" 2> /dev/null` </p></strong>

</pre>
</div>	
</div></div></div>
EOF

              ;;
 
			587)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> SMTP TLS test for <strong> $FOLDER2 </strong></span>
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

<strong> <p>`smtp_tls "$FOLDER2" 2> /dev/null`</p></strong>

</pre>
</div>
</div></div></div>
EOF
 
              ;;

			110)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> POP3 Mail test for <strong> $FOLDER3 </strong></span>
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
<strong> <p>`pop3 "$FOLDER3" 2> /dev/null`</p></strong>

</pre>
</div>
</div></div></div>
EOF
 				
              ;;			  

			995)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> POP3 SSL Mail test for <strong> $FOLDER4 </strong></span>
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
<strong> <p>`pop3s "$FOLDER4" 2> /dev/null` </p></strong>
	</pre>
</div>
</div></div></div>
EOF
			
              ;;		
			
			143)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> IMAP Mail test for <strong> $FOLDER5 </strong></span>
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
<strong> <p>`imap "$FOLDER5" 2> /dev/null` </p></strong>
	</pre>
</div>
</div></div></div>
EOF
				
              ;;		
          
			993)
cat << EOF			
 <div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> IMAP SSL Mail test for <strong> $FOLDER6 </strong></span>
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
<strong> <p>`imaps "$FOLDER6" 2> /dev/null` </p></strong>
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
<p><input type=radio name=cmd value=25 checked> <input id="searchbox" type=text placeholder="domain.tld" name=folder>
<input id="submit" value="25 SMTP" type=submit></p>       
<p><input type=radio name=cmd value=465> <input id="searchbox" type=text placeholder=' ' name=folder1>
<input id="submit" value="465 SSL" type=submit></p>
<p><input type=radio name=cmd value=587> <input id="searchbox" type=text name=folder2>
<input id="submit" value="587 TLS" type=submit></p>
<p><input type=radio name=cmd value=110> <input id="searchbox" type=text name=folder3>
<input id="submit" value="110 POP3" type=submit></p>
<p><input type=radio name=cmd value=995> <input id="searchbox" type=text name=folder4>
<input id="submit" value="995 POP3S" type=submit></p>
<p><input type=radio name=cmd value=143> <input id="searchbox" type=text name=folder5>
<input id="submit" value="143 IMAP" type=submit></p>
<p><input type=radio name=cmd value=993> <input id="searchbox" type=text name=folder6>
<input id="submit" value="993 IMAPS" type=submit></p>
</form>
		</div>	
</div>

EOF

./footer.cgi
 