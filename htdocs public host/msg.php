<?php
ini_set('session.cookie_lifetime', 600);
ini_set('session.gc-maxlifetime', 600);
session_start();
header('Access-Control-Allow-Origin: *');
$out = array();
$value = "python chat.py ".$_GET['msg'];
$command = escapeshellcmd($value);
$output = exec($command,$out,$result);
$a=0;
foreach($out as $line) {	
    echo $line."\n"; 
}
?>