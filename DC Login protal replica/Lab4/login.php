<?php
$Name = 'Pratig Thapa Magar';
$file = 'login.php';
$desc = 'Login page for authenticating student users';
$day = date('M d Y');
?>

<?php 
require_once('./includes/functions.php');
prepareAllStatements();

$title = "Login";
$banner = "Student Login";

session_start();

// Message from registration or other page
$msg = "";
if (isset($_SESSION['message']) && $_SESSION['message'] != "") {
    $msg = $_SESSION['message'];
    unset($_SESSION['message']); // Show once
}

// Pre-fill Student ID if cookie exists
$sticky_id = $_COOKIE['LOGIN_COOKIE'] ?? "";

// Process login form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $id = trim($_POST['id']);
    $pw = trim($_POST['password']);

    $conn = db_connect();
    if (!$conn) {
        $msg = "Database connection failed.";
    } else {
        // Fetch user info (existing or newly registered)
        $res = pg_query_params($conn, 
            "SELECT user_id, first_name, last_name, password 
             FROM users 
             WHERE user_id = $1", 
            [$id]
        );

        if ($res && pg_num_rows($res) === 1) {
            $user = pg_fetch_assoc($res);

            if (password_verify($pw, $user['password'])) {
                // Login success
                $_SESSION['user'] = [
                    'id' => $user['user_id'],
                    'first_name' => $user['first_name'],
                    'last_name' => $user['last_name']
                ];

                // Update last access
                pg_query_params($conn, "UPDATE users SET last_access = NOW() WHERE user_id = $1", [$id]);

                // Save cookie for convenience
                setcookie("LOGIN_COOKIE", $id, time() + 60*60*24*30);

                log_activity("User $id successfully logged in");
				
				$_SESSION['login_success'] = true;
                // Redirect to homepage
                header("Location: index.php");
	
                exit;

            } else {
                $msg = "Invalid password.";
                log_activity("Failed login attempt (wrong password) for ID $id");
            }

        } else {
            $msg = "Invalid student ID.";
            log_activity("Failed login attempt (unknown ID) for ID $id");
        }
    }
}

include('./includes/header.php');
?>

<div class="row">
    <div class="col-md-6 offset-md-3">

        <?php if ($msg): ?>
            <div class="alert alert-warning"><?= htmlspecialchars($msg) ?></div>
        <?php endif; ?>

        <h3>Login</h3>
        <form method="POST">
            <label class="form-label">Student ID</label>
            <input type="text" name="id" class="form-control" value="<?= htmlspecialchars($sticky_id) ?>">

            <br>

            <label class="form-label">Password</label>
            <input type="password" name="password" class="form-control">

            <br>
            <button class="btn btn-primary w-100">Login</button>
        </form>
    </div>
</div>

<?php include('./includes/footer.php'); ?>
