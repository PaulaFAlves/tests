<?php

include_once("conexao.php"); 

$codigo = filter_input(INPUT_POST, 'codigo', FILTER_SANITIZE_STRING);
$disciplina = filter_input(INPUT_POST, 'disciplina', FILTER_SANITIZE_STRING);
$curso = filter_input(INPUT_POST, 'curso', FILTER_SANITIZE_STRING);



//echo "Nome: $nome <br>";
//echo "Email: $email <br>"; 

$result_usuario = "INSERT INTO cadastra_disciplinas (disciplina, curso) VALUES ('$disciplina', '$curso')";
$resultado_usuario = mysqli_query($conn, $result_usuario);
header('Location: cadastro_disciplina.php');
