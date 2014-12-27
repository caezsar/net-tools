#!/bin/bash
echo "Content-type: text/html"
echo ""


## Declare IP Variables ##
remote_host=`./remote_host.pl 2> /dev/null| cut -d" " -f6`	   
city=`geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat $REMOTE_ADDR | grep City | cut -d: -f2| sed 's/N\/A,//g'| sed 's/0,//g'`
country=`geoiplookup $REMOTE_ADDR | grep Country | cut -d: -f 2| sed 's/N\/A,//g'| sed 's/0,//g'`
asn=`geoiplookup $REMOTE_ADDR | grep ASN | cut -d: -f 2| sed 's/N\/A,//g'| sed 's/0,//g'`




cat << EOF

<!DOCTYPE html>
<html lang="en">
	<head>
	
		<meta charset="utf-8">
		<title> Online Network Tools: DNS, IP, Whois, Traceroute, Email, Port Scan, IP Calculation, Ping, Traceroute, MTR, GeoIP, Google Map Location </title>
    <meta name="description" content="Free all-in-one online network troubleshooting, diagnostic and scanning tools at one awesome interface.">
    <meta name="keywords" content="dns, tools, ping, traceroute, check, http, headers, whois, lookup, password, generator, network, scanner, spf, tool, ip, calculation, geoip, mtr, google map location, nmap">
	<meta name="author" content="caezsar">
	<meta name="viewport" content="width=device-width, initial-scale=1">
		
		<link href="plugins/bootstrap/bootstrap.css" rel="stylesheet">

		<script type="text/javascript" src="js/run_prettify.js"></script>
		<script type="text/javascript" src="js/dashboard.js"></script>
		<link href="css/font-awesome.css" rel="stylesheet">
		<link href="css/font-awesome.min.css" rel="stylesheet">
		<link href="css/icons.css" rel="stylesheet">
		<link href="css/style_v2.css" rel="stylesheet">

		
<!-- Direct mobile devices to website mobile version -->
<script type="text/javascript">
if (screen.width <= 699) {
document.location = "m/";
}
</script>

<!-- SOCIAL BUTTON FLOAT  -->

<script type="text/javascript">
//<![CDATA[
  (function() {
    var shr = document.createElement('script');
    shr.setAttribute('data-cfasync', 'false');
    shr.src = '//dsms0mj1bbhn4.cloudfront.net/assets/pub/shareaholic.js';
    shr.type = 'text/javascript'; shr.async = 'true';
    shr.onload = shr.onreadystatechange = function() {
      var rs = this.readyState;
      if (rs && rs != 'complete' && rs != 'loaded') return;
      var site_id = 'e1b04c868e4c12a66b1fe1fe35faa297';
      try { Shareaholic.init(site_id); } catch (e) {}
    };
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(shr, s);
  })();
//]]>
</script>




<!-- GOOGLE ANALITICS -->
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-33207530-4', 'auto');
  ga('send', 'pageview');
</script>
		
	</head>



	
<body>
<!--Start Header-->

<div id="modalbox">
	<div class="devoops-modal">
		<div class="devoops-modal-header">
			<div class="modal-header-name">
				<span>Basic table</span>
			</div>
			<div class="box-icons">
				<a class="close-link">
					<i class="fa fa-times"></i>
				</a>
			</div>
		</div>
		<div class="devoops-modal-inner">
		</div>
		<div class="devoops-modal-bottom">
		</div>
	</div>
</div>
<header class="navbar">
	<div class="container-fluid expanded-panel">
		<div class="row">
<!-- LOGO -->		
			<div id="logo" class="col-xs-12 col-sm-2">
			   <a href="./" class="logo"> <img src=img/lg2.png width="135" height="35">
			</div>
			
			<div id="top-panel" class="col-xs-12 col-sm-10">
				<div class="row">
					<div class="col-xs-8 col-sm-4">				
				<!-- <a href="http://$REMOTE_ADDR"><span class="badge"> IP: $REMOTE_ADDR </span></a> -->
					</div>
					
					<div class="col-xs-4 col-sm-8 top-panel-right">
					
