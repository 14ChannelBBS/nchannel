function relthread(){

	// Date�I�u�W�F�N�g���쐬
	var date = new Date() ;
	// UNIX�^�C���X�^���v���擾���� (�~���b�P��)
	var a = date.getTime() ;
	// UNIX�^�C���X�^���v���擾���� (�b�P�� - PHP��time()�Ɠ���)
	var b = Math.floor( a / 1000 ) ;
	const formElements = document.forms.form;
	formElements.time.value = b;

	let uri = location.pathname.slice(1).split('/');
	formElements.bbs.value = uri[2];
	formElements.key.value = uri[3];

	// (1) XMLHttpRequest�I�u�W�F�N�g���쐬
	const xhr = new XMLHttpRequest();

	// (2) �擾����t�@�C���̐ݒ�
	xhr.open('get', '/'+uri[2]+"/dat/"+uri[3]+".dat");
	// xhr.responseType = 'blob'; (�t�@�C���`���ɂ���Đݒ�j

	// (3) ���N�G�X�g�i�v���j�𑗐M
	xhr.send();

	xhr.onreadystatechange = function() {
		// (4) �ʐM������Ɋ����������m�F
		if( xhr.readyState === 4 && xhr.status === 200) {
			// (5) �擾�������X�|���X���y�[�W�ɕ\��
			// �����Ƀt�@�C�����e���y�[�W�ɕ\�����鏈��������
			const file_area = document.getElementById('thread');
			let thread = this.response.split("\n");
			document.getElementById('title').innerHTML = thread[0].split("<>")[4];
			document.getElementById('all').innerHTML = "(�S����"+(thread.length-1)+"�̃��X������܂�)";
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
				th += "<dt>"+(index+1)+" �F"+mailto+" �F "+time+"</dt><dd> "+message+" <br><br></dd>\n";
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
			// (1) XMLHttpRequest�I�u�W�F�N�g���쐬
			const xhr2 = new XMLHttpRequest();

			// (2) �擾����t�@�C���̐ݒ�
			xhr2.open('get', '/'+uri[2]+"/dat/"+uri[3]+".dat");
			// xhr.responseType = 'blob'; (�t�@�C���`���ɂ���Đݒ�j

			// (3) ���N�G�X�g�i�v���j�𑗐M
			xhr2.send();

			xhr2.onreadystatechange = function() {
				// (4) �ʐM������Ɋ����������m�F
				if( xhr2.readyState === 4 && xhr2.status === 200) {
					// (5) �擾�������X�|���X���y�[�W�ɕ\��
					// �����Ƀt�@�C�����e���y�[�W�ɕ\�����鏈��������
					const file_area = document.getElementById('thread');
					let thread = this.response.split("\n");
					document.getElementById('title').innerHTML = thread[0].split("<>")[4];
					document.getElementById('all').innerHTML = "(�S����"+(thread.length-1)+"�̃��X������܂�)";
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
						th += "<dt>"+(index+1)+" �F"+mailto+" �F "+time+"</dt><dd> "+message+" <br><br></dd>\n";
					});
					file_area.innerHTML = th;
				}
			};
		}
	}
	return false;
}

// HTML�t�H�[���̌`���Ƀf�[�^��ϊ�����
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
	// (1) XMLHttpRequest�I�u�W�F�N�g���쐬
	const xhr2 = new XMLHttpRequest();

	// (2) �擾����t�@�C���̐ݒ�
	xhr2.open('get', '/'+uri[2]+"/dat/"+uri[3]+".dat");
	// xhr.responseType = 'blob'; (�t�@�C���`���ɂ���Đݒ�j

	// (3) ���N�G�X�g�i�v���j�𑗐M
	xhr2.send();

	xhr2.onreadystatechange = function() {
		// (4) �ʐM������Ɋ����������m�F
		if( xhr2.readyState === 4 && xhr2.status === 200) {
			// (5) �擾�������X�|���X���y�[�W�ɕ\��
			// �����Ƀt�@�C�����e���y�[�W�ɕ\�����鏈��������
			const file_area = document.getElementById('thread');
			let thread = this.response.split("\n");
			if (document.getElementById('all').innerHTML == "(�S����"+(thread.length-1)+"�̃��X������܂�)"){
				return;
			}
			document.getElementById('title').innerHTML = thread[0].split("<>")[4];
			document.getElementById('all').innerHTML = "(�S����"+(thread.length-1)+"�̃��X������܂�)";
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
				th += "<dt>"+(index+1)+" �F"+mailto+" �F "+time+"</dt><dd> "+message+" <br><br></dd>\n";
			});
			file_area.innerHTML = th;
		}
	};
  }, 1000);