<?php

include_once("conexao.php"); 

$s = "SELECT * FROM cadastra_disciplinas";
$relatorio = mysqli_query($conn, $s);

echo "Relatorio de Disciplinas" . "<hr><br>";
while($dados = mysqli_fetch_assoc($relatorio)){
	echo $dados['codigo'] . "<br>";
	echo $dados['disciplina'] . "<br>";
	echo $dados['curso'] . "<hr>";
};

?>