<a target="_blank" href="http://$REMOTE_ADDR"><span class="badge"> IP: $REMOTE_ADDR </span></a>
						
						<ul class="nav navbar-nav pull-right panel-menu">
<li class="hidden-xs"><a target="_blank" class="metro" href="/m" title='Mobile Version'><i class="icon-mobile"></i></a></li>							
<li class="hidden-xs"><a target="_blank" class="metro" href="/track.cgi" title='Track your location on Google Map!'><i class="icon-location"></i></a></li>
<li class="hidden-xs"><a target="_blank" class="metro" href="/scan" title='Scan Version'><i class="icon-search"></i></a></li>
<li class="hidden-xs"><a target="_blank" class="metro" href="https://www.facebook.com/TecMint" title='Facebook'><i class="icon-facebook"></i></a></li>
<li class="hidden-xs"><a target="_blank" class="metro" href="https://twitter.com/tecmint" title='Twitter'><i class="icon-twitter"></i></a></li>
<li class="hidden-xs"><a target="_blank" class="metro" href="https://plus.google.com/+Tecmint/posts" title='Google Plus'><i class="icon-google-plus"></i></a></li>
<li class="hidden-xs"><a target="_blank" class="metro" href="/" title='Home'><i class="icon-home"></i></a></li>
<li class="hidden-xs"><a target="_blank" class="metro" href="https://github.com/caezsar" title='Github'><i class="icon-github"></i></a></li>

						
							
						</ul>					
					</div>				
				</div>				
			</div>			
		</div>		
	</div>
				
				<div id="menu">

		<div id="social1">
<a href="./ "><span class="badges"> dns tools </span></a>
<a href="dns.cgi"><span class="badges"> dns records </span></a>
<a href="net.cgi"><span class="badges"> net tools </span></a>
<a href="mail.cgi"><span class="badges"> mail tools </span></a>
<a href="scan.cgi"><span class="badges"> scan tools </span></a>
<a href="geoip.cgi"><span class="badges"> geoip </span></a>
<a href="ipcalc.cgi"><span class="badges"> ipcalc </span></a>
<a href="headers.cgi"><span class="badges"> http head </span></a>
<a href="tinyurl.cgi"><span class="badges"> tiny url </span></a>
<a href="genpass.cgi"><span class="badges"> genpass </span></a>
			</div>
	
</header>
	

<!--End Header-->
<!--Start Container-->
<div id="main" class="container-fluid">

		
		<!--Start SUB HEAD Content-->
		
		<div class="row">
	<div id="breadcrumb" class="col-xs-12">
		
		<ol class="breadcrumb pull-left">
		<div id="social" class="pull-right">
		
	<!-- COMMENTED OUT
			<a target="_blank" class="metro" href="/m" title='Mobile Version'><i class="icon-mobile"></i></a>
			<a target="_blank" class="metro" href="/track.cgi" title='Track your location on Google Map!'><i class="icon-location"></i></a>
			<a target="_blank" class="metro" href="/scan" title='Scan Version'><i class="icon-search"></i></a>
			<a target="_blank" class="metro" href="https://www.facebook.com/TecMint" title='Facebook'><i class="icon-facebook"></i></a>
			<a target="_blank" class="metro" href="https://www.facebook.com/TecMint" title='Facebook'><i class="icon-twitter"></i></a>
			<a target="_blank" class="metro" href="https://www.facebook.com/TecMint" title='Facebook'><i class="icon-youtube"></i></a>		
	-->	
		</div>
		</ol>
		<div id="social" class="pull-right">
<a id="small">
Host:<span id="a"> $remote_host </span>&nbsp;
Country:<span id="a"> $country </span>&nbsp; 
City:<span id="a"> $city </span>&nbsp; 
ASN:<span id="a"> $asn </span></a>
<a class="metro" href="remote_scan.cgi" title='Auto IP Scan'><i class="icon-search"></i></a>
		</div>
	</div>
</div>


<!-- GOOGLE TOP ADD -->
<div id="topad" align="center">
               
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Tools_Top_720x90_Ad -->
<ins class="adsbygoogle"
     style="display:inline-block;width:720px;height:90px"
     data-ad-client="ca-pub-2601749019656699"
     data-ad-slot="3790603779"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

</div>

	
EOF
