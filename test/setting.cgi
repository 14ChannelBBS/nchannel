<?php
	if (isset($_POST["require"])){
		setcookie("software", $_POST["software"], (time()+60*60*24*(365*10)),"/");
		setcookie("character", $_POST["character"], (time()+60*60*24*(365*10)),"/");
	}
?>
<html><head>
<title>14ch設定ページ</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script type="text/javascript" src="/lib/common/common.v49.js?"></script>
<script type="text/javascript" src="/lib/setting.js/setting.v7.js?200130_v11697710659"></script>
<style>
input,select{font-size:12pt}
.inner{margin-left:10px}
.bar{width:100%;display:table;background:#FFEEEE;margin-top:3px;pading:5px}
form{margin-bottom:5px;padding:0px}
.word{
	color:#555;
	background:#f5f5f5;
	border-radius:3px;
	border:1px solid #eee;
	padding:1px;
	font-size:9pt;display:inline-block;
	width:100px
}
</style>
<style>
body {font-family: sans-serif;}
</style>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
</head>

<body style="background-color: #EFEFEF;">
<div class="notice" style="position:fixed;top:0px;left:0px;width:100%;z-index:1000"></div>
<div style="background:#000033;color:white;padding:3px;display:table;width:100%">
<div style="float:left;padding:3px">
<img src="/image/icon/svg/setting_white.svg" width="14" height="14"> <b>14ch設定</b>
</div>
</div>
<?php
	if (isset($_POST["require"])){
		echo '<div class="alert alert-success" role="alert">
		設定がセーブされました！
	  </div>';
	}
?>
<div style="padding:4px">
いろいろな個別設定をするページ
</div>
<a href="/<?=$_GET["bbs"]?>" style="color:blue">板に戻る</a>
<style>
.hide{display:none}

.list{max-height:200px;overflow-y:scroll;display:inline-block;padding-right:30px}
.bar_main{background:#5555AA;color:white;margin-top:15px}
.bar_sub{background:#eee;font-size:9pt;padding:4px;margin-bottom:10px}
.inner{margin-left:5px;margin-bottom:30px}

.detail{
	font-size:9pt;
	background:#ffe;
	padding:3px;
	display:inline-block;
	border-radius:2px;
	border:1px solid #ddd;
	margin:3px
}

.info{
	margin-left:5px;
	display:inline-block;
	background:#f9f9f9;
	font-size:9pt;
	color:#999
}

.item{
	margin-bottom:10px;
	border-bottom:2px dotted #f5f5f5;
}

</style>
<style type="text/css">
/* The switch - the box around the slider */
.switch {
	margin:3px;
  position: relative;
  display: inline-block;
  width: 45px;
  height: 24px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(18px);
  -ms-transform: translateX(18px);
  transform: translateX(18px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}

</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
<form action="/test/setting.cgi?bbs=<?=$_GET["bbs"]?>" method="post">
<div class="bar_main" style="background:#003300;color:white">■読み上げ関連</div>
<div class="inner">

<div class="item">
<t>ソフトウェア</t>：
<select name="software" class="setting">
<?php
	if ($_COOKIE["software"] == "voicevox"){
		echo '<option value="">OS標準</option>
		<option value="voicevox" selected>VOICEVOX</option>';
	}else{
		echo '<option value="">OS標準</option>
		<option value="voicevox">VOICEVOX</option>';
	}
?>
</select>
<div>
<div class="detail">
<b>※OS標準</b>…WindowsだとMicrosoft Harukaに。<br>
<b>VOICEVOX</b>…下のキャラクター選択画面で選んだキャラクターの声に。<br>
</div>
</div>
</div>

<div class="item">
<t>キャラクター</t>：
<select name="character" class="setting" required>
<option value="">選択してください</option>
<?php
$url = "https://static.tts.quest/voicevox_speakers.json";
$ch = curl_init(); // はじめ

//オプション
curl_setopt($ch, CURLOPT_URL, $url); 
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);  
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);  
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$html = curl_exec($ch);
$json = json_decode($html,true,JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
$err = curl_error($ch);
curl_close($ch); //終了
foreach ($json as $index => $speaker)
	if ($_COOKIE["character"] == $index){
		echo '<option value="'.$index.'" selected>'.mb_convert_encoding(str_replace("VOICEVOX:","",$speaker),"Shift-JIS","auto").'</option>';
	}else{
		echo '<option value="'.$index.'">'.mb_convert_encoding(str_replace("VOICEVOX:","",$speaker),"Shift-JIS","auto").'</option>';
	}
?>
</select>
<div>
<div class="detail">
<b>require</b>…ソフトウェア=VOICEVOX<br>
<b>CURLエラーメッセージ</b>…<?=$err?><br>
<b>※↑に何も表示されていない場合</b>…正常にキャラクター一覧が取得できた。<br>
<b>それ以外</b>…もう一度再読み込みをお願いします。<br>
</div>
</div>
</div>

<div style="position:fixed; right:50px; bottom:50px;">
<input style="border-style: solid; width:100px; height:50px;" type="submit" value="保存">
</div>
<input type="hidden" name="require" value="require">
</form>
<style>.syoicon{margin:3px;user-select: none;border:1px solid #DDD;border-radius:3px;color:#555;cursor:pointer;background:#ddd;width:200px;text-align:center;font-size:10pt;padding:2px}</style><style>.audio{cursor:pointer}.audio{background-image: url("//image.open2ch.net/lib/web-audio-recorder-js/play.svg")}.audio.playing{background-image: url("//image.open2ch.net/lib/web-audio-recorder-js/pause.svg")}</style><style>.spin { animation: spin 2s linear infinite;}@keyframes spin {0% {transform: rotate(0deg);} 100% {transform: rotate(360deg);}}</style><div style="display:none" id="youtube_player"><iframe id="player_iframe" src="" frameborder="0" allowfullscreen=""></iframe><div style="text-align:center;margin-top:3px"><input id="overlay_closeButton" type="button" value="Close"></div></div><div id="overlay" style="display:none"></div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
</body></html>