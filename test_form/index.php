<?php
	session_start();
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device.width, initial-scale=1.0">
	<title>Fael</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div class="container">
		<form class="form-signin" method="POST" action="valida.php">
			<h1>Faça seu login</h1>
			<label for="inputEmail" class="sr-only">Email</label><br>
			<input type="email" name="email" id="inputemail" class="form-control" required autofocus><br><br>
			<label for="inputPassword" class="sr-only">Senha</label><br>
			<input type="password" name="senha" id="inputpassword" class="form-control" required><br><br>
			<button class="btn btn-lg btn-danger btn-block" type="submit">Acessar</button>
		</form>
		<p class="text-center text-danger">
			<?php if(isset($_SESSION['loginErro'])){
				echo $_SESSION['loginErro'];
				unset($_SESSION['loginErro']);
			}
			?>
		</p>
	</div>	
</body>
</html>