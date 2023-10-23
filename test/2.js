function relthread(){

	// Dateオブジェクトを作成
	var date = new Date() ;
	// UNIXタイムスタンプを取得する (ミリ秒単位)
	var a = date.getTime() ;
	// UNIXタイムスタンプを取得する (秒単位 - PHPのtime()と同じ)
	var b = Math.floor( a / 1000 ) ;
	const formElements = document.forms.form;
	formElements.time.value = b;

	let uri = location.pathname.slice(1).split('/');
	formElements.bbs.value = uri[2];
	formElements.key.value = uri[3];

	// (1) XMLHttpRequestオブジェクトを作成
	const xhr = new XMLHttpRequest();

	// (2) 取得するファイルの設定
	xhr.open('get', '/'+uri[2]+"/dat/"+uri[3]+".dat");
	// xhr.responseType = 'blob'; (ファイル形式によって設定）

	// (3) リクエスト（要求）を送信
	xhr.send();

	xhr.onreadystatechange = function() {
		// (4) 通信が正常に完了したか確認
		if( xhr.readyState === 4 && xhr.status === 200) {
			// (5) 取得したレスポンスをページに表示
			// ここにファイル内容をページに表示する処理が入る
			const file_area = document.getElementById('thread');
			let thread = this.response.split("\n");
			document.getElementById('title').innerHTML = thread[0].split("<>")[4];
			document.getElementById('all').innerHTML = "(全部で"+(thread.length-1)+"のレスがあります)";
			document.title = thread[0].split("<>")[4] + " - 14Channel BBS";
			let th = "";
			thread.some(function(elem, index) {
				if (index == (thread.length-1)){
					return true;
				}
				var res = elem.split('<>');
				var mailto = "";
				var time = res[2];
				var message = res[3];
				if (res[1] == "") {
					mailto = "<span style=\"color: green;\"><b>"+res[0]+"</b></span>";
				}else{
					mailto = "<a href=\"mailto:"+res[1]+"\"><span style=\"color: green;\"><b>"+res[0]+"</b></span></a>";
				}
				th += "<dt>"+(index+1)+" ："+mailto+" ： "+time+"</dt><dd> "+message+" <br><br></dd>\n";
			});
			file_area.innerHTML = th;
		}
	};
}

function kakikomi() {
	const formElements = document.forms.form;
	let FROM = formElements.FROM.value;
	let mail = formElements.mail.value;
	let MESSAGE = formElements.MESSAGE.value;
	let bbs = formElements.bbs.value;
	let key = formElements.key.value;
	let time = formElements.time.value;
	let data = {"FROM": FROM, "mail": mail, "MESSAGE": MESSAGE, "bbs": bbs, "key": key, "time": time};
	//'FROM='+FROM+"&mail="+mail+"&MESSAGE="+MESSAGE+"&bbs="+bbs+"&key="+key+"&time="+time

	var xhr = new XMLHttpRequest();
	xhr.open('POST', '/test/bbs.cgi');
	xhr.setRequestHeader( 'Content-Type', 'application/x-www-form-urlencoded; charset=Shift-JIS' );
	xhr.send(EncodeHTMLForm(data));
	xhr.onreadystatechange = function() {

		if(xhr.readyState === 4 && xhr.status === 200) {
			console.log( xhr.response );
			formElements.MESSAGE.value = "";
			let uri = location.pathname.slice(1).split('/');
			// (1) XMLHttpRequestオブジェクトを作成
			const xhr2 = new XMLHttpRequest();

			// (2) 取得するファイルの設定
			xhr2.open('get', '/'+uri[2]+"/dat/"+uri[3]+".dat");
			// xhr.responseType = 'blob'; (ファイル形式によって設定）

			// (3) リクエスト（要求）を送信
			xhr2.send();

			xhr2.onreadystatechange = function() {
				// (4) 通信が正常に完了したか確認
				if( xhr2.readyState === 4 && xhr2.status === 200) {
					// (5) 取得したレスポンスをページに表示
					// ここにファイル内容をページに表示する処理が入る
					const file_area = document.getElementById('thread');
					let thread = this.response.split("\n");
					document.getElementById('title').innerHTML = thread[0].split("<>")[4];
					document.getElementById('all').innerHTML = "(全部で"+(thread.length-1)+"のレスがあります)";
					let th = "";
					thread.some(function(elem, index) {
						if (index == (thread.length-1)){
							return true;
						}
						var res = elem.split('<>');
						var mailto = "";
						var time = res[2];
						var message = res[3];
						if (res[1] == "") {
							mailto = "<span style=\"color: green;\"><b>"+res[0]+"</b></span>";
						}else{
							mailto = "<a href=\"mailto:"+res[1]+"\"><span style=\"color: green;\"><b>"+res[0]+"</b></span></a>";
						}
						th += "<dt>"+(index+1)+" ："+mailto+" ： "+time+"</dt><dd> "+message+" <br><br></dd>\n";
					});
					file_area.innerHTML = th;
				}
			};
		}
	}
	return false;
}

// HTMLフォームの形式にデータを変換する
function EncodeHTMLForm( data )
{
    var params = [];

    for( var name in data )
    {
        var value = data[ name ];
        var param = EscapeSJIS( name ) + '=' + EscapeSJIS( value );

        params.push( param );
    }

    return params.join( '&' ).replace( /%20/g, '+' );
}

  //window.addEventListener('DOMContentLoaded', relthread());
  window.addEventListener('load', relthread());
  var intervalId = setInterval(function(){
	let uri = location.pathname.slice(1).split('/');
	// (1) XMLHttpRequestオブジェクトを作成
	const xhr2 = new XMLHttpRequest();

	// (2) 取得するファイルの設定
	xhr2.open('get', '/'+uri[2]+"/dat/"+uri[3]+".dat");
	// xhr.responseType = 'blob'; (ファイル形式によって設定）

	// (3) リクエスト（要求）を送信
	xhr2.send();

	xhr2.onreadystatechange = function() {
		// (4) 通信が正常に完了したか確認
		if( xhr2.readyState === 4 && xhr2.status === 200) {
			// (5) 取得したレスポンスをページに表示
			// ここにファイル内容をページに表示する処理が入る
			const file_area = document.getElementById('thread');
			let thread = this.response.split("\n");
			if (document.getElementById('all').innerHTML == "(全部で"+(thread.length-1)+"のレスがあります)"){
				return;
			}
			document.getElementById('title').innerHTML = thread[0].split("<>")[4];
			document.getElementById('all').innerHTML = "(全部で"+(thread.length-1)+"のレスがあります)";
			document.title = thread[0].split("<>")[4] + " - 14Channel BBS";
			let th = "";
			thread.some(function(elem, index) {
				if (index == (thread.length-1)){
					return true;
				}
				var res = elem.split('<>');
				var mailto = "";
				var time = res[2];
				var message = res[3];
				if (res[1] == "") {
					mailto = "<span style=\"color: green;\"><b>"+res[0]+"</b></span>";
				}else{
					mailto = "<a href=\"mailto:"+res[1]+"\"><span style=\"color: green;\"><b>"+res[0]+"</b></span></a>";
				}
				th += "<dt>"+(index+1)+" ："+mailto+" ： "+time+"</dt><dd> "+message+" <br><br></dd>\n";
			});
			file_area.innerHTML = th;
		}
	};
  }, 1000);