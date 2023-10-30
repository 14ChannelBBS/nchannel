<?php
	ini_set("display_errors",false);
	$ms1 = microtime(true);
	require "modules.php";
	require "SysSettings.php";
	$iscap = false;
	$timeskip = false;
	$isadmin = false;
	$bbs = $_POST["bbs"];
	$key = $_POST["key"];
	$time = $_POST["time"];
	$from = $_POST["FROM"];
	$mail = $_POST["mail"];
	$content = $_POST["MESSAGE"];
	$subject = rtrim($_POST["subject"]);
	$issurenusi = false;
	$isthreadstopped = false;
	$client_id = $_COOKIE["client_id"]; //Client ID
	$isnewthread = false;
	if (strpos("{\"result\":{\"ipv4_cidrs\":[\"173.245.48.0/20\",\"103.21.244.0/22\",\"103.22.200.0/22\",\"103.31.4.0/22\",\"141.101.64.0/18\",\"108.162.192.0/18\",\"190.93.240.0/20\",\"188.114.96.0/20\",\"197.234.240.0/22\",\"198.41.128.0/17\",\"162.158.0.0/15\",\"104.16.0.0/13\",\"104.24.0.0/14\",\"172.64.0.0/13\",\"131.0.72.0/22\"],\"ipv6_cidrs\":[\"2400:cb00::/32\",\"2606:4700::/32\",\"2803:f800::/32\",\"2405:b500::/32\",\"2405:8100::/32\",\"2a06:98c0::/29\",\"2c0f:f248::/32\"],\"etag\":\"38f79d050aa027e3be3865e495dcc9bc\"},\"success\":true,\"errors\":[],\"messages\":[]}",$_SERVER["REMOTE_ADDR"]) !== false){
		$ipaddr = $_SERVER["REMOTE_ADDR"];
	}else{
		$ipaddr = $_SERVER['HTTP_CF_CONNECTING_IP'];
	}
	$host = gethostbyaddr($ipaddr);
	if (strpos($_SERVER['HTTP_USER_AGENT'],"Monazilla/1.00") !== false){
		$ismonazilla = true;
	}else{
		$ismonazilla = false;
	}
	if (!isset($_POST["subject"])) {
		if (!isset($_POST["key"])){
			PrintBBSError("フォーム情報が欠落しています！","もう一度書き込んでみてください！");
			exit();
		}
	}
	if (!isset($_POST["bbs"]) || !isset($_POST["MESSAGE"]) || $_POST["MESSAGE"] == "" || !isset($_POST["time"])){
		PrintBBSError("フォーム情報が欠落しています！","もう一度書き込んでみてください！");
		exit();
	}
	if (preg_match("/\D/", $key)){
		PrintBBSError("キー情報が不正です！","UNIX時間って知っていますか...?");
		exit();
	}
	if (isset($_POST["key"]) && $key != null && !file_exists('../'.$bbs.'/dat/'.$key.".dat")){
		PrintBBSError("そんなスレッド存在しません！","あれれ");
		exit();
	}
	if (!file_exists('../'.$bbs.'/SETTING.TXT')){
		PrintBBSError("ユーザー設定が消失しています！","あらら、バグで消えちゃったのかしら...");
		exit();
	}
	$settings = parse_ini_file('../'.$bbs.'/SETTING.TXT',false,INI_SCANNER_RAW);
	if ($settings["BBS_RES_MAX"] == ""){
		$settings["BBS_RES_MAX"] = 1000;
	}
	if (isset($_POST["cf-turnstile-response"])){
		//シークレット(将来いつ使うかは不明)
		$id = bin2hex(openssl_random_pseudo_bytes(8));
		//公開しても良いクライアントIDを生成
		$clientid = bin2hex(openssl_random_pseudo_bytes(16));

		$POST_DATA = array(
			'secret' => $turnstile_secret,
			'response' => $_POST["cf-turnstile-response"],
			//'response' => $_POST["h-captcha-response"],
			'remoteip' => $ipaddr
		);
		$curl=curl_init("https://challenges.cloudflare.com/turnstile/v0/siteverify");
		//$curl=curl_init("https://api.hcaptcha.com/siteverify");
		//curl_setopt($curl,CURLOPT_POST, TRUE);
		// ↓はmultipartリクエストを許可していないサーバの場合はダメっぽいです
		// @DrunkenDad_KOBAさん、Thanks
		curl_setopt($curl,CURLOPT_POSTFIELDS, $POST_DATA);
		curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($POST_DATA));
		curl_setopt($curl,CURLOPT_SSL_VERIFYPEER, FALSE);  // オレオレ証明書対策
		curl_setopt($curl,CURLOPT_SSL_VERIFYHOST, FALSE);  // 
		curl_setopt($curl,CURLOPT_RETURNTRANSFER, TRUE);
		curl_setopt($curl,CURLOPT_COOKIEJAR,	  'cookie');
		curl_setopt($curl,CURLOPT_COOKIEFILE,	 'tmp');
		curl_setopt($curl,CURLOPT_FOLLOWLOCATION, TRUE); // Locationヘッダを追跡
		//curl_setopt($curl,CURLOPT_REFERER,		"REFERER");
		//curl_setopt($curl,CURLOPT_USERAGENT,	  "USER_AGENT"); 
		curl_setopt($curl, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);	//IPv4だけを受け付ける
		curl_setopt($curl, CURLOPT_FORBID_REUSE, true);
		
		$json = curl_exec($curl);
		$output= json_decode($json,true);
		if ($output["success"] != true){
			setcookie("2ch_X", "", time()-60);
			PrintRobotCheckAndRules($settings,true);
			exit();
		}else{
			setcookie("2ch_X", $id, (time()+60*60*24*(365*10)));
			setcookie("client_id",$clientid,(time()+60*60*24*(365*10)));
			file_put_contents("../robotcheck_bypass.txt","$id<>$clientid\n",FILE_APPEND);
			chmod("../robotcheck_bypass.txt",0660);
			$checkrobot = true;
		}
	}else{
		$a = file_get_contents("../robotcheck_bypass.txt");
		if (false === strpos($a, $_COOKIE["2ch_X"]."\n")) {
			$a = file_put_contents("../robotcheck_bypass.txt",$_COOKIE["2ch_X"]."\n",FILE_APPEND);
		}
	}
	if (file_exists("../$bbs/dat/$key.dat")){
		chmod("../$bbs/dat/$key.dat",0664);
		chmod("../$bbs/log/$key.log",0664);
		//先に読み出しておく
		$dat = file("../$bbs/dat/$key.dat");
		$max = count($dat);
		list(,,,$cont,$subject2) = explode("<>",$dat[0]);
		$cont = htmlspecialchars_decode($cont);
		$cont = str_replace(" <br> ", "\n",$cont);
	}
	//PrintBBSError("準備中です！",$"Twitter(<a href=\"https://twitter.com/14ChannelBBS\">@14ChannelBBS</a>)や<a href=\"https://discord.gg/BtNdCYStxn\">Discord</a>で最新情報をご確認ください！");
	$date = new DateTime();
	$weeks = explode("/",$settings["BBS_YMD_WEEKS"]);

	$from = htmlspecialchars($from,ENT_QUOTES,"Shift_JIS",false);
	$from = preg_replace("/\r\n|\n|\r/", "",$from);
	$mail = htmlspecialchars($mail,ENT_QUOTES,"Shift_JIS",false);
	$mail = preg_replace("/\r\n|\n|\r/", "",$mail);
	$content = rtrim($content);
	$content = str_replace('"', "&quot;", $content);
	$content = str_replace("<", "&lt;", $content);
	$content = str_replace(">", "&gt;", $content);
	$content = htmlspecialchars($content,ENT_QUOTES,"Shift_JIS",false);
	$content = str_replace("'", "&#039;", $content);
	$subject = str_replace('"', "&quot;", $subject);
	$subject = str_replace("<", "&lt;", $subject);
	$subject = str_replace(">", "&gt;", $subject);
	$subject = str_replace("'", "&#039;", $subject);
	$subject = htmlspecialchars($subject,ENT_QUOTES,"Shift_JIS",false);
	if (!isset($_COOKIE["2ch_X"]) && $checkrobot != true){
		if (!check2chx()){
			if ($ismonazilla){
				PrintBBSError("認証が必要です。Webブラウザから「https://".$_SERVER['SERVER_NAME']."/test/authkey.php」にアクセスし、画面の指示に従ってください。","ここが見れるのはおかしいよ");
			}else{
				PrintRobotCheckAndRules($settings);
			}
			exit();
		}
	}
	$from = preg_replace('/##(.*)$/',"",$from);
	$content = preg_replace("/\r\n|\n|\r/", " <br> ",$content);
	$content = preg_replace("/\*\*(.*?)\*\*/", "<b>$1</b>",$content);
	$content = preg_replace("/~~(.*?)~~/", "<s>$1</s>",$content);
	$content = preg_replace("/__(.*?)__/", "<u>$1</u>",$content);
	$content = preg_replace("/&lt;i&gt;(.*?)&lt;\/i&gt;/","<i>$1</i>",$content);
	$content = preg_replace("/```(.*?)```/", "<pre style=\"font-size: 16px; line-height: 18px; font-family: Mona,IPAMonaPGothic,'IPA モナー Pゴシック','MS PGothic AA','MS PGothic','ＭＳ Ｐゴシック',sans-serif;\">$1</pre>",$content);
	$content = preg_replace("/\|\|(.*?)\|\|/","<span style=\"background-color: #CECECE;\" onClick=\"this.innerText='$1'\">ネタバレ注意(クリックして表示)</span>",$content);
	$content = preg_replace_callback(
		"/&lt;vibrate&gt;(.*?)&lt;\/vibrate&gt;/",
		function ($matches) {
			return "<span class=\"buruburu\">".$matches[1]."</span> "."<style> .buruburu {    display: inline-block;    animation: hurueru .1s  infinite;}@keyframes hurueru {    0% {transform: translate(0px, 0px) rotateZ(0deg)}    25% {transform: translate(2px, 2px) rotateZ(1deg)}    50% {transform: translate(0px, 2px) rotateZ(0deg)}    75% {transform: translate(2px, 0px) rotateZ(-1deg)}    100% {transform: translate(0px, 0px) rotateZ(0deg)}}</style>";
		},
		$content
	);
	$content = preg_replace("/&lt;fluorescence&gt;(.*?)&lt;\/fluorescence&gt;/","<span style=\"  position: relative;  background: linear-gradient(transparent 40%, yellow 40%);\">$1</span>",$content);
	$content = preg_replace_callback(
		"/&lt;fluorescence color=(.+)&gt;(.*?)&lt;\/fluorescence&gt;/",
		function ($matches) {
			$matches[1] = str_replace("&amp;","#",$matches[1]);
			return "<span style=\"  position: relative;  background: linear-gradient(transparent 40%, ".$matches[1]." 40%);\">".$matches[2]."</span>";
		},
		$content
	);
	$content = preg_replace_callback(
		"/&lt;shuffle&gt;(.*?)&lt;\/shuffle&gt;/",
		function ($matches) {
			$string = str_replace("&", "&amp;",$matches[1]);
			$string = htmlspecialchars_decode($string);
			return mb_str_shuffle($string)." <br> <span style=\"color: red;\"><small>シャッフル、原文→「<span style=\"background-color: #CECECE;\" onClick=\"this.innerText='".$matches[1]."'\">(クリックして表示)</span></small></span><br>";
		},
		$content
	);
	if (!file_exists("../$bbs/dat/$key.dat")){
		$content = preg_replace_callback(
			"/!mail:(.+):/",
			function ($matches) {
				$string = openssl_encrypt($matches[1], 'AES-256-CBC', "Cirno_BAKA_KEY_SANNAN_NAITAYO_5787_````*****+++NIOFJH)FHSGA)HDFABFKJHABFAN", 0, "OREHA_NENNNNEKO%'('_DSJNADUAHUDASD(UTRJHIWO");
				return "!mail:".$string.":";
			},
			$content
		);

		$content = preg_replace_callback(
			"/!discordwebhook:(.+):/",
			function ($matches) {
				$string = openssl_encrypt($matches[1], 'AES-256-CBC', "Cirno_BAKA_KEY_SANNAN_NAITAYO_5787_````*****+++NIOFJH)FHSGA)HDFABFKJHABFAN", 0, "OREHA_NENNNNEKO%'('_DSJNADUAHUDASD(UTRJHIWO");
				return "!discordwebhook:".$string.":";
			},
			$content
		);
		$content = preg_replace_callback(
			"/!pass(.+)!3/",
			function ($matches) {
				return "!pass".password_hash($matches[1],PASSWORD_DEFAULT)."!3";
			},
			$content
		);
	}
	$content = preg_replace_callback(
		"/!odai:(\d+):/",
		function ($matches) {
			$odais = array(
				"好きな食べ物は何？",
				"好きな人は誰？",
				"なんの仕事をしているの？",
				"名前は何？",
				"住んでいるところはどこ？",
			);
			return "<span style=\"color: red;\"><small>&gt;&gt;".$matches[1]." に対してお題→</small></span>".$odais[openssl_rand(0,(count($odais) - 1))];
		},
		$content
	);
	$content = str_replace("\\*\\*", "**",$content);
	$content = str_replace("\\~\\~", "~~",$content);
	$content = str_replace("\\_\\_", "__",$content);
	$content = str_replace("\\`\\`\\`", "```",$content);
	$content = str_replace("\\|\\|", "||",$content);
	$from = str_replace("★", "☆", $from);
	$from = str_replace("◆", "◇", $from);
	if (file_exists("../$bbs/dat/$key.dat")){
		$isnewthread = false;
		if ($dat[(count($dat)-1)] == "停止しました。。。<>停止<>停止<>真・スレッドストッパー。。。(￣ー￣)ﾆﾔﾘ<>\n"){
			PrintBBSError("このスレッドはストップされてるぽいです。。。","スレッドストッパーでも発動したんじゃないですかね？");
			exit();
		}

		list($f,$m,$d,$c,$s) = explode("<>",$dat[0]);
		if (preg_match("/!pass(.+)!3/",$mail, $ac) && preg_match("/!pass(.+)!3/",$cont, $ac2)){
			if (password_verify($ac[1],$ac2[1])){
				$issurenusi = true;
			}
		}
		$mail = preg_replace("/!pass.+!3/", "",$mail);

		if (preg_match_all("/!add:(.*?):/",$content, $ac,PREG_SET_ORDER) && $issurenusi){
			foreach ($ac as $a){
				$c = "$c <hr> <span style=\"color: red;\"><small>追記(".$date->format("Y/m/d H:i:s").")→</small>".$a[1]."</span>";
			}
			$dat[0] = "$f<>$m<>$d<>$c<>$s";
			$ndat = implode("",$dat);

			$cont = $c;
		}

		if (preg_match("/!chtt:(.*):/",$content, $ac) && $issurenusi){
			$gomi = trim($s);
			$s = $ac[1];
			$c = "$c <hr> <span style=\"color: red;\"><small>スレッドタイトル変更(".$date->format("Y/m/d H:i:s").") 元→</small>".$gomi."</span>";
			$dat[0] = "$f<>$m<>$d<>$c<>$s\n";
			$ndat = implode("",$dat);

			$subject2 = $s;
		}

		if (strpos($content,"!stop") !== false && $issurenusi){
			$isthreadstopped = true;
			$ndat = implode("",$dat);
		}
	}else{
		$isnewthread = true;
		$key = time();
		$issurenusi = true;
		$cont = $content;
		$cont = htmlspecialchars_decode($cont);
		$cont = str_replace(" <br> ", "\n",$cont);
		$subject2 = $subject;
		$max = 0;

		$nanasi = array();
		$na = explode("\n",$cont);
		foreach ($na as $a){
			if (preg_match("/!774(.*)!3/",$a, $nanasisto)){
				array_push($nanasi,$nanasisto[1]);
			}
		}
		$maxna = count($nanasi);
		if ($maxna == 1){
			$content = $content." <br> <span style=\"color: red;\"><small>名無し名変更→".$nanasi[0]."</small></span>";
		}else if ($maxna >= 2){
			foreach($nanasi as $nasi){
				$content = $content." <br> <span style=\"color: red;\"><small>名無し名(ランダム)追加→".$nasi."</small></span>";
			}
		}
		if (preg_match("/!maxres(.*)!3/",$cont, $maxres)){
			$settings["BBS_RES_MAX"] = intval($maxres[1]);
			$content = $content." <br> <span style=\"color: red;\"><small>最大レス数変更→".$maxres[1]."</small></span>";
		}

		$nanasi = array();
		$na = explode("\n",$cont);
		foreach ($na as $a){
			if (preg_match("/!mail:(.+):/",$a, $nanasisto)){
				array_push($nanasi,$nanasisto[1]);
			}
		}
		$maxna = count($nanasi);
		if ($maxna == 1){
			$content = $content." <br> <span style=\"color: red;\"><small>レスがあったときにメール送信→".$nanasi[0]."</small></span>";
		}else if ($maxna >= 2){
			foreach($nanasi as $nasi){
				$content = $content." <br> <span style=\"color: red;\"><small>レスがあったときにメール送信→".$nasi."</small></span>";
			}
		}

		$nanasi = array();
		$na = explode("\n",$cont);
		foreach ($na as $a){
			if (preg_match("/!gacha(.*)!3/",$a, $nanasisto)){
				array_push($nanasi,$nanasisto[1]);
			}
		}
		$maxna = count($nanasi);
		if ($maxna == 1){
			$content = $content." <br> <span style=\"color: red;\"><small>ガチャ(一個だけ！？)→".$nanasi[0]."</small></span>";
		}else if ($maxna >= 2){
			foreach($nanasi as $nasi){
				$content = $content." <br> <span style=\"color: red;\"><small>ガチャ(追加)→".$nasi."</small></span>";
			}
		}

		$nanasi = array();
		$na = explode("\n",$cont);
		foreach ($na as $a){
			if (preg_match("/!discordwebhook:(.+):/",$a, $nanasisto)){
				array_push($nanasi,$nanasisto[1]);
			}
		}
		$maxna = count($nanasi);
		if ($maxna == 1){
			$content = $content." <br> <span style=\"color: red;\"><small>レスがあったときにDiscordのWebhook→".substr($nanasi[0],0,10)."(省略)</small></span>";
		}else if ($maxna >= 2){
			foreach($nanasi as $nasi){
				$content = $content." <br> <span style=\"color: red;\"><small>レスがあったときにDiscordのWebhook→".substr($nasi,0,10)."(省略)</small></span>";
			}
		}

		$nanasi = array();
		$na = explode("\n",$cont);
		foreach ($na as $a){
			if (preg_match("/!pass(.+)!3/",$a, $nanasisto)){
				array_push($nanasi,$nanasisto[1]);
			}
		}
		$maxna = count($nanasi);
		if ($maxna >= 1){
			$content = $content." <br> <span style=\"color: red;\"><small>スレッドパス→".$nanasi[0]."</small></span>";
		}

		if (preg_match("/!maxres(.*)!3/",$cont, $maxres)){
			$settings["BBS_RES_MAX"] = intval($maxres[1]);
			$content = $content." <br> <span style=\"color: red;\"><small>最大レス数変更→".$maxres[1]."</small></span>";
		}

		if (strpos($cont,"!force774") !== false){
			$content = $content." <br> <span style=\"color: red;\"><small>強制名無し</small></span>";
		}
		if (strpos($cont,"!forcekote") !== false){
			$content = $content." <br> <span style=\"color: red;\"><small>強制コテハン</small></span>";
		}
		if (strpos($cont,"!noid") !== false){
			$content = $content." <br> <span style=\"color: red;\"><small>ID&#127824;</small></span>";
		}
	}
	if (preg_match("/!maxres(.*)!3/",$cont, $maxres)){
		$settings["BBS_RES_MAX"] = intval($maxres[1]);
	}
	if ($from != "" && strpos($cont,"!force774") === false){
		$from = trip($from);
	}else{
		if (strpos($cont,"!forcekote") !== false){
			PrintBBSError("このスレッドではコテハン必須なようです！","このスレッドは嫌われている可能性が高い");
		}
		$nanasi = array();
		$na = explode("\n",$cont);
		foreach ($na as $a){
			if (preg_match("/!774(.*)!3/",$a, $nanasisto)){
				array_push($nanasi,$nanasisto[1]);
			}
		}

		$maxna = count($nanasi);
		if ($maxna != 0){
			$from = $nanasi[mt_rand(0,$maxna-1)];
		}else{
			$from = $settings["BBS_NONAME_NAME"];
		}
	}

	if ($from == "fusianasan" || $from == "山崎渉" || $from == "tasukeruyo"){
		$from = "</b>".$host."<b>";
		$content = $content." <hr> <span style=\"color: blue;\"><i>".$_SERVER['HTTP_USER_AGENT']."</i></span> <hr> <span style=\"color: blue;\"><i>".$client_id."</i></span>";
	}

	$nanasi = array();
	$na = explode("\n",$cont);
	foreach ($na as $a){
		if (preg_match("/!gacha(.*)!3/",$a, $nanasisto)){
			array_push($nanasi,$nanasisto[1]);
		}
	}

	$maxna = count($nanasi);
	if ($maxna != 0){
		$content = str_replace("!:gacha:","<span style=\"color: red;\"><small>ガチャの結果→</small></span>".$nanasi[mt_rand(0,$maxna-1)],$content);
	}

	$id = generateid();
	checkacap();
	if ($issurenusi){
		$id = $id."<span style=\"color: red;\"><small>主</small></span>";
	}
	if (strpos($cont,"!noid") !== false){
		$id = "";
	}
	if ($id != "ReportForm"){
		setcookie("cookName",$_POST["FROM"],(time()+60*60*24*(365*10)));
		setcookie("cookMail",$_POST["mail"],(time()+60*60*24*(365*10)));
	}
	//キャップ付きのみが書ける かつ キャップを持っていない場合は エラー
	if (!file_exists("../$bbs/dat/$key.dat") && substr($settings["BBS_TITLE"] , -1) == "+" && $iscap == false){
		PrintBBSError("この掲示板は★付きの記者さんのみスレッドが立てられます","過去にキャップを配布しています。探してみてください。");
		exit();
	}
	$now = microtime(true);
	$ms = (int)(($now - (int)$now) * 1000);
	$msStr = str_pad($ms, 2, 0, STR_PAD_LEFT);

	//もしもレス数がBBS_RES_MAXを超えてるならば、エラー
	if ($max >= intval($settings["BBS_RES_MAX"])){
		PrintBBSError("このスレッドはもう書けません！","このスレッドは".$settings["BBS_RES_MAX"]."レスまで書けたみたいです");
		exit();
	}

	//板内連続書き込み規制
	if (intval($settings['timecount']) >= 2) {
		# 投稿者のホスト名記録ファイルを読み込む（timecount個記録されている）
		$file = "../$bbs/timecheck.cgi";
		$IP = array();
		$ipchk = array();
		$count = 0;
		if (file_exists($file)) {
			$IP = file($file);
			foreach($IP as $tmp){
				$tmp = rtrim($tmp);
				list($time1,$host1) = explode("<>", $tmp);
				if ($ipaddr == $host1) {
					# 同じ投稿フォームからの場合は2重カキコとしてエラー
					if ($_POST['time'] == $time1){
						PrintBBSError("２重カキコですか？？","もうすでに書き込めていると思われます");
						exit();
					}
					# ホスト名が同じ投稿の数をカウント
					$count++;
					array_push($ipchk,$time1);
				}
			}
		}
		# もし最後の書き込み時間が(現在時刻-timeskip)秒よりあとの場合
		if ((intval($ipchk[max($ipchk)]) <= (time() - intval($settings["timeskip"]))) && !$timeskip){
			# timecount 個の投稿内にtimeclose 個以上の投稿があればエラー
			if ($count >= intval($settings['timeclose'])){
				PrintBBSError("連続投稿ですか？？","連続投稿じゃないのに書けない場合は".$settings['timeskip']."秒後にもう一度書き込んでください。");
				exit();
			}
		}
		array_unshift($IP, "$_POST[time]<>$ipaddr\n");
		# 記録ファイル内のホスト数を timecount 個以内に調整して保存
		while (count($IP) > $settings['timecount']) array_pop($IP);
		$fp = @fopen($file, "w");
		foreach($IP as $tmp) fputs($fp, $tmp);
		fclose($fp);
	}

	//もしもレス数がBBS_RES_MAXを超えているならば、Over <BBS_RES_MAX> Threadを出す
	if (isset($ndat)){
		if ($isthreadstopped == true){
			$_a = "停止しました。。。<>停止<>停止<>真・スレッドストッパー。。。(￣ー￣)ﾆﾔﾘ<>";
			if (($max+1) >= intval($settings["BBS_RES_MAX"])){
				file_put_contents("../$bbs/dat/$key.dat",$ndat."$from<>$mail<>".$date->format('Y/m/d')."(".$weeks[intval($date->format('w'))].") ".$date->format('H:i:s').".".$msStr." ID:$id<>$content<>$subject\n$_a\nOver ".$settings["BBS_RES_MAX"]." Thread<><>".$date->format('Y/m/d')."(".$weeks[intval($date->format('w'))].") ".$date->format('H:i:s').".".$msStr."<>このスレッドは".$settings["BBS_RES_MAX"]."レスを超えました。<br> 続きは<a href=\"/\">14Channel BBS</a>でどうぞ。<>\n",LOCK_EX);
			}else{
				file_put_contents("../$bbs/dat/$key.dat",$ndat."$from<>$mail<>".$date->format('Y/m/d')."(".$weeks[intval($date->format('w'))].") ".$date->format('H:i:s').".".$msStr." ID:$id<>$content<>$subject\n$_a\n",LOCK_EX);
			}
		}else{
			if (($max+1) >= intval($settings["BBS_RES_MAX"])){
				file_put_contents("../$bbs/dat/$key.dat",$ndat."$from<>$mail<>".$date->format('Y/m/d')."(".$weeks[intval($date->format('w'))].") ".$date->format('H:i:s').".".$msStr." ID:$id<>$content<>$subject\nOver ".$settings["BBS_RES_MAX"]." Thread<><>".$date->format('Y/m/d')."(".$weeks[intval($date->format('w'))].") ".$date->format('H:i:s').".".$msStr."<>このスレッドは".$settings["BBS_RES_MAX"]."レスを超えました。<br> 続きは<a href=\"/\">14Channel BBS</a>でどうぞ。<>\n",LOCK_EX);
			}else{
				file_put_contents("../$bbs/dat/$key.dat",$ndat."$from<>$mail<>".$date->format('Y/m/d')."(".$weeks[intval($date->format('w'))].") ".$date->format('H:i:s').".".$msStr." ID:$id<>$content<>$subject\n",LOCK_EX);
			}
		}
	}else{
		if (($max+1) >= intval($settings["BBS_RES_MAX"])){
			file_put_contents("../$bbs/dat/$key.dat","$from<>$mail<>".$date->format('Y/m/d')."(".$weeks[intval($date->format('w'))].") ".$date->format('H:i:s').".".$msStr." ID:$id<>$content<>$subject\nOver ".$settings["BBS_RES_MAX"]." Thread<><>".$date->format('Y/m/d')."(".$weeks[intval($date->format('w'))].") ".$date->format('H:i:s').".".$msStr."<>このスレッドは".$settings["BBS_RES_MAX"]."レスを超えました。<br> 続きは<a href=\"/\">14Channel BBS</a>でどうぞ。<>\n",FILE_APPEND|LOCK_EX);
		}else{
			file_put_contents("../$bbs/dat/$key.dat","$from<>$mail<>".$date->format('Y/m/d')."(".$weeks[intval($date->format('w'))].") ".$date->format('H:i:s').".".$msStr." ID:$id<>$content<>$subject\n",FILE_APPEND|LOCK_EX);
		}
	}
	
	chmod("../$bbs/dat/$key.dat",0664);
	file_put_contents("../$bbs/log/$key.log","$from<>$mail<>ID:$id<>$content<>$subject<>$bbs<>$key<>".time()."<>$ipaddr<>$host\n",FILE_APPEND|LOCK_EX);
	chmod("../$bbs/log/$key.log",0664);

	$nanasi = array();
	$na = explode("\n",$cont);
	foreach ($na as $a){
		if (preg_match("/!mail:(.+):/",$a, $nanasisto)){
			array_push($nanasi,$nanasisto[1]);
		}
	}

	foreach ($nanasi as $mailaddr){
		$mailad = openssl_decrypt($mailaddr, 'AES-256-CBC', $encrypt_key, 0, $encrypt_iv);
		mb_internal_encoding("Shift_JIS");
		mb_language("ja");
		$header = array();
		$header['MIME-Version'] 				= "1.0";
		$header['Content-Type'] 				= "text/plain; charset=Shift_JIS";
		$header['Content-Transfer-Encoding'] 	= "8bit";
		$header['From'] 						= "nchannel.p@users.osdn.me";
		//headerを編集
		$set_header = array();
		foreach ($header as $a => $val) 
		{
			$set_header[] = $a . ': ' . $val;
		}
		
		// ヘッダーを1文に結合
		$send_header = implode("\n", $set_header);
		$_bool = mb_send_mail(
			$mailad,
			"あなたのスレッド「".$subject2."」に新しいレスが付きました！",
			wordwrap("https://apple.14chan.cf/test/read.cgi/$bbs/$key/", 70, "\r\n"),
			$set_header
		);
	}

	$nanasi = array();
	$na = explode("\n",$cont);
	foreach ($na as $a){
		if (preg_match("/!discordwebhook:(.+):/",$a, $nanasisto)){
			array_push($nanasi,$nanasisto[1]);
		}
	}

	foreach ($nanasi as $mailaddr){
		$mailad = openssl_decrypt($mailaddr, 'AES-256-CBC', $encrypt_key, 0, $encrypt_iv);
		$_a = sendwebhook($bbs,$key,$from,$content,$subject2,$mailad,($max+1));
	}

	$subjecttxt = file_get_contents("../$bbs/subject.txt");
	$subject2 = trim($subject2);
	if (!isset($subject2)||$subject2 == ""){
		$subject2 = '[ここ壊れてます]';
	}
	//$subjecttxt = str_replace("$key.dat<>$subject2 (".$max.")\n", "", $subjecttxt);
	//$subjecttxt = str_replace("$key.dat<>$gomi (".$max.")\n", "", $subjecttxt);
	if (false === strpos("sage", $mail)) {
		$subjecttxt = preg_replace("/$key\.dat<>.*\n/", "", $subjecttxt);
	}
	
	if (false !== strpos("soko",$mail)) {
		$subjecttxt = "$subjecttxt$key.dat<>$subject2 (".($max+1).")\n";
	}else if (false !== strpos("sage", $mail)) {
		if ($isnewthread != false){
			$subjecttxt = $subjecttxt;
		}else{
			$subjecttxt = "$subjecttxt$key.dat<>$subject2 (".($max+1).")\n";
		}
	}else{
		$subjecttxt = "$key.dat<>$subject2 (".($max+1).")\n$subjecttxt";
	}
	file_put_contents("../$bbs/subject.txt",$subjecttxt,LOCK_EX);
	generateHTML($bbs);
	$ms2 = microtime(true);
	echo '<html><head>
	<title>書きこみました。</title>
	<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
	<meta http-equiv="Refresh" content="3;URL=/test/read.cgi/'.$bbs.'/'.$key.'/">
	<meta name="robots" content="noindex">
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
	</head>
	
	<body>
	書きこみが終わりました。 ['.($ms2-$ms1).'s]<br>
	<br>
	画面を切り替えるまでしばらくお待ち下さい。<br>
	<br>
	<br>
	<br>
	<br>
	<hr>
	
	
	</body></html>';

