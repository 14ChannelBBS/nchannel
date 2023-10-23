<?php
	ini_set("display_errors",true);
	echo password_hash($_GET["name"],PASSWORD_DEFAULT);