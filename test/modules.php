<?php
	function generateHTML($bbs){
		$settings = parse_ini_file('../'.$bbs.'/SETTING.TXT',false,INI_SCANNER_RAW);
		$head = file_get_contents("../$bbs/head.txt");
		$sns_desc = preg_replace("/<(.*)>/", "", $head);
		$sns_desc = preg_replace("/\r\n|\n|\r/", "", $sns_desc);
		$foot = file_get_contents("../$bbs/foot.txt");
		$subject = file("../$bbs/subject.txt");
		$count = 0;
		foreach ($subject as $subj){
			$count++;
			$subj = preg_replace("/(.*).dat<>(.*)\n/", "<a href=\"/test/read.cgi/$bbs/$1/l50\">$count:</a><a href=\"#$count\"> $2</a>", $subj);
			$subje = "$subje\n$subj";
			if ($count >= intval($settings["BBS_THREAD_NUMBER"])){
				break;
			}
		}
	
		$count2 = 0;
		foreach ($subject as $subjt){
			$count2++;
			if ($count2 > $count){
				$count++;
				$subjt = preg_replace("/(.*).dat<>(.*)\n/", "<a href=\"/test/read.cgi/$bbs/$1/l50\">$count: $2</a>", $subjt);
				$subje = "$subje\n$subjt";
			}
			if ($count == intval($settings["BBS_MAX_MENU_THREAD"])){
				break;
			}
		}

		foreach ($subject as $subjt){
			$subjt = preg_replace("/(.*).dat<>(.*)\n/", "<a href=\"/test/read.cgi/$bbs/$1/l50\">$count: $2</a>", $subjt);
			$subjetttt = "$subjetttt\n$subjt";
		}
	
		$count = 0;
		$max = 0;
		foreach ($subject as $subj){
			$count++;
			$threadvn = "";
			preg_match("/(.*).dat<>(.*)\(.*\)\n/",$subj, $kagi);
			$kagi[2] = str_replace("&", "&amp;",$kagi[2]);
			$kagi[2] = htmlspecialchars_decode($kagi[2]);
			$sure = file("../$bbs/dat/$kagi[1].dat");
			$suren = file_get_contents("../$bbs/dat/$kagi[1].dat");
			$max = count($sure);
	
			$countt = 0;
			if ($max <= 10){
				foreach ($sure as $surenn){
					$countt++;
					$LOG2 = trim($surenn);
					$LOG2 = str_replace("&", "&amp;",$LOG2);
					$LOG2 = htmlspecialchars_decode($LOG2);
					list($name,$mail,$time,$message,$subject) = explode("<>",$LOG2);
					$message = preg_replace_callback("/(https?):\/\/([\w;\/\?:\@&=\+\$,\-\.!~\*'\(\)%#]+)/i", function ($matches)
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
							return '<small><a href=\"//jump.14chan.cf/'.$matches[0].'">'.$matches[0].'</a></small> <br> <blockquote class="twitter-tweet"><a href="'.$match[0].'"></a> </blockquote>';
						}else if ($filetype == "jpg" || $filetype == "jpeg" || $filetype == "gif" || $filetype == "png" || $filetype == "apng" || $filetype == "svg" || $filetype == "ico" || $filetype == "webp"){
							return "<small><a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\">".$matches[1]."://".$matches[2]."</a></small> <br> <a href=\"".$matches[1]."://".$matches[2]."\" data-lightbox=\"group\"><img src=\"".$matches[1]."://".$matches[2]."\" style=\"width: 30%; height:30%;\"></img></a>";
						}else if($filetype == "mp4" || $filetype == "avi" || $filetype == "webm" || $filetype == "mov" || $filetype == "mkv"){
							return "<small><a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\">".$matches[1]."://".$matches[2]."</a></small> <br> <video controls width=\"30%\" height=\"30%\" src=\"".$matches[1]."://".$matches[2]."\"></video>";
						}else{
							return "<a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\" target=\"_blank\">".$matches[1]."://".$matches[2]."</a>";
						}
					}, $message);
					$message = preg_replace("/&gt;&gt;(\d+)/", "<a href=\"/test/read.cgi/$bbs/".$kagi[1]."/$1\">&gt;&gt;$1</a>", $message);
					$mailto = $mail ? "<a href=\"mailto:$mail\"><span style=\"color: ".$settings["BBS_NAME_COLOR"].";\"><b>$name</b></span></a>" : "<span style=\"color: ".$settings["BBS_NAME_COLOR"].";\"><b>$name</b></span>";
					$threadvn = "$threadvn\n"."<dt>$countt ：$mailto ： $time</dt><dd> $message <br><br></dd>\n";
					if ($countt == $max){
						break;
					}
				}
			}else{
				foreach ($sure as $surenn){
					$countt++;
					$LOG2 = trim($surenn);
					$LOG2 = str_replace("&", "&amp;",$LOG2);
					$LOG2 = htmlspecialchars_decode($LOG2);
					list($name,$mail,$time,$message,$subject) = explode("<>",$LOG2);
					$message = preg_replace_callback("/(https?):\/\/([\w;\/\?:\@&=\+\$,\-\.!~\*'\(\)%#]+)/i", function ($matches)
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
							return '<small><a href=\"//jump.14chan.cf/'.$matches[0].'">'.$matches[0].'</a></small> <br> <blockquote class="twitter-tweet"><a href="'.$match[0].'"></a> </blockquote>';
						}else if ($filetype == "jpg" || $filetype == "jpeg" || $filetype == "gif" || $filetype == "png" || $filetype == "apng" || $filetype == "svg" || $filetype == "ico" || $filetype == "webp"){
							return "<small><a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\">".$matches[1]."://".$matches[2]."</a></small> <br> <a href=\"".$matches[1]."://".$matches[2]."\" data-lightbox=\"group\"><img src=\"".$matches[1]."://".$matches[2]."\" style=\"width: 30%; height:30%;\"></img></a>";
						}else if($filetype == "mp4" || $filetype == "avi" || $filetype == "webm" || $filetype == "mov" || $filetype == "mkv"){
							return "<small><a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\">".$matches[1]."://".$matches[2]."</a></small> <br> <video controls width=\"30%\" height=\"30%\" src=\"".$matches[1]."://".$matches[2]."\"></video>";
						}else{
							return "<a href=\"//jump.14chan.cf/".$matches[1]."://".$matches[2]."\" target=\"_blank\">".$matches[1]."://".$matches[2]."</a>";
						}
					}, $message);
					$message = preg_replace("/&gt;&gt;(\d+)/", "<a href=\"/test/read.cgi/$bbs/".$kagi[1]."/$1\">&gt;&gt;$1</a>", $message);
					$mailto = $mail ? "<a href=\"mailto:$mail\"><span style=\"color: ".$settings["BBS_NAME_COLOR"].";\"><b>$name</b></span></a>" : "<span style=\"color: ".$settings["BBS_NAME_COLOR"].";\"><b>$name</b></span>";
					if ($countt == 1 || $countt >= $max-9){
						$threadvn = "$threadvn\n"."<dt>$countt ：$mailto ： $time</dt><dd style=\"overflow-wrap: break-word\"> $message <br><br></dd>\n";
					}
	
					if ($countt == $max){
						break;
					}
				}
			}
	
			$threadv = $threadv."\n".'<table style="table-layout: fixed; margin-bottom:1.2em;" width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#EFEFEF" align="center">
			<tbody><tr>
				<td>
				<a name="'.$count.'"></a>
				<div align="right"><a href="#menu">■</a><a href="#'.($count-1).'">▲</a><a href="#'.($count+1).'">▼</a></div>
				<div style="font-weight:bold;margin-bottom:0.2em;">【'.$count.':'.$max.'】<font size="+2" color="#FF0000">'.$kagi[2].'</font></div>
				<dl style="margin-top:0px;">
				'.$threadvn.'
				</dl>
				<form method="POST" action="/test/bbs.cgi">
				<blockquote>
				<input type="hidden" name="bbs" value="'.$bbs.'">
				<input type="hidden" name="key" value="'.$kagi[1].'">
				<input type="hidden" name="time" value="'.time().'">
				<input type="submit" value="書き込む" name="submit"> 
				名前：<input type="text" name="FROM" size="19">
				E-mail：<input type="text" name="mail" size="19"><br>
				<blockquote style="margin-top:0px;">
				<textarea rows="5" cols="64" name="MESSAGE"></textarea>
				<div style="font-weight:bold;">
				<a href="/test/read.cgi/'.$bbs.'/'.$kagi[1].'/">全部読む</a>
				<a href="/test/read.cgi/'.$bbs.'/'.$kagi[1].'/l50">最新50</a>
				<a href="/test/read.cgi/'.$bbs.'/'.$kagi[1].'/1-100">1-100</a>
				<a href="#top">板のトップ</a>
				<a href="./">リロード</a>
				</div>
				</blockquote>
				</blockquote>
				</form>
				</td>
			</tr>
			</tbody></table>';
	
			if ($count == intval($settings["BBS_THREAD_NUMBER"])){
				break;
			}
		}
		$count = 0;
		$index='<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
			<head>
	 
	 <meta http-equiv="Content-Type" content="text/html;charset=Shift-JIS">
	 <meta http-equiv="Content-Script-Type" content="text/javascript">
	 
	
	 <title>'.$settings["BBS_TITLE"].' - 14Channel BBS</title>
	
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
	<meta name="twitter:card" content="summary_large_image" />
	<meta property="og:image" content="'.$settings["BBS_TITLE_PICTURE"].'" />
	<meta property="og:title" content="14Channel BBS - '.$settings["BBS_TITLE"].'" />
	<meta property="og:description" content="'.$sns_desc.'"/>
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
		<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4330360014245167"
		 crossorigin="anonymous"></script>
		 <link href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.7.1/css/lightbox.css" rel="stylesheet">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.7.1/js/lightbox.min.js" type="text/javascript"></script>
	<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
	</head>
	<!--nobanner-->
	<body vlink="'.$settings["BBS_VLINK_COLOR"].'" text="'.$settings["BBS_TEXT_COLOR"].'" link="'.$settings["BBS_LINK_COLOR"].'" bgcolor="'.$settings["BBS_BG_COLOR"].'" background="'.$settings["BBS_BG_PICTURE"].'" alink="'.$settings["BBS_ALINK_COLOR"].'">
	<!-- [FC2 Analyzer] //analyzer.fc2.com/  -->
	<script language="javascript" src="//analyzer54.fc2.com/ana/processor.php?uid=2894165" type="text/javascript"></script>
	<noscript><div align="right"><img src="//analyzer54.fc2.com/ana/icon.php?uid=2894165&ref=&href=&wid=0&hei=0&col=0" /></div></noscript>
	<!-- [FC2 Analyzer]  -->
	<a name="top"></a>
	<div align="center"><a href="//"><img src="'.$settings["BBS_TITLE_PICTURE"].'" alt="14Channel BBS" border="0"></a></div>
	<a name="info"></a>
	<table style="margin-bottom:1.2em;" width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#CCFFCC" align="center">
	 <tbody><tr>
	  <td>
	  <table width="100%" border="0">
	   <tbody><tr>
		<td><font size="+1"><b>'.$settings["BBS_SUBTITLE"].'</b></font></td>
		<td align="right"><a href="#menu">■</a> <a href="#1">▼</a></td>
	   </tr>
	   <tr>
		<td colspan="2">
		'.$head.'
		</td>
	   </tr>
	  </tbody></table>
	  </td>
	 </tr>
	 <tr>
	  <td align="center"><a href="/" target="_blank"><small>■<b>掲示板一覧</b>■</small></a></td>
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
	現在の閲覧者数:<script language="javascript" type="text/javascript" src="//counter1.fc2.com/views.php?id=89505170"></script><noscript><img src="//counter1.fc2.com/counter_now.php?id=89505170" /></noscript>
	<!-- FC2カウンター ここまで -->
	</td></tr>
	</tbody></table>
	
	<a name="menu"></a>
	<table style="margin:1.2em auto;" width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#CCFFCC" align="center">
	 <tbody><tr>
	  <td>
	  <small>
	  '.$subje.'
	  </small>
	  <div align="right"><small><b><a href="./subback.html">スレッド一覧はこちら</a></b></small></div>
	  </td>
	 </tr>
	</tbody></table>
	
	'.$threadv.'
	
	<form method="POST" action="/test/bbs.cgi">
	<table style="margin-bottom:1.2em;" width="95%" cellspacing="7" cellpadding="3" border="1" bgcolor="#CCFFCC" align="center">
	 <tbody><tr>
	  <td nowrap="">
	  <b>新規'.mb_str_shuffle("スレッド").'作成</b><br>
	  <input placeholder="スレタイ" type="text" name="subject" size="40"><input type="submit" value="新規スレッド作成"><br>
	  名前：<input placeholder="なまえ#とりっぷ" type="text" name="FROM" size="19"> <input placeholder="めーる#きゃっぷ" type="text" name="mail" size="19"><br>
	  <textarea rows="5" cols="60" name="MESSAGE"></textarea>
	  <input type="hidden" name="bbs" value="'.$bbs.'">
	  <input type="hidden" name="time" value="'.time().'">
	  </td>
	 </tr>
	</tbody></table>
	</form>
	'.$foot.'
	<b>
	<p style="margin: 0; padding: 0.25em 0; text-align: center; color: #333;">
	<a href="//14chan.cf/">14Channel BBS</a> BBS.CGI - '.date("Y/m/d H:i:s",filemtime("bbs.cgi")).' JST<br>
	<a href="./SETTING.TXT">SETTING.TXT</a></p>
	<p style="margin: 0 0 0.5em 0; text-align: center; font-size: 0.8em; color: #933;">
	Server By <!--<a href="https://osdn.net/"><img src="//osdn.net/sflogo.php?group_id=14874&amp;type=1" width="96" height="29" border="0" alt="OSDN"></a>-->OSDN. Thanks!!<br>
	last modified at '.date("Y/m/d H:i:s").' JST
	</p>
	</b>
	
	
	</body>';
		file_put_contents("../$bbs/index.html",$index,LOCK_EX);
	
		$subback = '<html><head><title>'.$settings["BBS_TITLE"].' - 14Channel BBS</title></head><body><small>'.$subjetttt.'</small><p style="margin: 0 0 0.5em 0; text-align: right; font-size: 0.8em; color: #933;">last modified at '.date("Y/m/d H:i:s").' JST</p></body></html>';
		file_put_contents("../$bbs/subback.html",$subback,LOCK_EX);
	}

	/**
	 * 日本語対応 str_shuffle
	 * @param  string  $str  並び替え対象文字列
	 * @return string 並び替え結果文字列
	 */
	function mb_str_shuffle($str)
	{
		$arr = mb_str_split($str,1,"Shift-JIS");
		openssl_shuffle($arr);
		return implode("", $arr);
	}

	function mb_str_split($string, $split_length = 1, $encoding = null) {
		if ($split_length < 1) {
			return false;
		}
		if (func_num_args() < 3) {
			$encoding = mb_internal_encoding();
		}
		$ret = array();
		$len = mb_strlen($string, $encoding);
		for ($i = 0; $i < $len; $i += $split_length) {
			$ret[] = mb_substr($string, $i, $split_length, $encoding);
		}
		if (!$ret) {
			$ret[] = '';
		}
		return $ret;
	}

	function mt_shuffle(array &$array) {
		$array = array_values($array);
		for ($i = count($array) - 1; $i > 0; --$i) {
			$j = mt_rand(0, $i);
			$tmp = $array[$i];
			$array[$i] = $array[$j];
			$array[$j] = $tmp;
		}
	}

	function openssl_rand($min = 0, $max = PHP_INT_MAX) {
		$min = (int)$min;
		$max = (int)$max;
		$range = $max - $min;
		if ($range <= 0) {
			return $min;
		}
		$log    = log($range, 2);
		$bytes  = (int)($log / 8) + 1;
		$bits   = (int)$log + 1;
		$filter = (int)(1 << $bits) - 1;
		do {
			$rand = hexdec(bin2hex(openssl_random_pseudo_bytes($bytes))) & $filter;
		} while ($rand > $range);
		return $min + $rand;
	}

	function openssl_shuffle(array &$array) {
		$array = array_values($array);
		for ($i = count($array) - 1; $i > 0; --$i) {
			$j = openssl_rand(0, $i);
			$tmp = $array[$i];
			$array[$i] = $array[$j];
			$array[$j] = $tmp;
		}
	}

	function sendwebhook($bbs,$key,$from,$content,$subject,$url,$count){
		$POST_DATA = array(
			'bbs' => $bbs,
			'key' => $key,
			'from' => strip_tags(mb_convert_encoding($from,"UTF-8","Shift-JIS")),
			"content" => strip_tags(mb_convert_encoding($content,"UTF-8","Shift-JIS")),
			'subject' => mb_convert_encoding($subject,"UTF-8","Shift-JIS"),
			'url' => $url
		);
		$curl=curl_init("https://script.google.com/macros/s/AKfycbwX-8_eNB2OJDFL-H5cuXMJuxxcQQtudFLRXf3N1FmlkM-yl_1OsuKBglDZymRSxyoCgQ/exec");
		curl_setopt($curl,CURLOPT_POST, TRUE);
		// ↓はmultipartリクエストを許可していないサーバの場合はダメっぽいです
		// @DrunkenDad_KOBAさん、Thanks
		//curl_setopt($curl,CURLOPT_POSTFIELDS, $POST_DATA);
		curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($POST_DATA));
		curl_setopt($curl,CURLOPT_SSL_VERIFYPEER, FALSE);  // オレオレ証明書対策
		curl_setopt($curl,CURLOPT_SSL_VERIFYHOST, FALSE);  // 
		curl_setopt($curl,CURLOPT_RETURNTRANSFER, TRUE);
		curl_setopt($curl,CURLOPT_COOKIEJAR,      'cookie');
		curl_setopt($curl,CURLOPT_COOKIEFILE,     'tmp');
		curl_setopt($curl,CURLOPT_FOLLOWLOCATION, TRUE); // Locationヘッダを追跡
		curl_setopt($curl, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);
		//curl_setopt($curl,CURLOPT_REFERER,        "REFERER");
		//curl_setopt($curl,CURLOPT_USERAGENT,      "USER_AGENT"); 
		
		$response = curl_exec( $curl );
		$info = curl_getinfo($curl);

		$errno = curl_errno($curl);
		$error = curl_error($curl);

		curl_close( $curl );
		return [$response,$info,$error,$errno];
	}
?>