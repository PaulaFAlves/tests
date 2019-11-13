<?php

	session_start();
	include_once("conexao.php");
	if((isset($_POST['email'])) && (isset($_POST['senha']))) {
		$usuario = $_POST['email'];
		$senha = $_POST['senha'];

		if (($usuario == "paula@paula") && ($senha == "1111")){
			header("Location: menu.php");
		}else{
			$_SESSION['loginErro'] = "Usuario ou senha invalido.";
			header("Location: index.php");
		}

	}else{
		$_SESSION['loginErro'] = "Erro.";
		header("Location: index.php");
	}


?>