<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8">
	<title>Fael</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<form class="form-login" method="POST" action="processa_polo.php">
		<h1>Cadastro de Polo</h1>
		<label class="label">Nome: </label>
		<input type="text" name="nome"><br><br>
		<label class="label">Email: </label>
		<input type="email" name="email"><br><br>
		<label class="label">Estado:</label>
		<input type="text" name="estado"><br><br>
		<label class="label">Cidade:</label>
		<input type="text" name="cidade"><br><br>
		<label class="label">CEP:</label>
		<input type="text" name="cep"><br><br>
		<input type="submit" value="Cadastrar"><br><br>
		<input type="button" value="Voltar" onclick="history.go(-1)">
	</form>
</body>
</html>