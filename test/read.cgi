<?php
    //�ݒ�
    $ver = '<b>
	<p style="margin: 0; padding: 0.25em 0; text-align: center; color: #333;">
	<a href="//14chan.cf/">14�����˂� �����I</a> READ.CGI(readmode 1) - '.date("Y/m/d H:i:s", filemtime("./1.php")).' JST <b>������</b><br></p>
	<p style="margin: 0 0 0.5em 0; text-align: center; font-size: 0.8em; color: #933;">
	Server By <!--<a href="https://osdn.net/"><img src="//osdn.net/sflogo.php?group_id=14874&amp;type=1" width="96" height="29" border="0" alt="OSDN"></a>-->OSDN. Thanks!!<br>
	</p>
	</b>';
    session_start();
    $readmode = $_GET['v'];
    $rm = $_SERVER['REQUEST_URI'];
    preg_match('/\/(\?.+)/', $rm, $rm);
    $rm = $rm[1];
    if (!isset($readmode)){
        $readmode = "1";
    }
    if (file_exists("$readmode.php")){
        require "$readmode.php";   
    }else{
        $pathinfo = $_SERVER['REQUEST_URI'];
        $pathinfo = preg_replace("/\?.*/", "", $pathinfo);
?>
<html><head>
<meta name="msapplication-square70x70logo" content="http://apple.14chan.cf/favicons/site-tile-70x70.png">
<meta name="msapplication-square150x150logo" content="http://apple.14chan.cf/favicons/site-tile-150x150.png">
<meta name="msapplication-wide310x150logo" content="http://apple.14chan.cf/favicons/site-tile-310x150.png">
<meta name="msapplication-square310x310logo" content="http://apple.14chan.cf/favicons/site-tile-310x310.png">
<meta name="msapplication-TileColor" content="#0078d7">
<link rel="shortcut icon" type="image/vnd.microsoft.icon" href="/favicon.ico">
<link rel="icon" type="image/vnd.microsoft.icon" href="/favicon.ico">
<link rel="apple-touch-icon" sizes="57x57" href="http://apple.14chan.cf/favicons/apple-touch-icon-57x57.png">
<link rel="apple-touch-icon" sizes="60x60" href="http://apple.14chan.cf/favicons/apple-touch-icon-60x60.png">
<link rel="apple-touch-icon" sizes="72x72" href="http://apple.14chan.cf/favicons/apple-touch-icon-72x72.png">
<link rel="apple-touch-icon" sizes="76x76" href="http://apple.14chan.cf/favicons/apple-touch-icon-76x76.png">
<link rel="apple-touch-icon" sizes="114x114" href="http://apple.14chan.cf/favicons/apple-touch-icon-114x114.png">
<link rel="apple-touch-icon" sizes="120x120" href="http://apple.14chan.cf/favicons/apple-touch-icon-120x120.png">
<link rel="apple-touch-icon" sizes="144x144" href="http://apple.14chan.cf/favicons/apple-touch-icon-144x144.png">
<link rel="apple-touch-icon" sizes="152x152" href="http://apple.14chan.cf/favicons/apple-touch-icon-152x152.png">
<link rel="apple-touch-icon" sizes="180x180" href="http://apple.14chan.cf/favicons/apple-touch-icon-180x180.png">
<link rel="icon" type="image/png" sizes="36x36" href="http://apple.14chan.cf/favicons/android-chrome-36x36.png">
<link rel="icon" type="image/png" sizes="48x48" href="http://apple.14chan.cf/favicons/android-chrome-48x48.png">
<link rel="icon" type="image/png" sizes="72x72" href="http://apple.14chan.cf/favicons/android-chrome-72x72.png">
<link rel="icon" type="image/png" sizes="96x96" href="http://apple.14chan.cf/favicons/android-chrome-96x96.png">
<link rel="icon" type="image/png" sizes="128x128" href="http://apple.14chan.cf/favicons/android-chrome-128x128.png">
<link rel="icon" type="image/png" sizes="144x144" href="http://apple.14chan.cf/favicons/android-chrome-144x144.png">
<link rel="icon" type="image/png" sizes="152x152" href="http://apple.14chan.cf/favicons/android-chrome-152x152.png">
<link rel="icon" type="image/png" sizes="192x192" href="http://apple.14chan.cf/favicons/android-chrome-192x192.png">
<link rel="icon" type="image/png" sizes="256x256" href="http://apple.14chan.cf/favicons/android-chrome-256x256.png">
<link rel="icon" type="image/png" sizes="384x384" href="http://apple.14chan.cf/favicons/android-chrome-384x384.png">
<link rel="icon" type="image/png" sizes="512x512" href="http://apple.14chan.cf/favicons/android-chrome-512x512.png">
<link rel="icon" type="image/png" sizes="36x36" href="http://apple.14chan.cf/favicons/icon-36x36.png">
<link rel="icon" type="image/png" sizes="48x48" href="http://apple.14chan.cf/favicons/icon-48x48.png">
<link rel="icon" type="image/png" sizes="72x72" href="http://apple.14chan.cf/favicons/icon-72x72.png">
<link rel="icon" type="image/png" sizes="96x96" href="http://apple.14chan.cf/favicons/icon-96x96.png">
<link rel="icon" type="image/png" sizes="128x128" href="http://apple.14chan.cf/favicons/icon-128x128.png">
<link rel="icon" type="image/png" sizes="144x144" href="http://apple.14chan.cf/favicons/icon-144x144.png">
<link rel="icon" type="image/png" sizes="152x152" href="http://apple.14chan.cf/favicons/icon-152x152.png">
<link rel="icon" type="image/png" sizes="160x160" href="http://apple.14chan.cf/favicons/icon-160x160.png">
<link rel="icon" type="image/png" sizes="192x192" href="http://apple.14chan.cf/favicons/icon-192x192.png">
<link rel="icon" type="image/png" sizes="196x196" href="http://apple.14chan.cf/favicons/icon-196x196.png">
<link rel="icon" type="image/png" sizes="256x256" href="http://apple.14chan.cf/favicons/icon-256x256.png">
<link rel="icon" type="image/png" sizes="384x384" href="http://apple.14chan.cf/favicons/icon-384x384.png">
<link rel="icon" type="image/png" sizes="512x512" href="http://apple.14chan.cf/favicons/icon-512x512.png">
<link rel="icon" type="image/png" sizes="16x16" href="http://apple.14chan.cf/favicons/icon-16x16.png">
<link rel="icon" type="image/png" sizes="24x24" href="http://apple.14chan.cf/favicons/icon-24x24.png">
<link rel="icon" type="image/png" sizes="32x32" href="http://apple.14chan.cf/favicons/icon-32x32.png">
<link rel="manifest" href="http://apple.14chan.cf/favicons/manifest.json">
</head><body bgcolor="#EFEFEF">
<title>�d�q�q�n�q�I</title>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<font size="+1" color="#FF0000"><b>ERROR: read.cgi�̃o�[�W�����w�肪�Ԉ���Ă��܂��I</b></font><br>
<br>
<hr>
<font size="+1" color="#00AA00"><b>�G���[�̌�����������Ȃ��H</b></font>
<ul style="line-height:1.5;">
�܂��m�F���悤�I<br>
�q���g:read.cgi�̃o�[�W�����Ԉ���Ă܂���<br>
<b>
<!--�s<a href="//info.5ch.net/?curid=686">�������߂Ȃ����̑����\</a>�t<br>-->
�s<a href="http://apple.14chan.cf/">�ITOP�֖߂�</a>�t<br>
�s<a href="http://apple.14chan.cf<?=$pathinfo?>">���T���̃y�[�W�͂���������...</a>�t<br>
</b>
</ul><!--<br>
<font size="+1" color="#DD00DD"><b>���������ăA�N�Z�X�K���ł����H</b></font>
<ul style="line-height:1.5;">
���g���̃v���o�C�_���񂪁A<b>�����ƂȂ����l�ɑΉ�</b>����܂ŋK���͑����܂��B<br>
�ʂ̑Ή��E�i�W�ɂ��ẮA�v���o�C�_����ւ��q�˂��������B<br>
<small>���̑��A14�����˂�ɂ��ẮA
<a href="//5ch.net/qa/">���S�҂̎���</a>
<a href="//5ch.net/accuse/">�ᔻ�v�]</a>
<a href="//5ch.net/operate/">�^�p���</a>
<a href="//5ch.net/operatex/">�^�p�Վ�</a>
�Ȃǂւǂ����B</small>
</ul><br>
<font size="+1" color="#DD3300"><b>�� �Q�l�ɂ���</b></font>
<ul style="line-height:1.5;">
�Q�l�𓱓����邱�ƂŋK�����ɘa����܂��B<br>
�Q�l�̍w���� <a href="//premium.5ch.net/">������</a> ����<br>
���ɘQ�l���������Ȃ� <a href="//login.5ch.net/login.php">���O�C��</a> ���邱�ƂŗL���ɂȂ�܂��B <br>
</ul>
    -->
</body></html>
<?php
    }