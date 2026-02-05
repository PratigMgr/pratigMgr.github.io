<?php 
ob_start();

$Name = 'Pratig Thapa Magar';
$file = 'header.php';
$desc = 'Contains the header section and HTML head for all pages';
$day = date('M d Y');
?>

<!-- 
Name: <?php echo $Name . "\n"; ?>
File: <?php echo $file . "\n"; ?>
Desc: <?php echo $desc . "\n"; ?>
Date: <?php echo $day . "\n"; ?>
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>INFT2100 - <?php echo $title; ?></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
        }
        
        body {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        
        .content-wrapper {
            flex: 1;
        }

        .banner {
            background-color: #f8f9fa;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
		.logo-img {
				background: transparent !important;
				border-radius: 0;
				padding: 0;
				mix-blend-mode: multiply;
			}
    </style>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            
            <!-- Home link must always show -->
			<a class="navbar-brand" href="index.php"><img src="./image/logo.png" width="70" class="mx-auto mb-3">
			DC Student Portal</a>


            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">

                    <!-- Static Home link (required) -->
                    <li class="nav-item">
                        <a class="nav-link" href="index.php">Home</a>
                    </li>

                    <!-- Dynamic Links Based on Login Status -->
                    <?php if (!isset($_SESSION['user'])): ?>
                        
                        <!-- Show when NOT logged in -->
                        <li class="nav-item">
                            <a class="nav-link" href="login.php">Login</a>
                        </li>
                        
                        <li class="nav-item">
                            <a class="nav-link" href="register.php">Register</a>
                        </li>

                    <?php else: ?>

                        <!-- Show when LOGGED IN -->
                        <li class="nav-item">
                            <a class="nav-link" href="grades.php">Dashboard</a>
                        </li>

						<li class="nav-item">
							<a class="nav-link" href="grades.php">Grades</a>
						</li>
                        <li class="nav-item">
                            <a class="nav-link" href="logout.php">Logout</a>
                        </li>

                    <?php endif; ?>
                </ul>
            </div>

        </div>
    </nav>

    <div class="container mt-4">
        <div class="banner">
            <h1><?php echo $banner; ?></h1>
            <p class="lead">INFT2100 - Web Development</p>
        </div>
