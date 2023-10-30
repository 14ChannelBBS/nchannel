<?php
	if (!isset($_SERVER['HTTP_CF_CONNECTING_IP'])){
		$ipaddr = $_SERVER["REMOTE_ADDR"];
	}else{
		$ipaddr = $_SERVER['HTTP_CF_CONNECTING_IP'];
	}
	$host = gethostbyaddr($ipaddr);

	$from = '����������@14�����˂�';
	$iscap = false;

	if (isset($_POST["bbs"])){
		require "modules.php";
		require "SysSettings.php";
		$settings = parse_ini_file($_POST["bbs"].'/SETTING.TXT',false,INI_SCANNER_RAW);
		foreach($caps as $index => $value){
			if (password_verify($_POST["pass"],$caps[$index][0])){
				$from = str_replace("<FROM>",$from,$caps[$index][1]);
				$id = $caps[$index][2];
				$isadmin = $caps[$index][3];
				$iscap = $caps[$index][4];
				$timeskip = $caps[$index][5];
			}
		}

		if ($isadmin){
			if (!isset($_POST["operation"])){
?>
<meta name="robots" content="noindex">
<h1>�L���b�v�����p�Ǘ��y�[�W�i�΁j</h1>
<?=$from?>����A����ɂ���<br>
<form action="/test/admin.php" method="post">
���ݑI������Ă���F<?=substr($_POST["bbs"], 3)?><input type="hidden" name="bbs" value="<?=$_POST["bbs"]?>"><br>
�X���b�h��I�����Ă݂�F<select name="thread">
<option value="">�����I�����Ȃ�</option>
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
����(optional)�F<input type="text" name="insu"><br>
�������邩�l���Ă݂�F<select name="operation" required>
<option value="">--�I�����Ă�������--</option>
<option value="0">index.html�̍Đ���</option>
<option value="1">�X���b�h�̍폜</option>
<option value="2">���X�̍폜</option>
<option value="3">subject.txt�̍Đ���</option>
</select><br>
<input type="hidden" name="pass" value="<?=$_POST["pass"]?>">
<input type="submit" value="����J�n">
</form>
<?php
			}else{
				if ($_POST["operation"] == "0"){
					if ($_POST["bbs"] != ""){
						generateHTML(substr($_POST["bbs"], 3));
					}else{
						$dir = '../';
						$list1 = glob($dir . '*', GLOB_ONLYDIR);
					
						foreach ($list1 as $dir1) {
							if (file_exists($dir1.'/SETTING.TXT')) {
								generateHTML(substr($dir1, 3));
							}
						}
					}
					echo "Operation Successful";
					exit();
				}else if ($_POST["operation"] == "1"){
					if (!isset($_POST["thread"]) || !file_exists($_POST["thread"])){
						echo "����ȃX���b�h���݂��܂���B";
						exit();
					}else{
						$dat = file($_POST["thread"]);
						$max = count($dat);
						list(,,,,$subject) = explode("<>",$dat[0]);
						if (unlink($_POST["thread"])){
							$subjecttxt = file_get_contents($_POST["bbs"]."/subject.txt");
							$subject = trim($subject2);
							$dir1 = preg_match("/\/dat\/(.*)\.dat/",$_POST["thread"],$match);
							$subjecttxt = preg_replace("/".$dir1."<>.*\n/", "", $subjecttxt);
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
						echo "����ȃX���b�h���݂��܂���B";
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
				}else if ($_POST["operation"] == "3"){
					if ($_POST["bbs"] != ""){
						$threads = array();
						$time_list = array(); //�e�t�@�C���̍X�V���t���i�[����z��
						$subjecttxt = array();

						$dir = $_POST["bbs"].'/dat/';
						$list1 = glob($dir . '*.dat');
					
						foreach ($list1 as $dir1) {
							preg_match("/\/dat\/(.*)\.dat/",$dir1,$match);
							$threads[] = $match[1].".dat";
							$time_list[] = filemtime($dir1); //�t�@�C���̍X�V���t��z��Ɋi�[����
						}
						// array_multisort('�\�[�g���s���z��','�\�[�g��','���킹�ă\�[�g���������z��');
						array_multisort($time_list,SORT_DESC,$threads); //�X�V���t�Ń\�[�g

						foreach ($threads as $file){
							$dat = file($_POST["bbs"].'/dat/'.$file);
							list(,,,,$subject) = explode("<>",$dat[0]);
							$subject = rtrim($subject);
							if (!isset($subject)||$subject == ""){
								$subject = '[�������Ă܂�]';
							}
							$subjecttxt[] = "$file<>$subject (".count($dat).")";
						}
						$sub = implode("\n",$subjecttxt);
						if ($sub != ""){
							$sub = $sub."\n";
						}
						file_put_contents($_POST["bbs"]."/subject.txt",$sub);

						generateHTML(substr($_POST["bbs"], 3));
					}else{
						$dir = '../';
						$list1 = glob($dir . '*', GLOB_ONLYDIR);
					
						foreach ($list1 as $dir1) {
							if (file_exists($dir1.'/SETTING.TXT')) {
								$threads = array();
								$time_list = array(); //�e�t�@�C���̍X�V���t���i�[����z��
								$subjecttxt = array();
		
								$dir = $dir1.'/dat/';
								$list1 = glob($dir . '*.dat');
							
								foreach ($list1 as $dir2) {
									preg_match("/\/dat\/(.*)\.dat/",$dir2,$match);
									$threads[] = $match[1].".dat";
									$time_list[] = filemtime($dir2); //�t�@�C���̍X�V���t��z��Ɋi�[����
								}
								// array_multisort('�\�[�g���s���z��','�\�[�g��','���킹�ă\�[�g���������z��');
								array_multisort($time_list,SORT_DESC,$threads); //�X�V���t�Ń\�[�g
		
								foreach ($threads as $file){
									$dat = file($dir1.'/dat/'.$file);
									list(,,,,$subject) = explode("<>",$dat[0]);
									$subject = rtrim($subject);
									if (!isset($subject)||$subject == ""){
										$subject = '[�������Ă܂�]';
									}
									$subjecttxt[] = "$file<>$subject (".count($dat).")";
								}
								$sub = implode("\n",$subjecttxt);
								if ($sub != ""){
									$sub = $sub."\n";
								}
								file_put_contents($dir1."/subject.txt",$sub);
		
								generateHTML(substr($dir1, 3));
							}
						}
					}
					echo "Operation Successful";
					exit();
				}else{
					echo "�s�������ˁ`������";
					exit();
				}
			}
		}else{
			echo '���Ȃ��̒񎦂����L���b�v�͉^�c�L���b�v�ł͓��e�ł��B�����L�O�L���b�v�B';
			exit();
		}
	}else{
?>
<meta name="robots" content="noindex">
<h1>�L���b�v�����p�Ǘ��y�[�W�i�΁j</h1>
<?=$from?>�A����ɂ���<br>
<form action="/test/admin.php" method="post">
��I�����Ă݂�F<select name="bbs">
<option value="">���ׂĂ̔�</option>
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
���O�͖{���ɃL���b�v�������H�F<input type="password" name="pass"><br>
<input type="submit" value="���O�C��">
</form>
<?php
	}
?>