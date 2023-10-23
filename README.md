# nchannel
> 私のスパゲッティーソースでも、掲示板は動くんですよ... - nennneko5787

このスクリプトは[14Channel BBS(https://apple.14chan.cf/)](https://apple.14chan.cf/)で使われているものらしいですよ。
## How to Install
### Require
> 詳しい環境については[こちらのページ(https://apple.14chan.cf/test/phpinfo.php)](https://apple.14chan.cf/test/phpinfo.php)からバージョンを確認してください。
- PHP Version 5.6.40-0+deb8u12以上
- Server API→Apache 2.0 Handler
- sendmailが使える環境(使えなくてもおｋ)
- curlが使える環境
### procedure
①まず、このリポジトリの内容をどうにかしてサーバーにぶち込みます。  
②次に、readmeフォルダに有るSysSettings.phpをいじってtestフォルダにぶち込みます。  
③次に、testフォルダに有るplainフォルダを一番上の階層へぶち込んで、SETTING.TXTの中身をいじりまくります。  
④最後に、/test/admin.phpにアクセスして、②で設定したキャップでログインして、何をするか考えてみる：の横にあるところでindex.htmlの再生成を選択肢、操作開始をクリック。  
  
この手順で多分板ができます。あとは③と④を繰り返して板を増やしまくりましょう。