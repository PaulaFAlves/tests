<?php

include_once("conexao.php"); 

$s = "SELECT * FROM cadastra_polos";
$relatorio = mysqli_query($conn, $s);

echo "Relatorio de Polos" . "<hr><br>";
while($dados = mysqli_fetch_assoc($relatorio)){
	echo $dados['codigo'] . "<br>";
	echo $dados['nome'] . "<br>";
	echo $dados['email'] . "<br>";
	echo $dados['cidade'] . "<br>";
	echo $dados['estado'] . "<br>";
	echo $dados['cep'] . "<hr>";
};

?>