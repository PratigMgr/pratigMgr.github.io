<?php
$Name = 'Pratig Thapa Magar';
$file = 'logout.php';
$desc = 'Ends session and logs out the user';
$day = date('M d Y');
?>

<!-- 
Name: <?php echo $Name . "\n"; ?>
File: <?php echo $file . "\n"; ?>
Desc: <?php echo $desc . "\n"; ?>
Date: <?php echo $day . "\n"; ?>
-->

<?php
// Load helper functions
require_once("./includes/functions.php");

// Start session if not already started
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Log current user info if available
if (isset($_SESSION['user'])) {
    $user_id = $_SESSION['user']['id'] ?? 'Unknown';
    log_activity("User $user_id logged out");
}

// Completely destroy the session
session_unset();
session_destroy();

// Start a new session to store logout message
session_start();
$_SESSION['message'] = "You have successfully logged out.";

// Redirect to login page
header("Location: login.php");
exit;
?>
