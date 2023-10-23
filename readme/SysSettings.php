<?php
	$caps = array();
	$caps[0] = array("キャップのキー(hashapassword.phpで生成)","名前(<FROM>で名前に変換)","ID",iscap(そのキャップは運営としての能力を有するか),timeskip(連投規制にかからなくなるか))
	// Cloudflare turnstile( https://www.cloudflare.com/ja-jp/products/turnstile/ )のサイトキーとシークレット
	$sitekey = '';
	$secret = '';
	// レスでメールのメールアドレス暗号化用keyとiv
	$encrypt_key = "指定しろ";
	$encrypt_iv = "絶対に";
?>