const f = document.getElementById('file');
f.addEventListener('change', (evt) => {
  const fileIn = evt.target;
  const form = document.getElementById('form1');
  const fd = new FormData(form);
  const MESSAGE = document.getElementById('MESSAGE');
  const xhr = new XMLHttpRequest()

  xhr.open("POST", "/upload/upload.php");

  // アップロード関連イベント
  xhr.upload.addEventListener('loadstart', (evt) => {
	// アップロード開始
  });
  
  xhr.upload.addEventListener('progress', (evt) => {
	// アップロード進行パーセント
	const percent = (evt.loaded / evt.total * 100).toFixed(1);
	console.log(`++ xhr.upload: progress ${percent}%`);
  });
  
  xhr.upload.addEventListener('abort', (evt) => {
	// アップロード中断
	console.log('++ xhr.upload: abort (Upload aborted)');
  });
  
  xhr.upload.addEventListener('error', (evt) => {
	// アップロードエラー
	console.log('++ xhr.upload: error (Upload failed)');
  });
  
  xhr.upload.addEventListener('load', (evt) => {
	// アップロード正常終了
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
	// アップロードタイムアウト
	console.log('++ xhr.upload: timeout');
  });
  
  xhr.upload.addEventListener('loadend', (evt) => {
	// アップロード終了 (エラー・正常終了両方)
	console.log('++ xhr.upload: loadend (Upload Finished)');
  });
  
  xhr.send(fd);
});

$(function(){
	// ファイル貼り付け
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