function PrintBBSError($str1,$str2){
	global $from;
	global $mail;
	global $content;
	global $bbs;
	global $key;
	global $subject;
	global $time;
	global $host;
	global $ipaddr;
	global $ismonazilla;

	if ($ismonazilla){
		echo '<html><!-- 2ch_X:error --><head>
		<title>ＥＲＲＯＲ！</title>
		<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
		</head>
		<body bgcolor="#EFEFEF"><font size="+1" color="#FF0000"><b>'.$str1.'</b></font><hr /></body></html>';
	}else{
		echo '<html><!-- 2ch_X:error --><head>
		<title>ＥＲＲＯＲ！</title>
		<meta name="robots" content="noindex">
		<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
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
		</head>
		<body bgcolor="#EFEFEF">
		<font size="+1" color="#FF0000"><b>ERROR: '.$str1.'</b></font><br />
		<font size="-0.5" color="#FF0000"><b>'.$str2.'</b></font>
		<ul>
		問い合わせID：<b> '.$_SERVER['HTTP_CF_RAY'].'</b><br>ホスト：<b>'.$host.'</b><br><br>IPアドレス：<b>'.$ipaddr.'</b>
		<ul>
		タイトル： <b>'.$subject.'</b><br>名前： <b>'.$from.'</b><br>E-mail： <b>'.$mail.'</b><br>
		内容：<b>'.$content.'</b><br><br>
		</ul>
		</ul>
		<hr>
		<ul>
		<font size="+1" color="#00AA00"><b>エラーの原因が分からない？</b></font>
		<ul style="line-height:1.5;">
		まず確認しよう！<br>
		<b>
		《<a href="//info.5ch.net/?curid=686">書き込めない時の早見表</a>》<br>
		《<a href="../'.$bbs.'/">掲示板へ戻る</a>》<br>
		《<a href="../'.$bbs.'/subback.html">スレッド一覧へ戻る</a>》<br>
		《<a href="../test/read.cgi/'.$bbs.'/'.$key.'">スレッドへ戻る</a>》<br>
		</b>
		</ul><br>
		<font size="+1" color="#DD00DD"><b>もしかしてアクセス規制ですか？</b></font>
		<ul style="line-height:1.5;">
		お使いのプロバイダさんが、<b>原因となった人に対応</b>するまで規制は続きます。<br>
		個別の対応・進展については、プロバイダさんへお尋ねください。<br>
		<small>その他、14Channel BBSについては、
		<a href="/qa/">初心者の質問</a>
		<a href="/accuse/">批判要望</a>
		<a href="/operate/">運用情報</a>
		<a href="/operatex/">運用臨時</a>
		などへどうぞ。</small>
		</ul><br>
		<!--
		<font size="+1" color="#DD3300"><b>● 浪人について</b></font>
		<ul style="line-height:1.5;">
		浪人を導入することで規制が緩和されます。<br>
		浪人の購入は <a href="//premium.5ch.net/">こちら</a> から<br>
		既に浪人をお持ちなら <a href="//login.5ch.net/login.php">ログイン</a> することで有効になります。 <br>
		</ul>
		-->
		
		</ul></body></html>';
	}
}

