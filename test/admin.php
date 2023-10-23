<?php
	if (!isset($_SERVER['HTTP_CF_CONNECTING_IP'])){
		$ipaddr = $_SERVER["REMOTE_ADDR"];
	}else{
		$ipaddr = $_SERVER['HTTP_CF_CONNECTING_IP'];
	}
	$host = gethostbyaddr($ipaddr);

	$from = '名無しさん@14ちゃんねる';
	$id = generateid();
	$iscap = false;

	if (isset($_POST["bbs"])){
		require "modules.php";
		require "SysSettings.php";
		$settings = parse_ini_file($_POST["bbs"].'/SETTING.TXT',false,INI_SCANNER_RAW);
		foreach($caps as $index => $value){
			if (password_verify($_POST["pass"],$caps[$index][0])){
				$from = str_replace("<FROM>",$from,$caps[$index][1]);
				$id = $caps[$index][2];
				$iscap = $caps[$index][3];
				$timeskip = $caps[$index][4];
			}
		}

		if ($iscap){
			if (!isset($_POST["operation"])){
?>
<h1>キャップ持ち用管理ページ（笑）</h1>
<?=$from?>(<?=$id?>)さん、こんにちは<br>
<form action="/test/admin.php" method="post">
現在選択されている板：<?=substr($_POST["bbs"], 3)?><input type="hidden" name="bbs" value="<?=$_POST["bbs"]?>"><br>
スレッドを選択してみる：<select name="thread">
<option value="">何も選択しない</option>
<?php
	$dir = $_POST["bbs"]."/dat/*.dat";
	$list1 = glob($dir);

	foreach ($list1 as $dir1) {
		$dat = file($dir1);
		list(,,,,$subject) = explode("<>",$dat[0]);
		$subject = trim($subject);
		echo "<option value=\"$dir1\">".$subject."(".substr($dir1, 11).")</option>";
	}
?>
</select><br>
引数(optional)：<input type="text" name="insu"><br>
何をするか考えてみる：<select name="operation" required>
<option value="">--選択してください--</option>
<option value="0">index.htmlの再生成</option>
<option value="1">スレッドの削除</option>
<option value="2">レスの削除</option>
<option value="3">レスの削除</option>
</select><br>
<input type="hidden" name="pass" value="<?=$_POST["pass"]?>">
<input type="submit" value="操作開始">
</form>
<?php
			}else{
				if ($_POST["operation"] == "0"){
					generateHTML(substr($_POST["bbs"], 3));
					echo "Operation Successful";
					exit();
				}else if ($_POST["operation"] == "1"){
					if (!isset($_POST["thread"]) || !file_exists($_POST["thread"])){
						echo "そんなスレッド存在しません。";
						exit();
					}else{
						$dat = file($_POST["thread"]);
						$max = count($dat);
						list(,,,,$subject) = explode("<>",$dat[0]);
						if (unlink($_POST["thread"])){
							$subjecttxt = file_get_contents($_POST["bbs"]."/subject.txt");
							$subject = trim($subject2);
							$subjecttxt = str_replace(substr($dir1, 11)."<>$subject (".$max.")\n", "", $subjecttxt);
							file_put_contents("../$bbs/subject.txt",$subjecttxt,LOCK_EX);
							generateHTML(substr($_POST["bbs"], 3));
							echo "Operation Successful";
							exit();
						}else{
							echo "Operation Failure";
							exit();
						}
					}
				}else if ($_POST["operation"] == "2"){
					if (!isset($_POST["thread"]) || !file_exists($_POST["thread"])){
						echo "そんなスレッド存在しません。";
						exit();
					}else{
						$dat = file($_POST["thread"]);
						$dat[(intval($_POST["insu"])-1)] = $settings["BBS_DELETE_NAME"]."<>".$settings["BBS_DELETE_NAME"]."<>".$settings["BBS_DELETE_NAME"]."<>".$settings["BBS_DELETE_NAME"]."<>".$settings["BBS_DELETE_NAME"]."\n";
						$datraw = implode("", $dat);
						file_put_contents($_POST["thread"],$datraw,LOCK_EX);
						generateHTML(substr($_POST["bbs"], 3));
						echo "Operation Successful";
						exit();
					}
				}else{
					echo "不正っすね～ｗｗｗ";
					exit();
				}
			}
		}else{
			echo 'あなたの提示したキャップは運営キャップでは内容です。多分記念キャップ。';
			exit();
		}
	}else{
?>
<h1>キャップ持ち用管理ページ（笑）</h1>
<?=$from?>(<?=$id?>)、こんにちは<br>
<form action="/test/admin.php" method="post">
板を選択してみる：<select name="bbs" required>
<option value="">--選択してください--</option>
<?php
	$dir = '../';
	$list1 = glob($dir . '*', GLOB_ONLYDIR);

	foreach ($list1 as $dir1) {
		if (file_exists($dir1.'/SETTING.TXT')) {
			$settings = parse_ini_file($dir1.'/SETTING.TXT',false,INI_SCANNER_RAW);
			echo "<option value=\"$dir1\">".$settings["BBS_TITLE"]."</option>";
		}
	}
?>
</select><br>
お前は本当にキャップ持ちか？：<input type="password" name="pass"><br>
<input type="submit" value="ログイン">
</form>
<?php
	}

	function generateid(){
		//初期パラメータ
		global $ipaddr;
		$date = new DateTime();
		$timestamp = $date->format('Y-m-d');
		$secret = "$bbs".$date->format('d-m-Y');

		//sha1を使ってハッシュ化
		$id_hash = hash_hmac("sha1", $timestamp.$ipaddr, $secret);

		//base64の形式に変換
		$id_base64 = base64_encode($id_hash);

		//先頭の8文字だけ抜き取る
		$id =  substr($id_base64, 0, 8);
		return $id;
	}
?>