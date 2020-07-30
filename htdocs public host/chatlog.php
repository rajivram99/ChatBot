<!DOCTYPE HTML>
<html>
<body>
<?php
ini_set('session.cookie_lifetime', 600);
ini_set('session.gc-maxlifetime', 600);
session_start();
header('Access-Control-Allow-Origin: *');
include("DBConnection.php");

if ($_SERVER['REQUEST_METHOD'] == 'POST')
{ 
$email=$_SESSION['s_email'];
$name=$_SESSION['s_name'];
$phone=$_SESSION['s_phone'];
$type= $_POST["type"];

if ($type == 'self') {
    $id='usr_query';
}
else{
    $id='bot_response';
}

$query =mysqli_real_escape_string($db, $_POST["msg"])."\n";
$stmt = $db->prepare("UPDATE usr SET ?=CONCAT(?,?),date_time=NOW() WHERE usr_email= ? AND usr_name= ? AND usr_phone= ?");
$stmt->bind_param("ssssss",$id,$id,$query,$email,$name,$phone);
$stmt->execute();
$result = $stmt->affected_rows;
$stmt -> close();
$db -> close(); 

}
?>
</body> 
</html>    