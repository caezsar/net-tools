#!/bin/bash

POST=$(</dev/stdin)

./head.cgi

	# read in our parameters in form method get
  FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
         if [[ -z "$FOLDER4" ]]
    then
        echo " "
    else
	short_url=`curl -s http://tinyurl.com/api-create.php?url=$FOLDER4`

cat << EOF

<div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> TinyURL result for <strong> $FOLDER4 </strong></span>
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
                <pre id="block"><strong>
Short URL is : <font size="4px"><a href="$short_url" target="_blank" style="color:#AE0C32">$short_url</a></font></strong>
		</pre>
</div>	
</div></div></div>
EOF

		fi

cat << EOF

<div class="col-sm-5">
		<div>
<form method=POST>
<input id="searchbox" type=text placeholder="enter long string" name=folder4>
<input id="submit" value="tiny url" type=submit>
</form>
		</div>	
</div>

EOF

./footer.cgi
 