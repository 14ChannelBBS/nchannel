<?php

const FILE_FOL = "./";

//変数の初期化
    $check = null;
    $newfilename = null;
    $msg = null;

//元ファイル名の先頭にアップロード日時を加える

    $ext = pathinfo($_FILES["file"]["name"], PATHINFO_EXTENSION);
    $newfilename = date("YmdHis").mt_rand().".".$ext;

// ファイルがアップデートされたかを調べる
    if(is_uploaded_file($_FILES["file"]["tmp_name"])) {
        $check = 1;
    } else {
        $check = 0;
        $msg = "ファイルが選択されていません。";
    }
	$file_pass = $_FILES["file"]["tmp_name"];
//例外処理を全てクリアしたらファイルをアップする
    if ($check == 1) {
      if (move_uploaded_file($file_pass, FILE_FOL.$newfilename)) {
        chmod(FILE_FOL. $_FILES["file"]["name"], 0644);
        print "https://apple.14chan.cf/upload/".$newfilename;
      } else {
        print "ファイルをアップロードできませんでした。";
      }
    } else {
    print $msg;
    }
?>