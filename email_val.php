<!DOCTYPE html>
<html>
<head>
</head>
<body>

<form name="myForm" action="" method="post">
Email: <input name="email" type="email">
<input type="submit" value="Submit">
</form>

</body>
</html>


<?php
$email = $_POST['email'];

if (!filter_var($email, FILTER_VALIDATE_EMAIL) === false) {
  echo("$email is a valid email address");
} else {
  echo("$email is not a valid email address");
}
?>