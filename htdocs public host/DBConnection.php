<?php
ini_set('session.cookie_lifetime', 600);
ini_set('session.gc-maxlifetime', 600);
session_start();
header('Access-Control-Allow-Origin: *');
define('DB_SERVER', '10.10.226.79');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', 'root');
define('DB_DATABASE', 'chat_usr'); 
$db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
?>
