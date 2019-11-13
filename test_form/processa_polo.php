<?php

include_once("conexao.php"); 

$codigo = filter_input(INPUT_POST, 'codigo', FILTER_SANITIZE_STRING);
$nome = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_STRING);
$email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_STRING);
$estado = filter_input(INPUT_POST, 'estado', FILTER_SANITIZE_STRING);
$cidade = filter_input(INPUT_POST, 'cidade', FILTER_SANITIZE_STRING);
$cep = filter_input(INPUT_POST, 'cep', FILTER_SANITIZE_STRING);

//echo "Nome: $nome <br>";
//echo "Email: $email <br>"; 

$result_usuario = "INSERT INTO cadastra_polos (nome, email, estado, cidade, cep) VALUES ('$nome', '$email', '$estado', '$cidade', '$cep')";
$resultado_usuario = mysqli_query($conn, $result_usuario);
header('Location: cadastro_polos.php');