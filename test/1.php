<?php
/*
	スレッドリーダー 「read.cgi」(中身はPHP)
*/
	//設定
	//ini_set('display_errors',1);
	date_default_timezone_set('Asia/Tokyo');
	//設定 END
	$pathinfo = $_SERVER['REQUEST_URI'];
	$pathinfo = preg_replace("/\?.*/", "", $pathinfo);
	$pathinfo = explode('/',$pathinfo);
	//array(4) { [0]=> string(0) "" [1]=> string(5) "admin" [2]=> string(10) "2000000000" [3]=> string(0) "" } 
	$bbs = $pathinfo[3];
	$key = $pathinfo[4];
	$mode = $pathinfo[5];
	$cookName = $_COOKIE["cookName"];
	$cookMail = $_COOKIE["cookMail"];
	$ver = '<b>
	<p style="margin: 0; padding: 0.25em 0; text-align: center; color: #333;">
	<a href="//14chan.cf/">14Channel BBS</a> READ.CGIv1 - '.date("Y/m/d H:i:s", filemtime("./1.php")).' JST <b>未完成</b><br>
	<a href="/'.$bbs.'/SETTING.TXT">SETTING.TXT</a></p>
	<p style="margin: 0 0 0.5em 0; text-align: center; font-size: 0.8em; color: #933;">
	Server By <!--<a href="https://osdn.net/"><img src="//osdn.net/sflogo.php?group_id=14874&amp;type=1" width="96" height="29" border="0" alt="OSDN"></a>-->OSDN. Thanks!!<br>
	</p>
	</b>';

	if (file_exists("../$bbs/SETTING.TXT") == false){
		header("HTTP/1.1 404 Not Found");
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<head>

 <meta http-equiv="Content-Type" content="text/html;charset=Shift_JIS">
 <meta http-equiv="Content-Style-Type" content="text/css">


 <title>指定された板は存在しません</title>
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
	<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4330360014245167"
	 crossorigin="anonymous"></script>
</head>
<!--nobanner-->
<body vlink="#AA0088" text="#000000" link="#0000FF" bgcolor="#EFEFEF" alink="#FF0000">
<table width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#ccffcc" align="center">
<tbody><tr><td>
<!-- FC2カウンター ここから -->
<script language="javascript" type="text/javascript" src="//counter1.fc2.com/counter.php?id=89505170"></script><noscript><img src="//counter1.fc2.com/counter_img.php?id=89505170" /></noscript>
<!-- FC2カウンター ここまで -->
<br>
<!-- FC2カウンター ここから -->
現在の閲覧者数:<script language="javascript" type="text/javascript" src="//counter1.fc2.com/views.php?id=89505170"></script><noscript><img src="//counter1.fc2.com/counter_now.php?id=89505170" /></noscript>
<!-- FC2カウンター ここまで -->
<!-- [FC2 Analyzer] //analyzer.fc2.com/  -->
<script language="javascript" src="//analyzer54.fc2.com/ana/processor.php?uid=2894165" type="text/javascript"></script>
<noscript><div align="right"><img src="//analyzer54.fc2.com/ana/icon.php?uid=2894165&ref=&href=&wid=0&hei=0&col=0" /></div></noscript>
<!-- [FC2 Analyzer]  -->
</td></tr>
</tbody></table>
<hr>
<div style="margin:0px;">
	<div style="margin-top:1em;">
	<span style="float:left;">
		<a href="/">■鯖TOPに戻る■</a>
	</span>
	<span style="float:right;">
		[PR]<a href="https://discord.gg/BtNdCYStxn" target="_blank">公式discord鯖</a>[PR]
		&nbsp;
</span>&nbsp;
	</div>
	</div>
<hr style="background-color:#888;color:#888;border-width:0;height:1px;position:relative;top:-.4em;">

<h1 style="color:red;font-size:larger;font-weight:normal;margin:-.5em 0 0;">指定された板は存在しません</h1>


<dl class="thread">
 <dt>1 ：<font color="green"><b>名無しさん＠14ちゃんねる</b></font>：2022/6/28(火) 00:00:00 ID:NoThread</dt>
  <dd>あなたが指定された板は存在していません。<br>削除されたかURLを間違っていますよ…。<br><br></dd>
 <dt>2 ：<font color="green"><b>名無しさん＠14ちゃんねる</b></font>：2022/6/28(火) 00:00:00 ID:NoThread</dt>
  <dd>14ちゃんねるは<a href="//www.nennneko5787.ml/">nennneko5787</a>が自作したスクリプトで動いています。<br><br></dd>
</dl>

<hr>

<div style="margin-top:4em;">
<?=$ver?>
</div>



</body>
<?php
	exit();
	}
	$settings = parse_ini_file('../'.$bbs.'/SETTING.TXT',false,INI_SCANNER_RAW);
	if ($settings["BBS_RES_MAX"] == ""){
		$settings["BBS_RES_MAX"] = 1000;
	}
	if (file_exists("../$bbs/dat/$key.dat") == false){
		$nodat = true;
		header("HTTP/1.1 404 Not Found");
	}

	$setting = file_get_contents("../$bbs/SETTING.TXT");

	if ($nodat == true){
		$dat = file("../$bbs/2000000000.dat");
	}else{
		$dat = file("../$bbs/dat/$key.dat");
	}
	$max = count($dat);

	$oneh = file_get_contents("../$bbs/1000.txt");
	if(strpos($dat[$max],$oneh) !== false){
		$stop = 1;
	}

	list(,,,,$subject) = explode("<>",$dat[0]);
	$subject = trim($subject);
	if (!isset($subject)||$subject == ""){
		$subject = '[ここ壊れてます]';
	}

	$datSize = floor(filesize("../$bbs/dat/$key.dat") / 1024);

	if (preg_match("/^l(.*)$/", $mode, $lasth)){
		$lasth = $lasth[1];
		$lastmode = true;
	}

	if (preg_match("/^(.*)\-$/", $mode, $ko_)){
		$ko__mode = true;
	}

	if (preg_match("/^(.*)\-(.*)$/", $mode, $ko_ko)){
		$ko_ko_mode = true;
	}

	if (preg_match("/^\-(.*)$/", $mode, $_ko)){
		$_ko_mode = true;
	}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=Shift-JIS">
