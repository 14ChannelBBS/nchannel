<?php
	require "SysSettings.php";
	echo openssl_encrypt($_GET["str"], 'AES-256-CBC', $encrypt_key, 0, $encrypt_iv);
?>