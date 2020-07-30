<!DOCTYPE HTML>
<html>
<body>
<?php
ini_set('session.cookie_lifetime', 600);
ini_set('session.gc-maxlifetime', 600);
session_start();
header('Access-Control-Allow-Origin: *');
$_SESSION['s_email'] = $_POST['mailid']; 
$_SESSION['s_name'] = $_POST['name']; 
$_SESSION['s_phone']=$_POST['cno'];
include("DBConnection.php"); 

if ($_SERVER['REQUEST_METHOD'] == 'POST')
{ 
$inName =mysqli_real_escape_string($db, $_POST["name"]);
$inEmail =mysqli_real_escape_string($db, $_POST["mailid"]);
$incno =mysqli_real_escape_string($db, $_POST["cno"]);

$stmt = $db->prepare("INSERT INTO usr(usr_name, usr_phone, usr_email, date_time) VALUES(?, ?, ?, NOW())"); 
$stmt->bind_param("sss", $inName, $incno, $inEmail);
$stmt->execute();
$result = $stmt->affected_rows;
$stmt -> close();
$db -> close();       
}
?>
</body> 
</html>