function PrintRobotCheckAndRules($settings,$flag = false) {
	global $bbs;
	global $key;
	global $from;
	global $mail;
	global $subject;
	global $content;
	global $ipaddr;
	global $host;
	global $sitekey;

	if ($flag == true){
		$string = "<br><font size=\"4\" color=\"#FF0000\"><b>認証に失敗しました。もう一度認証をお願いします。</b></font>";
	}

	$kakunin = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<!-- 2ch_X:cookie -->
	<head>
	
	 <meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
	
	 <title>■ 書き込み確認 ■</title>
	 <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
	 <!--<script src="https://js.hcaptcha.com/1/api.js" async defer></script>-->
	</head>
	<body vlink="#AA0088" text="#000000" link="#0000FF" bgcolor="#EFEFEF" alink="#FF0000">
	<font size="4" color="#FF0000"><b>書きこみ＆ロボットチェック</b></font>
	'.$string.'
	<blockquote style="margin-top:4em;">
	名前： '.$from.'<br>
	E-mail： '.$mail.'<br>
	内容：<br>
	'.$content.'<br>
	</blockquote>

	<div style="font-weight:bold;">
	投稿確認<br>
	・投稿者は、投稿に関して発生する責任が全て投稿者に帰すことを承諾します。<br>
	・投稿者は、話題と無関係な広告の投稿に関して、相応の費用を支払うことを承諾します<br>
	・投稿者は、投稿された内容について、掲示板運営者がコピー、保存、引用、転載等の利用することを許諾します。<br>
	　また、掲示板運営者に対して、著作者人格権を一切行使しないことを承諾します。<br>
	・投稿者は、掲示板運営者が指定する第三者に対して、著作物の利用許諾を一切しないことを承諾します。<br>
	</div>

	<p>
	現在、荒らし対策でロボットチェックを通過していないと書きこみできないようにしています。<br>
	<font size="2">(cookieを設定するとこの画面はでなくなります。)</font><br><br>
	<b>専ブラを使用している人やCookieが保存できない環境の人はWebブラウザから認証し、<a href="https://'.$_SERVER["SERVER_NAME"].'/test/authkey.php">https://'.$_SERVER["SERVER_NAME"].'/test/authkey.php</a>にアクセスし、認証キーを入手してください。</b><br>
	<pre>
	bbs:'.$bbs;
	if (isset($key) && $key != null) $kakunin = $kakunin."\n".'	key:'.$key;
	if (isset($subject) && $subject != null) $kakunin = $kakunin."\n".'	subject:'.$subject;
	$kakunin = $kakunin."\n".'	name:'.$from.'
	E-mail: '.$mail.'
	content:'.htmlspecialchars($content,ENT_QUOTES,"Shift_JIS").'
	ipaddr:'.$ipaddr.'
	host:'.$host.'
	ray-id:'.$_SERVER['HTTP_CF_RAY'].'
	</pre>
	</p>

	<form method="POST" action="/test/bbs.cgi">
	<div class="cf-turnstile" data-sitekey="'.$sitekey.'" data-callback="javascriptCallback"></div>
	<!--<div class="h-captcha" data-sitekey="3c898ad4-cd79-4bf7-aa03-246ceef4e1ad"></div>-->
	<input type="hidden" name="bbs" value="'.$bbs.'">';
	if (isset($key) && $key != null) $kakunin = $kakunin."\n".'	<input type="hidden" name="key" value="'.$key.'">';
	$kakunin = $kakunin."\n".'	<input type="hidden" name="time" value="'.time().'">
	<input type="hidden" name="FROM" value="'.$from.'" size="19">
	<input type="hidden" name="mail" value="'.$mail.'" size="19">';
	if (isset($subject) && $subject != null) $kakunin = $kakunin."\n".'	<input type="hidden" name="subject" value="'.$subject.'" size="19">';
	$kakunin = $kakunin."\n".'<input type="hidden" name="MESSAGE" value="'.$content.'" size="19">
	<input type="submit" value="上記全てを承諾して書き込む"><br>
	</form>

	<p>
	変更する場合は戻るボタンで戻って書き直して下さい。
	</p>

	</body>
	</html>';

	echo $kakunin;
}

