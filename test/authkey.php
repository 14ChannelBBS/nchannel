<?php
	require "SysSettings.php";
	if (strpos("{\"result\":{\"ipv4_cidrs\":[\"173.245.48.0/20\",\"103.21.244.0/22\",\"103.22.200.0/22\",\"103.31.4.0/22\",\"141.101.64.0/18\",\"108.162.192.0/18\",\"190.93.240.0/20\",\"188.114.96.0/20\",\"197.234.240.0/22\",\"198.41.128.0/17\",\"162.158.0.0/15\",\"104.16.0.0/13\",\"104.24.0.0/14\",\"172.64.0.0/13\",\"131.0.72.0/22\"],\"ipv6_cidrs\":[\"2400:cb00::/32\",\"2606:4700::/32\",\"2803:f800::/32\",\"2405:b500::/32\",\"2405:8100::/32\",\"2a06:98c0::/29\",\"2c0f:f248::/32\"],\"etag\":\"38f79d050aa027e3be3865e495dcc9bc\"},\"success\":true,\"errors\":[],\"messages\":[]}",$_SERVER["REMOTE_ADDR"]) !== false){
		$ipaddr = $_SERVER["REMOTE_ADDR"];
	}else{
		$ipaddr = $_SERVER['HTTP_CF_CONNECTING_IP'];
	}
	$id = $_COOKIE["2ch_X"]; //$id_base64;
	$a = file_get_contents("../robotcheck_bypass.txt");
	if (!isset($_COOKIE["2ch_X"]) || $_COOKIE["2ch_X"] == ""){
		$auth = false;
	}else if (false !== strpos($a, $id."\n")) {
		$auth = true;
	}else if (false === strpos($a, $id."\n")) {
		$auth = false;
	}
	if (isset($_POST["cf-turnstile-response"])){
		//�V�[�N���b�g(�������g�����͕s��)
		$id = bin2hex(openssl_random_pseudo_bytes(8));
		//���J���Ă��ǂ��N���C�A���gID�𐶐�
		$clientid = bin2hex(openssl_random_pseudo_bytes(16));

		$POST_DATA = array(
			'secret' => $turnstile_secret,
			'response' => $_POST["cf-turnstile-response"],
			'remoteip' => $ipaddr
		);
		$curl=curl_init("https://challenges.cloudflare.com/turnstile/v0/siteverify");
		curl_setopt($curl,CURLOPT_POST, TRUE);
		// ����multipart���N�G�X�g�������Ă��Ȃ��T�[�o�̏ꍇ�̓_�����ۂ��ł�
		// @DrunkenDad_KOBA����AThanks
		curl_setopt($curl,CURLOPT_POSTFIELDS, $POST_DATA);
		//curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($POST_DATA));
		curl_setopt($curl,CURLOPT_SSL_VERIFYPEER, FALSE);  // �I���I���ؖ����΍�
		curl_setopt($curl,CURLOPT_SSL_VERIFYHOST, FALSE);  // 
		curl_setopt($curl,CURLOPT_RETURNTRANSFER, TRUE);
		curl_setopt($curl,CURLOPT_COOKIEJAR,	  'cookie');
		curl_setopt($curl,CURLOPT_COOKIEFILE,	 'tmp');
		curl_setopt($curl,CURLOPT_FOLLOWLOCATION, TRUE); // Location�w�b�_��ǐ�
		//curl_setopt($curl,CURLOPT_REFERER,		"REFERER");
		//curl_setopt($curl,CURLOPT_USERAGENT,	  "USER_AGENT"); 
		curl_setopt($curl, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);	//IPv4�������󂯕t����
		curl_setopt($curl, CURLOPT_FORBID_REUSE, true);
		
		$json = curl_exec($curl);
		$output= json_decode($json,true);
		//var_dump($output);
		if ($output["success"] != true){
			setcookie("2ch_X", "", time()-60);
			echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
			<html>
			<head>
			
			 <meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
			
			 <title>�� �F�؂Ɏ��s���܂����B ��</title>
			 <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
			</head>
			<body vlink="#AA0088" text="#000000" link="#0000FF" bgcolor="#EFEFEF" alink="#FF0000">
			<font size="4" color="#FF0000"><b> �F�؂Ɏ��s���܂����B</b></font><br>
			<p>�������F�؂��܂��傤�I</p>
			<hr>
			<form method="post" action="/test/authkey.php">
			<div class="cf-turnstile" data-sitekey="'.$sitekey.'" data-callback="javascriptCallback"></div>
			<input type="submit" value="�F��">
			</form>
		
		</body>
		</html>';
			exit();
		}else{
			setcookie("2ch_X", $id, (time()+60*60*24*(365*10)));
			setcookie("client_id",$clientid,(time()+60*60*24*(365*10)));
			file_put_contents("../robotcheck_bypass.txt","$id<>$clientid\n",FILE_APPEND);
			chmod("../robotcheck_bypass.txt",0660);
			echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
			<html>
			<head>
			
			 <meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
			
			 <title>�� �F�؂ɐ������܂����B ��</title>
			</head>
			<body vlink="#AA0088" text="#000000" link="#0000FF" bgcolor="#EFEFEF" alink="#FF0000">
			<font size="4" color="#FF0000"><b>�F�؂ɐ������܂����B���Ȃ��̔F�؃L�[��"'.$id.'"�ł��I�ȉ��̂悤�ɂ��ĔF�؂��Ă��������I</b></font><br>
			<p><���O>#<�g���b�v�L�[>##'.$id.'</p>
			<hr>
		
		</body>
		</html>';
		exit();
		}
	}
	if ($auth == true){
		echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
		<html>
		<head>
		
		 <meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
		
		 <title>�� ���Ȃ��̔F�؃L�[ ��</title>
		</head>
		<body vlink="#AA0088" text="#000000" link="#0000FF" bgcolor="#EFEFEF" alink="#FF0000">
		<font size="4" color="#FF0000"><b>���Ȃ��̔F�؃L�[��"'.$id.'"�ł��I�ȉ��̂悤�ɂ��ĔF�؂��Ă��������I</b></font><br>
		<p><���O>#<�g���b�v�L�[>##'.$id.'</p>
		<hr>
	
	</body>
	</html>';
	}else{
		echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
		<html>
		<head>
		
		 <meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
		
		 <title>�� �܂��F�؂��ĂȂ��݂��� ��</title>
		 <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
		</head>
		<body vlink="#AA0088" text="#000000" link="#0000FF" bgcolor="#EFEFEF" alink="#FF0000">
		<font size="4" color="#FF0000"><b>���Ȃ��͂܂��F�؂��Ă��Ȃ��݂����ł��B</b></font><br>
		<p>�����ŔF�؂��Ă��܂��܂��傤�I</p>
		<hr>
		<form method="post" action="/test/authkey.php">
		<div class="cf-turnstile" data-sitekey="'.$sitekey.'" data-callback="javascriptCallback"></div>
		<input type="submit" value="�F��">
		</form>
	
	</body>
	</html>';
	}