<meta http-equiv="Content-Style-Type" content="text/css">

<title><?=$subject?> - 14Channel BBS</title>
<script language="JavaScript" type="text/javascript">
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
	var ptrn = \'(?:^|;| )\' + key + \'="(.*?)"\';
	if (document.cookie.match(ptrn))
		return decodeURIComponent(RegExp.$1);
	return "";
}
//-->
</script>

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
	<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4330360014245167"
	 crossorigin="anonymous"></script>

	 <link href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.7.1/css/lightbox.css" rel="stylesheet">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.7.1/js/lightbox.min.js" type="text/javascript"></script>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<script src="/test/TtsQuestV3Voicevox.js"></script>
<script>
	function ttsThread(text,speaker,token){
		<?php
			if (!isset($_COOKIE["software"]) || $_COOKIE["software"] == ""){
				echo '		const uttr = new SpeechSynthesisUtterance(text);
				uttr.lang = \'ja-JP\';
				speechSynthesis.speak(uttr);
				return true;';
			}else{
				echo '		var tts = new TtsQuestV3Voicevox(speaker, text, token);
				tts.play()';
			}
		?>
	}
</script>
<?php
		if (isset($_GET["sp"])) {
			echo '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">';
			echo '<style>
					body{ background-color: #EFEFEF; color: #000000; padding-left: 0.3em;}
				   a:link { color: #0000FF ; }
			　　　 a:visited { color: #AA0088 ; }
			　　　 a:hover { color: #FFFFFF ;}
			　　　 a:active { color: #FF0000 ; }
					dd {padding-left: 1em;}
					</style>';
		}
?>
</head>

<?php
	if (isset($_GET["sp"])) {
		echo '<body>';
	}else{
		echo '<body vlink="#AA0088" text="#000000" link="#0000FF" bgcolor="#EFEFEF" alink="#FF0000">';
	}
?>
<body vlink="<?=$settings["BBS_VLINK_COLOR"]?>" text="<?=$settings["BBS_TEXT_COLOR"]?>" link="<?=$settings["BBS_LINK_COLOR"]?>" bgcolor="<?=$settings["BBS_BG_COLOR"]?>" alink="<?=$settings["BBS_ALINK_COLOR"]?>">
<!-- [FC2 Analyzer] //analyzer.fc2.com/  -->
<script language="javascript" src="//analyzer54.fc2.com/ana/processor.php?uid=2894165" type="text/javascript"></script>
<noscript><div align="right"><img src="//analyzer54.fc2.com/ana/icon.php?uid=2894165&ref=&href=&wid=0&hei=0&col=0" /></div></noscript>
<!-- [FC2 Analyzer]  -->
<table width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#ccffcc" align="center">
<tbody><tr><td>
<!-- FC2カウンター ここから -->
<script language="javascript" type="text/javascript" src="//counter1.fc2.com/counter.php?id=89505170"></script><noscript><img src="//counter1.fc2.com/counter_img.php?id=89505170" /></noscript>
<!-- FC2カウンター ここまで -->
<br>
<!-- FC2カウンター ここから -->
現在の閲覧者数:<script language="javascript" type="text/javascript" src="//counter1.fc2.com/views.php?id=89505170"></script><noscript><img src="//counter1.fc2.com/counter_now.php?id=89505170" /></noscript>
<!-- FC2カウンター ここまで -->
</td></tr>
</tbody></table>
<hr>
<div style="margin:0px;">
<div style="margin-top:1em;">
<span style="float:left;">
<a href="/<?=$bbs?>/">■掲示板に戻る■</a>
<a href="//<?=$_SERVER['SERVER_NAME']?>/test/read.cgi/<?=$bbs?>/<?=$key?>/">全部</a>
<a href="//<?=$_SERVER['SERVER_NAME']?>/test/read.cgi/<?=$bbs?>/<?=$key?>/1-100">1-</a>
<a href="//<?=$_SERVER['SERVER_NAME']?>/test/read.cgi/<?=$bbs?>/<?=$key?>/101-200">101-</a>
<a href="//<?=$_SERVER['SERVER_NAME']?>/test/read.cgi/<?=$bbs?>/<?=$key?>/l50">最新50</a>
<a href="//<?=$_SERVER['SERVER_NAME']?>/test/setting.cgi?bbs=<?=$bbs?>">設定</a>
</span>
<span style="float:right;">
[PR]<a href="https://discord.gg/BtNdCYStxn" target="_blank">公式discord鯖</a>[PR]
</span>&nbsp;
</div>
</div>
<hr style="background-color:#888;color:#888;border-width:0;height:1px;position:relative;top:-.4em;">
<h1 style="color:#FF0000;font-size:larger;font-weight:normal;margin:-.5em 0 0;"><?=$subject?></h1>
<small style="font-weight:normal;margin:-.5em 0 0;">(全部で<?=$max?>のレスがあります)</small>
<dl class="thread">
<!--スレッドの中身挿入-->
<?php
foreach ($dat as $s){
	$count++;
	$LOG2 = trim($s);
	$LOG2 = str_replace("&", "&amp;",$LOG2);
	$LOG2 = htmlspecialchars_decode($LOG2);
	list($name,$mail,$time,$message,$subject) = explode("<>",$LOG2);
	$message = preg_replace_callback("/(https?):\/\/([\w;\/\?:\@&=\+\$,\-\.!~\*'\(\)%#]+)()/i", function ($matches)
	{
		// 通常は、$matches[0] がマッチした全体を表します。
		// $matches[1] は、マッチした中で、パターン内の最初の '(...)'
		// にあてはまる部分を表します。それ以降も同様です。
		$file = pathinfo($matches[1]."://".$matches[2]);
		$filetype = $file['extension'];
		//まず大前提！youtubeの動画のリンクは！変換しない！
		if (preg_match("/^(https?:\/\/)?(www\.youtube\.com\/watch\?v=|youtu.be\/)(.*)/i",$matches[1]."://".$matches[2],$match)){
			//return $matches[1]."://".$matches[2];
			return "<small><a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\">".$matches[1]."://".$matches[2]."</a></small> <br> <iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/".$match[3]."\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>";
		}else if (preg_match("/^(https?:\/\/)?(www\.nicovideo\.jp\/watch\/|nico.ms\/)(.*)/i",$matches[1]."://".$matches[2],$match)){
			return "<small><a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\">".$matches[1]."://".$matches[2]."</a></small> <br> <script type=\"application/javascript\" src=\"https://embed.nicovideo.jp/watch/".preg_replace("/\?.*/", "", $match[3])."/script?w=320&h=180\"></script>";
		}else if (preg_match("/https?:\/\/(twitter\.com|x\.com)\/(?<name>[^\?]+)\??.*/",$matches[1]."://".$matches[2],$match)){
			return '<small><a href=\"//jump.14chan.cf/'.$matches[0].'">'.$matches[0].'</a></small> <br> <blockquote class="twitter-tweet">
			<a href="'.$match[0].'"></a> 
		  </blockquote>';
		}else if ($filetype == "jpg" || $filetype == "jpeg" || $filetype == "gif" || $filetype == "png" || $filetype == "apng" || $filetype == "svg" || $filetype == "ico" || $filetype == "webp"){
			return "<small><a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\">".$matches[1]."://".$matches[2]."</a></small> <br> <a href=\"".$matches[1]."://".$matches[2]."\" data-lightbox=\"group\"><img src=\"".$matches[1]."://".$matches[2]."\" style=\"width: 30%; height:30%;\"></img></a>";
		}else if($filetype == "mp4" || $filetype == "avi" || $filetype == "webm" || $filetype == "mov" || $filetype == "mkv"){
			return "<small><a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\">".$matches[1]."://".$matches[2]."</a></small> <br> <video controls width=\"30%\" height=\"30%\" src=\"".$matches[1]."://".$matches[2]."\"></video>";
		}else{
			return "<a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\" target=\"_blank\">".$matches[1]."://".$matches[2]."</a>";
		}
	}, $message);
	//$message = preg_replace("/(https?)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)\.(jpg|jpeg|gif|png)/i", "<small><a href=\"$1$2.$3\">$1$2.$3</a></small> <br> <a href=\"$1$2.$3\" data-lightbox=\"group\"><img src=\"$1$2.$3\" style=\"width: 30%; height:30%;\"></img></a>", $message);
	//$message = preg_replace("/(https?)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)\.(mp4|avi|webm)/i", "<small><a href=\"$1$2.$3\">$1$2.$3</a></small> <br> <video controls width=\"30%\" height=\"30%\" src=\"$1$2.$3\"></video>", $message);
	$message = preg_replace("/&gt;&gt;(\d+)/", "<a href=\"$1\">&gt;&gt;$1</a>", $message);
	$mailto = $mail ? "<a href=\"mailto:$mail\"><span style=\"color: ".$settings["BBS_NAME_COLOR"].";\"><b>$name</b></span></a>" : "<span style=\"color: ".$settings["BBS_NAME_COLOR"].";\"><b>$name</b></span>";
	$time = "$time <button title=\"このレスを読み上げてもらう\" onclick=\"ttsThread('".htmlspecialchars(strip_tags(str_replace(" <br> ","、",$message)),ENT_NOQUOTES,"Shift_JIS",true)."',".$_COOKIE["character"].",'');\">&#x1f50a;</button><a href=\"/test/report.cgi?url=https://".$_SERVER["SERVER_NAME"]."/test/read.cgi/$bbs/$key/\" title=\"このレスを通報する\"><button>&#x1f4e2;</button></a>";
	if ($mode != ""){
		if ($lastmode){
			if (($count >= ($max - $lasth)) || $count == 1){
				echo "<dt>$count ：$mailto ： $time</dt><dd> $message <br><br></dd>\n";
			}
		}elseif ($ko_ko_mode || $ko__mode || $_ko_mode){
			if (($count >= intval($ko_ko[1]) && $count <= intval($ko_ko[2]) && $ko_ko_mode) || $count == 1){
				echo "<dt>$count ：$mailto ： $time</dt><dd> $message <br><br></dd>\n";
			}elseif (($count >= intval($ko_[1]) && $ko__mode) || $count == 1){
				echo "<dt>$count ：$mailto ： $time</dt><dd> $message <br><br></dd>\n";
			}elseif (($count <= intval($_ko[1]) && $_ko_mode) || $count == 1){
				echo "<dt>$count ：$mailto ： $time</dt><dd> $message <br><br></dd>\n";
			}
		}else{
			if ($count == $mode || $count == 1){
				echo "<dt>$count ：$mailto ： $time</dt><dd> $message <br><br></dd>\n";
			}
		}
	}else{
		echo "<dt>$count ：$mailto ： $time</dt><dd> $message <br><br></dd>\n";
	}
	if ($count == $max){
		break;
	}
}

$time_ikioi = time() - intval($key);
$minute_ikioi = ($time_ikioi - ($time_ikioi % 60)) / 60;
$ikioi = $max/$minute_ikioi*60*24;
?>
</dl>
<font face="Arial" color="red"><b><?=$datSize?>KB</b></font>
<hr>
<center><a href="//<?=$_SERVER['SERVER_NAME']?>/test/read.cgi/<?=$bbs?>/<?=$key?>/<?=$max?>-">新着レスの表示</a>｜勢い：<?=$ikioi;?></center>
<hr>
<?php
if ($nodat != true){
?>
<div class="links">
<a href="/<?=$bbs?>/">掲示板に戻る</a>
<a href="//<?=$_SERVER['SERVER_NAME']?>/test/read.cgi/<?=$bbs?>/<?=$key?>/">全部</a>
<a href="//<?=$_SERVER['SERVER_NAME']?>/test/read.cgi/<?=$bbs?>/<?=$key?>/1-100">1-</a>
<a href="//<?=$_SERVER['SERVER_NAME']?>/test/read.cgi/<?=$bbs?>/<?=$key?>/101-200">101-</a>
<a href="//<?=$_SERVER['SERVER_NAME']?>/test/read.cgi/<?=$bbs?>/<?=$key?>/l50">最新50</a>
</div>
<form method="POST" action="/test/bbs.cgi">
<input type="hidden" name="bbs" value="<?=$bbs?>"><input type="hidden" name="key" value="<?=$key?>"><input type="hidden" name="time" value="<?=time()?>">
<input type="submit" value="書き込む">
名前：<input type="text" name="FROM" value="<?=$cookName?>" size="19">
E-mail<font size="1">（省略可）</font>：<input type="text" name="mail" value="<?=$cookMail?>" size="19">
<br>
<textarea rows="5" cols="70" id="MESSAGE" name="MESSAGE"></textarea><br>
</form>
<br>
<form id="form_id"><span style="background-color: #CECECE; padding: 2px;">ファイルを選択：<input type="file" id="file" onchange="selectFile()"></span></form>
<div class="output hide"></div>
<div style="margin-top:4em;">
<?=$ver?>
</div>
<script src="/test/readv1.js"></script>
<?php
}
if (isset($_GET["sp"])) {
	echo '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>';
}
?>
</body>
</html>