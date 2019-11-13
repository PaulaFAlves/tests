<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8">
	<title>Fael</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<form class="form-login" method="POST" action="processa_disciplina.php">
		<h1>Cadastro de Disciplina</h1>
		<label class="label">Disciplina: </label>
		<input type="text" name="disciplina"><br><br>
		<label class="label">Curso: </label>
		<input type="text" name="curso"><br><br>
		<input type="submit" value="Cadastrar"><br><br>
		<input type="button" value="Voltar" onclick="history.go(-1)">
	</form>
</body>
</html>