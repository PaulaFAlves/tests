<?php

include_once("conexao.php"); 

$s = "SELECT * FROM cadastra_alunos";
$relatorio = mysqli_query($conn, $s);

echo "Relatorio de Alunos" . "<hr><br>";
while($dados = mysqli_fetch_assoc($relatorio)){
	echo $dados['codigo'] . "<br>";
	echo $dados['nome'] . "<br>";
	echo $dados['sobrenome'] . "<br>";
	echo $dados['nascimento'] . "<br>";
	echo $dados['cidade'] . "<br>";
	echo $dados['estado'] . "<hr>";
};

?>