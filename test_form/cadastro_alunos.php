<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8">
	<title>Fael</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<form class="form-login" method="POST" action="processa_aluno.php">
		<h1>Cadastro de Aluno</h1>
		<label class="label">Nome: </label>
		<input type="text" name="nome"><br><br>
		<label class="label">Sobrenome: </label>
		<input type="text" name="sobrenome"><br><br>
		<label class="label">Nascimento:</label>
		<input type="text" name="nascimento"><br><br>
		<label class="label">Cidade:</label>
		<input type="text" name="cidade"><br><br>
		<label class="label">Estado:</label>
		<input type="text" name="estado"><br><br>
		<input type="submit" value="Cadastrar"><br><br>
		<input type="button" value="Voltar" onclick="history.go(-1)">
	</form>
</body>
</html>