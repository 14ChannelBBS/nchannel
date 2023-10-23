<?php
	$reasons = array("ローカルルール違反","スレッド・板の趣旨に無関係な投稿","マルチポスト・スパム・埋め立てなどの荒らし行為全般","人種差別・性差別など差別全般","故意にサーバーに負荷をかける行為","アフィサイトへの転載や、ロンダリング目的の投稿","特定の人物・団体・サイトへの過度な嫌がらせ・誹謗中傷","許可なく自動投稿プログラムを使用する行為","デマを流す行為","自作自演行為","グロ画像など人を不快にするコンテンツの投稿","ブラクラ・マルウェアなど有害なプログラムの投稿","ステルスマーケティング行為","麻薬取引","児童ポルノの投稿","テロ予告や、方法・日時・場所などを指定した具体的な殺害予告");
	if ($_POST["kaku"] != "kaku"){
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html><head>
 
 <meta http-equiv="Content-Type" content="text/html;charset=Shift-JIS">
 <meta http-equiv="Content-Script-Type" content="text/javascript">
 

 <title>スレッド・レスの通報フォーム - 14Channel BBS</title>

<!--
function l(e) {
	var N = getCookie("cookName"), M = getCookie("cookMail");
	for (var i = 0, j = document.forms ; i < j.length ; i++){
		if (j[i].FROM && j[i].mail) {
			j[i].FROM.value = N;
			j[i].mail.value = M;
		}}
}
window.onload = l;
function getCookie(key) {
	var ptrn = '(?:^|;| )' + key + '="(.*?)"';
	if (document.cookie.match(ptrn))
		return decodeURIComponent(RegExp.$1);
	return "";
}
//-->
</script>
<meta name="twitter:card" content="summary_large_image">
<meta property="og:image" content="./kanban.png">
<meta property="og:title" content="14Channel BBS - 14Channel Lab">
<meta property="og:description" content="･転んでも泣かない･出されたものは残さず食べる･Perl使いを尊重する">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<meta name="msapplication-square70x70logo" content="/favicons/site-tile-70x70.png">
<meta name="msapplication-square150x150logo" content="/favicons/site-tile-150x150.png">
<meta name="msapplication-wide310x150logo" content="/favicons/site-tile-310x150.png">
<meta name="msapplication-square310x310logo" content="/favicons/site-tile-310x310.png">
<meta name="msapplication-TileColor" content="#0078d7">
<link rel="shortcut icon" type="image/vnd.microsoft.icon" href="/favicon.ico">
<link rel="icon" type="image/vnd.microsoft.icon" href="/favicon.ico">
<link rel="apple-touch-icon" sizes="57x57" href="/favicons/apple-touch-icon-57x57.png">
<link rel="apple-touch-icon" sizes="60x60" href="/favicons/apple-touch-icon-60x60.png">
<link rel="apple-touch-icon" sizes="72x72" href="/favicons/apple-touch-icon-72x72.png">
<link rel="apple-touch-icon" sizes="76x76" href="/favicons/apple-touch-icon-76x76.png">
<link rel="apple-touch-icon" sizes="114x114" href="/favicons/apple-touch-icon-114x114.png">
<link rel="apple-touch-icon" sizes="120x120" href="/favicons/apple-touch-icon-120x120.png">
<link rel="apple-touch-icon" sizes="144x144" href="/favicons/apple-touch-icon-144x144.png">
<link rel="apple-touch-icon" sizes="152x152" href="/favicons/apple-touch-icon-152x152.png">
<link rel="apple-touch-icon" sizes="180x180" href="/favicons/apple-touch-icon-180x180.png">
<link rel="icon" type="image/png" sizes="36x36" href="/favicons/android-chrome-36x36.png">
<link rel="icon" type="image/png" sizes="48x48" href="/favicons/android-chrome-48x48.png">
<link rel="icon" type="image/png" sizes="72x72" href="/favicons/android-chrome-72x72.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicons/android-chrome-96x96.png">
<link rel="icon" type="image/png" sizes="128x128" href="/favicons/android-chrome-128x128.png">
<link rel="icon" type="image/png" sizes="144x144" href="/favicons/android-chrome-144x144.png">
<link rel="icon" type="image/png" sizes="152x152" href="/favicons/android-chrome-152x152.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicons/android-chrome-192x192.png">
<link rel="icon" type="image/png" sizes="256x256" href="/favicons/android-chrome-256x256.png">
<link rel="icon" type="image/png" sizes="384x384" href="/favicons/android-chrome-384x384.png">
<link rel="icon" type="image/png" sizes="512x512" href="/favicons/android-chrome-512x512.png">
<link rel="icon" type="image/png" sizes="36x36" href="/favicons/icon-36x36.png">
<link rel="icon" type="image/png" sizes="48x48" href="/favicons/icon-48x48.png">
<link rel="icon" type="image/png" sizes="72x72" href="/favicons/icon-72x72.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicons/icon-96x96.png">
<link rel="icon" type="image/png" sizes="128x128" href="/favicons/icon-128x128.png">
<link rel="icon" type="image/png" sizes="144x144" href="/favicons/icon-144x144.png">
<link rel="icon" type="image/png" sizes="152x152" href="/favicons/icon-152x152.png">
<link rel="icon" type="image/png" sizes="160x160" href="/favicons/icon-160x160.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicons/icon-192x192.png">
<link rel="icon" type="image/png" sizes="196x196" href="/favicons/icon-196x196.png">
<link rel="icon" type="image/png" sizes="256x256" href="/favicons/icon-256x256.png">
<link rel="icon" type="image/png" sizes="384x384" href="/favicons/icon-384x384.png">
<link rel="icon" type="image/png" sizes="512x512" href="/favicons/icon-512x512.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicons/icon-16x16.png">
<link rel="icon" type="image/png" sizes="24x24" href="/favicons/icon-24x24.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicons/icon-32x32.png">
<link rel="manifest" href="/favicons/manifest.json">
	<script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4330360014245167" crossorigin="anonymous" data-checked-head="true"></script>
	 <link href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.7.1/css/lightbox.css" rel="stylesheet">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script><script charset="utf-8" src="chrome-extension://donbcfbmhbcapadipfkeojnmajbakjdc/dist/ruffle.js?id=57056776348"></script><meta http-equiv="origin-trial" content="As0hBNJ8h++fNYlkq8cTye2qDLyom8NddByiVytXGGD0YVE+2CEuTCpqXMDxdhOMILKoaiaYifwEvCRlJ/9GcQ8AAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3MTk1MzI3OTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="AgRYsXo24ypxC89CJanC+JgEmraCCBebKl8ZmG7Tj5oJNx0cmH0NtNRZs3NB5ubhpbX/bIt7l2zJOSyO64NGmwMAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3MTk1MzI3OTksImlzU3ViZG9tYWluIjp0cnVlfQ==">
<script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.7.1/js/lightbox.min.js" type="text/javascript"></script>
<script async="" src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</head><iframe id="google_esf" name="google_esf" src="https://googleads.g.doubleclick.net/pagead/html/r20231017/r20190131/zrt_lookup.html" style="display: none;" data-ruffle-polyfilled=""></iframe>
<!--nobanner-->
<body vlink="#AA0088" text="#000000" link="#0000FF" bgcolor="#FFFFFF" background="/lab/ba.gif" alink="#FF0000">
<!-- [FC2 Analyzer] //analyzer.fc2.com/  -->
<script language="javascript" src="//analyzer54.fc2.com/ana/processor.php?uid=2894165" type="text/javascript"></script><ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;" data-ad-status="unfilled"><div id="aswift_0_host" style="border: none; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;" tabindex="0" title="Advertisement" aria-label="Advertisement"><iframe id="aswift_0" name="aswift_0" browsingtopics="true" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-4330360014245167&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;lmt=1697802579&amp;plat=1%3A1024%2C2%3A1024%2C3%3A2097152%2C4%3A2097152%2C9%3A32776%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1081344%2C32%3A32%2C41%3A32%2C42%3A32&amp;format=0x0&amp;url=https%3A%2F%2Fapple.14chan.cf%2Flab%2F&amp;ea=0&amp;pra=5&amp;wgl=1&amp;easpi=0&amp;asro=0&amp;asiscm=1&amp;aslmt=0.4&amp;asamt=-1&amp;asedf=0&amp;asefa=1&amp;aseiel=1~2&amp;uach=WyJXaW5kb3dzIiwiMTAuMC4wIiwieDg2IiwiIiwiMTE4LjAuNTk5My44OSIsW10sMCxudWxsLCI2NCIsW1siQ2hyb21pdW0iLCIxMTguMC41OTkzLjg5Il0sWyJHb29nbGUgQ2hyb21lIiwiMTE4LjAuNTk5My44OSJdLFsiTm90PUE_QnJhbmQiLCI5OS4wLjAuMCJdXSwwXQ..&amp;dt=1697845469115&amp;bpp=143&amp;bdt=190&amp;idt=206&amp;shv=r20231017&amp;mjsv=m202310180101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3D7091f419602a8b2c-22b7a07160e40095%3AT%3D1696593946%3ART%3D1697845158%3AS%3DALNI_MZ501vOmBD3y1EgK4EtSHEpIOibOg&amp;gpic=UID%3D00000c59279a2576%3AT%3D1696593946%3ART%3D1697845158%3AS%3DALNI_MYayvNUAw_nun1UCjM73tL6P8rAyw&amp;nras=1&amp;correlator=6944451689962&amp;frm=20&amp;pv=2&amp;ga_vid=1955798766.1697423348&amp;ga_sid=1697845469&amp;ga_hid=1945975442&amp;ga_fc=1&amp;u_tz=540&amp;u_his=1&amp;u_h=768&amp;u_w=1366&amp;u_ah=728&amp;u_aw=1366&amp;u_cd=24&amp;u_sd=1&amp;dmc=4&amp;adx=-12245933&amp;ady=-12245933&amp;biw=1366&amp;bih=607&amp;scr_x=0&amp;scr_y=0&amp;eid=44759927%2C44759876%2C31078019%2C31078831%2C44795922%2C44805112%2C44805534%2C44805680%2C44805918%2C44805933%2C31078297%2C31079012%2C44803794%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=3884234530048862&amp;tmod=32748251&amp;uas=0&amp;nvt=1&amp;fsapi=1&amp;ref=https%3A%2F%2Fapple.14chan.cf%2Ftest%2Fread.cgi%2Flab%2F1697802449%2F&amp;fc=1920&amp;brdim=0%2C0%2C0%2C0%2C1366%2C0%2C1366%2C728%2C1366%2C607&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=32768&amp;bc=31&amp;td=1&amp;nt=1&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;dtd=241" data-google-container-id="a!1" data-load-complete="true" data-ruffle-polyfilled=""></iframe></div></ins><a href="https://fc2.com/"><img id="fc2analyzerimg_" src="https://analyzer54.fc2.com/ana/icon61.gif" alt="FC2 Analyzer" style="position: absolute; left: 0px; top: 0px; border: 0px solid rgb(255, 255, 255); z-index: 2147483647; display: none;"></a><script src="https://analyzer54.fc2.com/ana/analyzer.php?uid=2894165&amp;amp;pid=0&amp;amp;idsess=&amp;amp;ref=https%3A//apple.14chan.cf/test/read.cgi/lab/1697802449/&amp;amp;href=https%3A//apple.14chan.cf/lab/&amp;amp;wid=1366&amp;amp;hei=768&amp;amp;col=24&amp;amp;visitor=1-2056012135-1697277962-1697845166-53-3-1697622478&amp;amp;ssl=0" charset="UTF-8"></script>
<noscript><div align="right"><img src="//analyzer54.fc2.com/ana/icon.php?uid=2894165&ref=&href=&wid=0&hei=0&col=0" /></div></noscript>
<!-- [FC2 Analyzer]  -->
<a name="top"></a>
<div align="center"><a href="//"><img src="/lab/kanban.png" alt="14Channel BBS" border="0"></a></div>
<a name="info"></a>
<table style="margin-bottom:1.2em;" width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#CCFFCC" align="center">
 <tbody><tr>
  <td>
  <table width="100%" border="0">
   <tbody><tr>
	<td><font size="+1"><b>スレッド・レスの通報フォーム</b></font></td>
	<td align="right"><a href="#menu">■</a> <a href="#1">▼</a></td>
   </tr>
   <tr>
	<td colspan="2">
	<div align="center" style="margin: 1.2em 0;">
		<p>スレッドや、レスの通報をしたい場合は、下のフォームを使って通報をお願いします。</p><br>
		<p>理由一覧：<br>
		・ローカルルール違反 <br>
		・スレッド・板の趣旨に無関係な投稿 <br>
		・マルチポスト・スパム・埋め立てなどの荒らし行為全般 <br>
		・人種差別・性差別など差別全般 <br>
		・故意にサーバーに負荷をかける行為 <br>
		・アフィサイトへの転載や、ロンダリング目的の投稿 <br>
		・特定の人物・団体・サイトへの過度な嫌がらせ・誹謗中傷 <br>
		・許可なく自動投稿プログラムを使用する行為 <br>
		・デマを流す行為 <br>
		・自作自演行為 <br>
		・グロ画像など人を不快にするコンテンツの投稿 <br>
		・ブラクラ・マルウェアなど有害なプログラムの投稿 <br>
		・ステルスマーケティング行為 <br>
		・麻薬取引 <br>
		・児童ポルノの投稿 <br>
		・テロ予告や、方法・日時・場所などを指定した具体的な殺害予告 </p>
	</td>
   </tr>
   <form method="POST" action="/test/report.cgi">
<table style="margin-bottom:1.2em;" width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#CCFFCC" align="center">
 <tbody><tr>
  <td nowrap="">
  <b>スレッド・レスの通報</b><br>
  スレッド・レスのURL：<input placeholder="https://apple.14chan.cf/test/read.cgi/lab/1696505965/1" type="text" name="url" size="40" value="<?=$_GET["url"]?>" pattern="^(https?):\/\/(apple\.14chan\.cf|nchannel\.osdn\.jp|nchannel\.osdn\.io)\/test\/read.cgi\/.*$" reuqired><input type="submit" value="通報"><br>
  理由：
  <select name="reason" required>
 	 <option value="">--選択してください--</option>
	 <option value="0">ローカルルール違反</option>
	 <option value="1">スレッド・板の趣旨に無関係な投稿</option>
	 <option value="2">マルチポスト・スパム・埋め立てなどの荒らし行為全般</option>
	 <option value="3">人種差別・性差別など差別全般</option>
	 <option value="4">故意にサーバーに負荷をかける行為</option>
	 <option value="5">アフィサイトへの転載や、ロンダリング目的の投稿</option>
	 <option value="6">特定の人物・団体・サイトへの過度な嫌がらせ・誹謗中傷</option>
	 <option value="7">許可なく自動投稿プログラムを使用する行為</option>
	 <option value="8">デマを流す行為</option>
	 <option value="9">自作自演行為</option>
	 <option value="10">グロ画像など人を不快にするコンテンツの投稿</option>
	 <option value="11">ブラクラ・マルウェアなど有害なプログラムの投稿</option>
	 <option value="12">ステルスマーケティング行為</option>
	 <option value="13">麻薬取引</option>
	 <option value="14">児童ポルノの投稿</option>
	 <option value="15">テロ予告や、方法・日時・場所などを指定した具体的な殺害予告</option>
  </select>
  <br>備考：<br><textarea name="bikou" rows="5" cols="70"></textarea>
  <input type="hidden" name="kaku" value="kaku" />
<br>
  </td>
 </tr>
</tbody></table>
</form>
  </tbody></table>
  </td>
 </tr>
</tbody></table>

<a name="ad"></a>
<table width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#ccffcc" align="center">
<tbody><tr><td>
<!-- FC2カウンター ここから -->
<script language="javascript" type="text/javascript" src="//counter1.fc2.com/counter.php?id=89505170"></script><noscript><img src="//counter1.fc2.com/counter_img.php?id=89505170" /></noscript>
<!-- FC2カウンター ここまで -->
<br>
<!-- FC2カウンター ここから -->
現在の閲覧者数:<script language="javascript" type="text/javascript" src="//counter1.fc2.com/views.php?id=89505170"></script><script src="https://counter1.fc2.com/views_js.php?id=89505170&amp;main=0&amp;lang=0" charset="UTF-8"></script><noscript><img src="//counter1.fc2.com/counter_now.php?id=89505170" /></noscript>
<!-- FC2カウンター ここまで -->
</td></tr>
</tbody></table>
</body></html>
<?php




	}else{






?>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html><head>
 
 <meta http-equiv="Content-Type" content="text/html;charset=Shift-JIS">
 <meta http-equiv="Content-Script-Type" content="text/javascript">
 

 <title>スレッド・レスの通報フォーム - 14Channel BBS</title>

<!--
function l(e) {
	var N = getCookie("cookName"), M = getCookie("cookMail");
	for (var i = 0, j = document.forms ; i < j.length ; i++){
		if (j[i].FROM && j[i].mail) {
			j[i].FROM.value = N;
			j[i].mail.value = M;
		}}
}
window.onload = l;
function getCookie(key) {
	var ptrn = '(?:^|;| )' + key + '="(.*?)"';
	if (document.cookie.match(ptrn))
		return decodeURIComponent(RegExp.$1);
	return "";
}
//-->
</script>
<meta name="twitter:card" content="summary_large_image">
<meta property="og:image" content="./kanban.png">
<meta property="og:title" content="14Channel BBS - 14Channel Lab">
<meta property="og:description" content="･転んでも泣かない･出されたものは残さず食べる･Perl使いを尊重する">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<meta name="msapplication-square70x70logo" content="/favicons/site-tile-70x70.png">
<meta name="msapplication-square150x150logo" content="/favicons/site-tile-150x150.png">
<meta name="msapplication-wide310x150logo" content="/favicons/site-tile-310x150.png">
<meta name="msapplication-square310x310logo" content="/favicons/site-tile-310x310.png">
<meta name="msapplication-TileColor" content="#0078d7">
<link rel="shortcut icon" type="image/vnd.microsoft.icon" href="/favicon.ico">
<link rel="icon" type="image/vnd.microsoft.icon" href="/favicon.ico">
<link rel="apple-touch-icon" sizes="57x57" href="/favicons/apple-touch-icon-57x57.png">
<link rel="apple-touch-icon" sizes="60x60" href="/favicons/apple-touch-icon-60x60.png">
<link rel="apple-touch-icon" sizes="72x72" href="/favicons/apple-touch-icon-72x72.png">
<link rel="apple-touch-icon" sizes="76x76" href="/favicons/apple-touch-icon-76x76.png">
<link rel="apple-touch-icon" sizes="114x114" href="/favicons/apple-touch-icon-114x114.png">
<link rel="apple-touch-icon" sizes="120x120" href="/favicons/apple-touch-icon-120x120.png">
<link rel="apple-touch-icon" sizes="144x144" href="/favicons/apple-touch-icon-144x144.png">
<link rel="apple-touch-icon" sizes="152x152" href="/favicons/apple-touch-icon-152x152.png">
<link rel="apple-touch-icon" sizes="180x180" href="/favicons/apple-touch-icon-180x180.png">
<link rel="icon" type="image/png" sizes="36x36" href="/favicons/android-chrome-36x36.png">
<link rel="icon" type="image/png" sizes="48x48" href="/favicons/android-chrome-48x48.png">
<link rel="icon" type="image/png" sizes="72x72" href="/favicons/android-chrome-72x72.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicons/android-chrome-96x96.png">
<link rel="icon" type="image/png" sizes="128x128" href="/favicons/android-chrome-128x128.png">
<link rel="icon" type="image/png" sizes="144x144" href="/favicons/android-chrome-144x144.png">
<link rel="icon" type="image/png" sizes="152x152" href="/favicons/android-chrome-152x152.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicons/android-chrome-192x192.png">
<link rel="icon" type="image/png" sizes="256x256" href="/favicons/android-chrome-256x256.png">
<link rel="icon" type="image/png" sizes="384x384" href="/favicons/android-chrome-384x384.png">
<link rel="icon" type="image/png" sizes="512x512" href="/favicons/android-chrome-512x512.png">
<link rel="icon" type="image/png" sizes="36x36" href="/favicons/icon-36x36.png">
<link rel="icon" type="image/png" sizes="48x48" href="/favicons/icon-48x48.png">
<link rel="icon" type="image/png" sizes="72x72" href="/favicons/icon-72x72.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicons/icon-96x96.png">
<link rel="icon" type="image/png" sizes="128x128" href="/favicons/icon-128x128.png">
<link rel="icon" type="image/png" sizes="144x144" href="/favicons/icon-144x144.png">
<link rel="icon" type="image/png" sizes="152x152" href="/favicons/icon-152x152.png">
<link rel="icon" type="image/png" sizes="160x160" href="/favicons/icon-160x160.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicons/icon-192x192.png">
<link rel="icon" type="image/png" sizes="196x196" href="/favicons/icon-196x196.png">
<link rel="icon" type="image/png" sizes="256x256" href="/favicons/icon-256x256.png">
<link rel="icon" type="image/png" sizes="384x384" href="/favicons/icon-384x384.png">
<link rel="icon" type="image/png" sizes="512x512" href="/favicons/icon-512x512.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicons/icon-16x16.png">
<link rel="icon" type="image/png" sizes="24x24" href="/favicons/icon-24x24.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicons/icon-32x32.png">
<link rel="manifest" href="/favicons/manifest.json">
	<script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4330360014245167" crossorigin="anonymous" data-checked-head="true"></script>
	 <link href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.7.1/css/lightbox.css" rel="stylesheet">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script><script charset="utf-8" src="chrome-extension://donbcfbmhbcapadipfkeojnmajbakjdc/dist/ruffle.js?id=57056776348"></script><meta http-equiv="origin-trial" content="As0hBNJ8h++fNYlkq8cTye2qDLyom8NddByiVytXGGD0YVE+2CEuTCpqXMDxdhOMILKoaiaYifwEvCRlJ/9GcQ8AAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3MTk1MzI3OTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="AgRYsXo24ypxC89CJanC+JgEmraCCBebKl8ZmG7Tj5oJNx0cmH0NtNRZs3NB5ubhpbX/bIt7l2zJOSyO64NGmwMAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3MTk1MzI3OTksImlzU3ViZG9tYWluIjp0cnVlfQ==">
<script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.7.1/js/lightbox.min.js" type="text/javascript"></script>
<script async="" src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</head><iframe id="google_esf" name="google_esf" src="https://googleads.g.doubleclick.net/pagead/html/r20231017/r20190131/zrt_lookup.html" style="display: none;" data-ruffle-polyfilled=""></iframe>
<!--nobanner-->
<body vlink="#AA0088" text="#000000" link="#0000FF" bgcolor="#FFFFFF" background="/lab/ba.gif" alink="#FF0000">
<!-- [FC2 Analyzer] //analyzer.fc2.com/  -->
<script language="javascript" src="//analyzer54.fc2.com/ana/processor.php?uid=2894165" type="text/javascript"></script><ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;" data-ad-status="unfilled"><div id="aswift_0_host" style="border: none; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;" tabindex="0" title="Advertisement" aria-label="Advertisement"><iframe id="aswift_0" name="aswift_0" browsingtopics="true" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-4330360014245167&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;lmt=1697802579&amp;plat=1%3A1024%2C2%3A1024%2C3%3A2097152%2C4%3A2097152%2C9%3A32776%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1081344%2C32%3A32%2C41%3A32%2C42%3A32&amp;format=0x0&amp;url=https%3A%2F%2Fapple.14chan.cf%2Flab%2F&amp;ea=0&amp;pra=5&amp;wgl=1&amp;easpi=0&amp;asro=0&amp;asiscm=1&amp;aslmt=0.4&amp;asamt=-1&amp;asedf=0&amp;asefa=1&amp;aseiel=1~2&amp;uach=WyJXaW5kb3dzIiwiMTAuMC4wIiwieDg2IiwiIiwiMTE4LjAuNTk5My44OSIsW10sMCxudWxsLCI2NCIsW1siQ2hyb21pdW0iLCIxMTguMC41OTkzLjg5Il0sWyJHb29nbGUgQ2hyb21lIiwiMTE4LjAuNTk5My44OSJdLFsiTm90PUE_QnJhbmQiLCI5OS4wLjAuMCJdXSwwXQ..&amp;dt=1697845469115&amp;bpp=143&amp;bdt=190&amp;idt=206&amp;shv=r20231017&amp;mjsv=m202310180101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3D7091f419602a8b2c-22b7a07160e40095%3AT%3D1696593946%3ART%3D1697845158%3AS%3DALNI_MZ501vOmBD3y1EgK4EtSHEpIOibOg&amp;gpic=UID%3D00000c59279a2576%3AT%3D1696593946%3ART%3D1697845158%3AS%3DALNI_MYayvNUAw_nun1UCjM73tL6P8rAyw&amp;nras=1&amp;correlator=6944451689962&amp;frm=20&amp;pv=2&amp;ga_vid=1955798766.1697423348&amp;ga_sid=1697845469&amp;ga_hid=1945975442&amp;ga_fc=1&amp;u_tz=540&amp;u_his=1&amp;u_h=768&amp;u_w=1366&amp;u_ah=728&amp;u_aw=1366&amp;u_cd=24&amp;u_sd=1&amp;dmc=4&amp;adx=-12245933&amp;ady=-12245933&amp;biw=1366&amp;bih=607&amp;scr_x=0&amp;scr_y=0&amp;eid=44759927%2C44759876%2C31078019%2C31078831%2C44795922%2C44805112%2C44805534%2C44805680%2C44805918%2C44805933%2C31078297%2C31079012%2C44803794%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=3884234530048862&amp;tmod=32748251&amp;uas=0&amp;nvt=1&amp;fsapi=1&amp;ref=https%3A%2F%2Fapple.14chan.cf%2Ftest%2Fread.cgi%2Flab%2F1697802449%2F&amp;fc=1920&amp;brdim=0%2C0%2C0%2C0%2C1366%2C0%2C1366%2C728%2C1366%2C607&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=32768&amp;bc=31&amp;td=1&amp;nt=1&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;dtd=241" data-google-container-id="a!1" data-load-complete="true" data-ruffle-polyfilled=""></iframe></div></ins><a href="https://fc2.com/"><img id="fc2analyzerimg_" src="https://analyzer54.fc2.com/ana/icon61.gif" alt="FC2 Analyzer" style="position: absolute; left: 0px; top: 0px; border: 0px solid rgb(255, 255, 255); z-index: 2147483647; display: none;"></a><script src="https://analyzer54.fc2.com/ana/analyzer.php?uid=2894165&amp;amp;pid=0&amp;amp;idsess=&amp;amp;ref=https%3A//apple.14chan.cf/test/read.cgi/lab/1697802449/&amp;amp;href=https%3A//apple.14chan.cf/lab/&amp;amp;wid=1366&amp;amp;hei=768&amp;amp;col=24&amp;amp;visitor=1-2056012135-1697277962-1697845166-53-3-1697622478&amp;amp;ssl=0" charset="UTF-8"></script>
<noscript><div align="right"><img src="//analyzer54.fc2.com/ana/icon.php?uid=2894165&ref=&href=&wid=0&hei=0&col=0" /></div></noscript>
<!-- [FC2 Analyzer]  -->
<a name="top"></a>
<div align="center"><a href="//"><img src="/lab/kanban.png" alt="14Channel BBS" border="0"></a></div>
<a name="info"></a>
<table style="margin-bottom:1.2em;" width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#CCFFCC" align="center">
 <tbody><tr>
  <td>
  <table width="100%" border="0">
   <tbody><tr>
	<td><font size="+1"><b>スレッド・レスの通報フォーム</b></font></td>
	<td align="right"><a href="#menu">■</a> <a href="#1">▼</a></td>
   </tr>
   <tr>
	<td colspan="2">
	<div align="center" style="margin: 1.2em 0;">
		<p>スレッドや、レスの通報をしたい場合は、下のフォームを使って通報をお願いします。</p><br>
		<p>理由一覧：<br>
		・ローカルルール違反 <br>
		・スレッド・板の趣旨に無関係な投稿 <br>
		・マルチポスト・スパム・埋め立てなどの荒らし行為全般 <br>
		・人種差別・性差別など差別全般 <br>
		・故意にサーバーに負荷をかける行為 <br>
		・アフィサイトへの転載や、ロンダリング目的の投稿 <br>
		・特定の人物・団体・サイトへの過度な嫌がらせ・誹謗中傷 <br>
		・許可なく自動投稿プログラムを使用する行為 <br>
		・デマを流す行為 <br>
		・自作自演行為 <br>
		・グロ画像など人を不快にするコンテンツの投稿 <br>
		・ブラクラ・マルウェアなど有害なプログラムの投稿 <br>
		・ステルスマーケティング行為 <br>
		・麻薬取引 <br>
		・児童ポルノの投稿 <br>
		・テロ予告や、方法・日時・場所などを指定した具体的な殺害予告 </p>
	</td>
   </tr>
   <form method="POST" action="/test/bbs.cgi">
<table style="margin-bottom:1.2em;" width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#CCFFCC" align="center">
 <tbody><tr>
  <td nowrap="">
  <b>この内容で通報しますか？</b><br>
  <input type="submit" value="通報する"><br>
  <textarea name="MESSAGE" id="content" rows="5" cols="70" readonly></textarea>
<script>
let textarea = document.getElementById('content');
textarea.value = 'スレッドのURL：<?=$_POST["url"]?>\n理由：<?=$reasons[$_POST["reason"]]?>\n備考：<?=$_POST["bikou"]?>';
</script>
<br>
	<input type="hidden" name="FROM" value="Report form">
	<input type="hidden" name="time" value="<?=time();?>">
	<input type="hidden" name="bbs" value="lab">
	<input type="hidden" name="key" value="1697802449">
  </td>
 </tr>
</tbody></table>
</form>
  </tbody></table>
  </td>
 </tr>
</tbody></table>

<a name="ad"></a>
<table width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#ccffcc" align="center">
<tbody><tr><td>
<!-- FC2カウンター ここから -->
<script language="javascript" type="text/javascript" src="//counter1.fc2.com/counter.php?id=89505170"></script><noscript><img src="//counter1.fc2.com/counter_img.php?id=89505170" /></noscript>
<!-- FC2カウンター ここまで -->
<br>
<!-- FC2カウンター ここから -->
現在の閲覧者数:<script language="javascript" type="text/javascript" src="//counter1.fc2.com/views.php?id=89505170"></script><script src="https://counter1.fc2.com/views_js.php?id=89505170&amp;main=0&amp;lang=0" charset="UTF-8"></script><noscript><img src="//counter1.fc2.com/counter_now.php?id=89505170" /></noscript>
<!-- FC2カウンター ここまで -->
</td></tr>
</tbody></table>
</body></html>
<?php
	}
?>
