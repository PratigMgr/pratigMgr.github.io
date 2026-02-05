<?php
$Name = 'Pratig Thapa Magar';
$file = 'register.php';
$desc = 'Handles new student account creation and validation';
$day = date('M d Y');
?>

<?php
require_once('./includes/functions.php');
prepareAllStatements();

// Start session at the very top
session_start();

// --- Header variables ---
$title = "Register";
$banner = "Create New Account";

// Redirect logged-in users
if (isset($_SESSION['user'])) {
    $_SESSION['message'] = "You are already logged in.";
    header("Location: index.php");
    exit;
}

// --- Form variables & sticky data ---
$errors = [];
$sticky = ["email"=>"", "first"=>"", "last"=>"", "birthdate"=>"", "program"=>""];

// --- Form submission handling ---
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $email = trim($_POST['email']);
    $pw = trim($_POST['password']);
    $cpw = trim($_POST['confirm']);
    $first = trim($_POST['first']);
    $last = trim($_POST['last']);
    $birth = trim($_POST['birthdate']);
    $program = $_POST['program'] ?? "";

    $sticky = [
        "email" => $email,
        "first" => $first,
        "last" => $last,
        "birthdate" => $birth,
        "program" => $program
    ];

    // --- Validation ---
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = "Invalid email address.";
    if ($first === "") $errors[] = "First name is required.";
    if ($last === "") $errors[] = "Last name is required.";
    if ($birth === "") $errors[] = "Birthdate is required.";
    if (strlen($pw) < 6) $errors[] = "Password must be at least 6 characters.";
    if ($pw !== $cpw) $errors[] = "Passwords do not match.";
    if ($program === "") $errors[] = "Please select a program.";

    // --- Insert into DB if no errors ---
    if (empty($errors)) {

        $pw_hash = password_hash($pw, PASSWORD_DEFAULT);
        $conn = db_connect();

        if (!$conn) {
            $errors[] = "Database connection failed.";
        } else {

            // Generate unique 9-digit user_id (Student ID)
            $user_id = generateUniqueUserId();

            // Insert into users table
            $res_user = pg_query_params($conn,
                "INSERT INTO users (user_id, first_name, last_name, email, birth_date, password, created_at, last_access)
                 VALUES ($1, $2, $3, $4, $5, $6, NOW(), NOW())",
                [$user_id, $first, $last, $email, $birth, $pw_hash]
            );

            if ($res_user) {
                // Insert into students table
                $res_student = pg_query_params($conn,
                    "INSERT INTO students (student_id, program_code)
                     VALUES ($1, $2)",
                    [$user_id, $program]
                );

                if ($res_student) {
                    log_activity("New student registered with Student ID $user_id");

                    // Set session message to show Student ID on homepage
                    $_SESSION['message'] = "Registration successful! Your Student ID is: $user_id";

                    // Redirect to homepage
                    header("Location: index.php");
                    exit;
                } else {
                    $errors[] = "Failed to insert student details.";
                }

            } else {
                $errors[] = "Failed to insert user details.";
            }
        }
    }
}

// --- Include site header ---
include('./includes/header.php');
?>

<div class="row">
    <div class="col-md-8 offset-md-2">

        <?php if (!empty($errors)): ?>
            <div class="alert alert-danger">
                <ul>
                    <?php foreach ($errors as $e) echo "<li>" . htmlspecialchars($e) . "</li>"; ?>
                </ul>
            </div>
        <?php endif; ?>

        <h3>Register</h3>
        <form method="POST">
            <label>Email:</label>
            <input type="text" class="form-control" name="email" value="<?= htmlspecialchars($sticky['email'] ?? ''); ?>"><br>

            <label>First Name:</label>
            <input type="text" class="form-control" name="first" value="<?= htmlspecialchars($sticky['first'] ?? ''); ?>"><br>

            <label>Last Name:</label>
            <input type="text" class="form-control" name="last" value="<?= htmlspecialchars($sticky['last'] ?? ''); ?>"><br>

            <label>Birthdate:</label>
            <input type="date" class="form-control" name="birthdate" value="<?= htmlspecialchars($sticky['birthdate'] ?? ''); ?>"><br>

            <label>Program:</label><br>
            <input type="radio" name="program" value="CPGA" <?= ($sticky['program'] ?? '')=="CPGA" ? "checked" : "" ?>> CPGA
            <input type="radio" name="program" value="CPPG" <?= ($sticky['program'] ?? '')=="CPPG" ? "checked" : "" ?>> CPPG
            <br><br>

            <label>Password:</label>
            <input type="password" class="form-control" name="password"><br>

            <label>Confirm Password:</label>
            <input type="password" class="form-control" name="confirm"><br>

            <button class="btn btn-success w-100">Register</button>
        </form>
    </div>
</div>

<?php include('./includes/footer.php'); ?>
