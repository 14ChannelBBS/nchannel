  function selectFile() {
    if (document.getElementById("file").value === "") {
      console.log("�I�����Ȃ���");
    }
    else {
		const form = document.forms[1];
	  	const fd = new FormData(form);
	 	const xhr = new XMLHttpRequest();
	 	xhr.open("POST", "/upload/upload.php");
		// (2) �t�@�C�����I�����ꂽ�Ƃ��ɏ��������s����悤�C�x���g���X�i�[�ɓo�^
		// (3) �I�������t�@�C����FormData�I�u�W�F�N�g�ɃZ�b�g

		// (4) �t�@�C�����M
		xhr.send(fd);

		// (5) �ʐM�����������烌�X�|���X���R���\�[���ɏo�͂���
		xhr.addEventListener('readystatechange', () => {

			if( xhr.readyState === 4 && xhr.status === 200) {
				console.log(xhr.response);
				let element = document.getElementById('MESSAGE');
				element.value = element.value+"\n"+xhr.response
			}
			document.getElementById("File").value = ""
		});
    }
  }