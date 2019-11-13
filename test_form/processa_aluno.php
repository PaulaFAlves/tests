<?php

include_once("conexao.php"); 

$codigo = filter_input(INPUT_POST, 'codigo', FILTER_SANITIZE_STRING);
$nome = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_STRING);
$sobrenome = filter_input(INPUT_POST, 'sobrenome', FILTER_SANITIZE_STRING);
$nascimento = filter_input(INPUT_POST, 'nascimento', FILTER_SANITIZE_STRING);
$estado = filter_input(INPUT_POST, 'estado', FILTER_SANITIZE_STRING);
$cidade = filter_input(INPUT_POST, 'cidade', FILTER_SANITIZE_STRING);


//echo "Nome: $nome <br>";
//echo "Email: $email <br>"; 

$result_usuario = "INSERT INTO cadastra_alunos (nome, sobrenome, nascimento, estado, cidade) VALUES ('$nome', '$sobrenome', $nascimento, '$estado', '$cidade')";
$resultado_usuario = mysqli_query($conn, $result_usuario);

header('Location: cadastro_alunos.php');