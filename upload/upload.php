<?php

const FILE_FOL = "./";

//�ϐ��̏�����
    $check = null;
    $newfilename = null;
    $msg = null;

//���t�@�C�����̐擪�ɃA�b�v���[�h������������

    $ext = pathinfo($_FILES["file"]["name"], PATHINFO_EXTENSION);
    $newfilename = date("YmdHis").mt_rand().".".$ext;

// �t�@�C�����A�b�v�f�[�g���ꂽ���𒲂ׂ�
    if(is_uploaded_file($_FILES["file"]["tmp_name"])) {
        $check = 1;
    } else {
        $check = 0;
        $msg = "�t�@�C�����I������Ă��܂���B";
    }
	$file_pass = $_FILES["file"]["tmp_name"];
//��O������S�ăN���A������t�@�C�����A�b�v����
    if ($check == 1) {
      if (move_uploaded_file($file_pass, FILE_FOL.$newfilename)) {
        chmod(FILE_FOL. $_FILES["file"]["name"], 0644);
        print "https://apple.14chan.cf/upload/".$newfilename;
      } else {
        print "�t�@�C�����A�b�v���[�h�ł��܂���ł����B";
      }
    } else {
    print $msg;
    }
?>