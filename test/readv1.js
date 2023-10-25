  function selectFile() {
    if (document.getElementById("file").value === "") {
      console.log("選択しなさい");
    }
    else {
		const form = document.forms[1];
	  	const fd = new FormData(form);
	 	const xhr = new XMLHttpRequest();
	 	xhr.open("POST", "/upload/upload.php");
		// (2) ファイルが選択されたときに処理を実行するようイベントリスナーに登録
		// (3) 選択したファイルをFormDataオブジェクトにセット

		// (4) ファイル送信
		xhr.send(fd);

		// (5) 通信が完了したらレスポンスをコンソールに出力する
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