<?php
// �{��
$message = "Line 1\r\nLine 2\r\nLine 3";

// 1 �s�� 70 �����𒴂���ꍇ�̂��߁Awordwrap() ��p����
$message = wordwrap($message, 70, "\r\n");

// ���M����
if (mail('nennneko5787@gmail.com', 'My Subject', $message) == true){
	echo "true";
}else{
	echo "��";
}
?>