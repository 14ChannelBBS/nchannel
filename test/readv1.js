const f = document.getElementById('file');
f.addEventListener('change', (evt) => {
  const fileIn = evt.target;
  const form = document.getElementById('form1');
  const fd = new FormData(form);
  const MESSAGE = document.getElementById('MESSAGE');
  const xhr = new XMLHttpRequest()

  xhr.open("POST", "/upload/upload.php");

  // �A�b�v���[�h�֘A�C�x���g
  xhr.upload.addEventListener('loadstart', (evt) => {
	// �A�b�v���[�h�J�n
  });
  
  xhr.upload.addEventListener('progress', (evt) => {
	// �A�b�v���[�h�i�s�p�[�Z���g
	const percent = (evt.loaded / evt.total * 100).toFixed(1);
	console.log(`++ xhr.upload: progress ${percent}%`);
  });
  
  xhr.upload.addEventListener('abort', (evt) => {
	// �A�b�v���[�h���f
	console.log('++ xhr.upload: abort (Upload aborted)');
  });
  
  xhr.upload.addEventListener('error', (evt) => {
	// �A�b�v���[�h�G���[
	console.log('++ xhr.upload: error (Upload failed)');
  });
  
  xhr.upload.addEventListener('load', (evt) => {
	// �A�b�v���[�h����I��
	console.log('++ xhr.upload: load (Upload Completed Successfully)');
		// Basic Events
		xhr.addEventListener('load', (evt) => {
			console.log('** xhr: load');
			const response = xhr.response;
			MESSAGE.value = MESSAGE.value+"\n"+response;
			console.log(response);
			form.file.value = "";
		})
	});
  
  xhr.upload.addEventListener('timeout', (evt) => {
	// �A�b�v���[�h�^�C���A�E�g
	console.log('++ xhr.upload: timeout');
  });
  
  xhr.upload.addEventListener('loadend', (evt) => {
	// �A�b�v���[�h�I�� (�G���[�E����I������)
	console.log('++ xhr.upload: loadend (Upload Finished)');
  });
  
  xhr.send(fd);
});

$(function(){
	// �t�@�C���\��t��
	$('textarea').inlineattachment({
	  uploadUrl: '/upload/upload.php',
	  allowedTypes: ['*'],
	  remoteFilename: (file)=>{return file.name},
	  urlText: (filename)=>{
		return `${filename}`
	  }
	});
	$('textarea').on('dragenter dragover', function() {
	  $(this).addClass('dragover')
	})
	$('textarea').on('drop dragleave dragend', function() {
	  $(this).removeClass('dragover')
	})
  });