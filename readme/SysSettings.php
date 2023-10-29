<?php
	$caps = array();
	$caps[0] = array("キャップのキー(hashapassword.phpで生成)","名前(<FROM>で名前に変換)","ID",isadmin(そのキャップはadmin.phpでログインできるか),iscap(そのキャップはキャップしか書けない板で書けるか),timeskip(連投規制にかからなくなるか))
	// Cloudflare turnstile( https://www.cloudflare.com/ja-jp/products/turnstile/ )のサイトキーとシークレット
	$sitekey = '';
	$turnstile_secret = '';
	// レスでメールのメールアドレス暗号化用keyとiv
	$encrypt_key = "指定しろ";
	$encrypt_iv = "絶対に";
?>