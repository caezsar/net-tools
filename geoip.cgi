#!/bin/bash

POST=$(</dev/stdin)

./head.cgi

	# read in our parameters in form method get
  FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
         if [[ -z "$FOLDER4" ]]
    then
        echo " "
    else
	city=`geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat "$FOLDER4" | grep City | cut -d: -f2| sed 's/N\/A,//g'| sed 's/0,//g'`
	country=`geoiplookup "$FOLDER4" | grep Country | cut -d: -f 2| sed 's/N\/A,//g'| sed 's/0,//g'`
	asn=`geoiplookup "$FOLDER4" | grep ASN | cut -d: -f 2| sed 's/N\/A,//g'| sed 's/0,//g'`

cat << EOF

<div class="row">
	<div class="col-xs-12 col-sm-11">
		<div class="box">
			<div class="box-header">
				<div class="box-name">
					<i class="fa fa-search"></i>
					<span> GeoIP result for <strong> $FOLDER4 </strong></span>
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
<strong><p>
Country: $country 
City: $city
ASN: $asn </strong></p>
</pre>
</div>	
</div></div></div>
EOF

		fi

cat << EOF

<div class="col-sm-5">
		<div>
<form method=POST>
<input id="searchbox" type=text placeholder="domain.tld" name=folder4>
<input id="submit" value="geoip" type=submit>
</form>
		</div>	
</div>

EOF

./footer.cgi
 