function check2chx(){
	global $from;
	preg_match('/##(.*)$/', $from, $match);
	$a = file_get_contents("../robotcheck_bypass.txt");
	if (!isset($match[1]) || $match[1] == ""){
		return false;
	}
	if (false !== strpos($a, $match[1]."\n")) {
		setcookie("2ch_X", $match[1], (time()+60*60*24*(365*10)));
		return true;
	}else if (false === strpos($a, $match[1]."\n")) {
		return false;
	}
}


function trip( $name ) {
	if (preg_match("/([^\#]*)\#(.+)/", $name, $match)) {
		if ( strlen($match[2]) >= 12 ) {
			if ( substr($match[2], 0, 1) === '#' ) { // 10 digits new protocol
				if ( preg_match( '|^#([0-9a-fA-F]{16})([./0-9a-zA-Z]{0,2})$|', $match[2], $matches ) ) {
					$key = pack('H*', $matches[1]);
					if ( ( $index = strpos($key, chr(128)) ) !== false )
						$key = substr($key, 0, $index);
					$trip = substr(crypt($key, substr($matches[2].'..', 0, 2)), -10);
					$name = $match[1]."</b> ◆".$trip."<b>";
				} else
					$trip = '???';
					$name = $match[1]."</b> ◆".$trip."<b>";
			} elseif ( substr($match[2], 0, 1) === '#' ) { // reserved
				$trip = '???';
				$name = $match[1]."</b> ◆".$trip."<b>";
			} else // 12 digits
				$trip = str_replace('+', '.', substr(base64_encode(sha1($match[2], true)), 0, 12));
				$name = $match[1]."</b> ◆".$trip."<b>";
		}else{
			$salt = substr($match[2]."H.", 1, 2);
			$salt = preg_replace("/[^\.-z]/", ".", $salt);
			$salt = strtr($salt,":;<=>?@[\\]^_`","ABCDEFGabcdef");
			$trip = substr(crypt($match[2], $salt),-10);
			$name = $match[1]."</b> ◆".$trip."<b>";
		}
	}
	return $name;
}

function generateid(){
	//初期パラメータ
	global $ipaddr;
	global $bbs;
	$date = new DateTime();
	$timestamp = $date->format('Y-m-d');
	$secret = "$bbs-$encrypt_key";

	//sha1を使ってハッシュ化
	$id_hash = hash_hmac("sha1", $timestamp.$ipaddr, $secret);

	//base64の形式に変換
	$id_base64 = base64_encode($id_hash);

	//先頭の8文字だけ抜き取る
	$id =  substr($id_base64, 0, 8);
	return $id;
}

function checkacap(){
	global $from;
	global $mail;
	global $id;
	global $iscap;
	global $timeskip;
	global $caps;
	global $isadmin;
	preg_match('/#(.*)/', $mail, $match);
	foreach($caps as $index => $value){
		if (password_verify($match[1],$caps[$index][0])){
			$from = str_replace("<FROM>",$from,$caps[$index][1]);
			$id = $caps[$index][2];
			$isadmin = $caps[$index][3];
			$iscap = $caps[$index][4];
			$timeskip = $caps[$index][5];
		}
	}
	$mail = preg_replace('/#(.*)/', '', $mail);
}