<?php
$Name = 'Pratig Thapa Magar';
$file = 'index.php';
$desc = 'Modern and organized DC-branded home page for Student Portal';
$day = date('M d Y');
?>

<?php 
require_once('includes/functions.php');
session_start();

// Set page metadata used by header.php
$title = "Home Page";

// Update banner to include logged-in user name if available
if (isset($_SESSION['user'])) {
    $firstName = htmlspecialchars($_SESSION['user']['first_name']);
    $banner    = "<span class='student-name'>$firstName</span>, Welcome to DC Portal";
} else {
    $banner = "Welcome to DC Student Portal";
}

// Include the shared header template
include('./includes/header.php');
?>

<!-- ======================= DISPLAY SUCCESS MESSAGE AFTER LOGIN ======================= -->
<?php
if (isset($_SESSION['login_success']) && $_SESSION['login_success'] === true): ?>
    <div class="alert alert-success alert-dismissible fade show text-center mt-3" role="alert">
        You have successfully logged in as <?= htmlspecialchars($_SESSION['user']['first_name'] . ' ' . $_SESSION['user']['last_name']); ?>.
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
<?php 
    unset($_SESSION['login_success']); // Show only once
endif;

// Display any other messages (e.g., from registration)
if (!empty($_SESSION['message'])): ?>
    <div class="alert alert-success alert-dismissible fade show text-center mt-3" role="alert">
        <?= htmlspecialchars($_SESSION['message']); ?>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
<?php 
    unset($_SESSION['message']);
endif;
?>

<!-- ======================= HERO / TOP BANNER ======================= -->
<div class="text-center mb-5">
    <img src="./image/durham-college-logo-png_seeklogo-310200.png" 
         alt="Durham College Logo"
         style="max-width: 320px;" 
         class="img-fluid mb-3">

    <h2 class="fw-bold mt-3">Your Academic Success Starts Here</h2>
    <p class="lead text-muted">
        Access your grades and student information securely through the DC Student Portal.
    </p>

    <!-- Login/Register buttons only if NOT logged in -->
    <?php if (!isset($_SESSION['user'])): ?>
    <div class="mt-4">
        <a href="login.php" class="btn btn-success btn-lg me-2 px-4">Login</a>
        <a href="register.php" class="btn btn-outline-success btn-lg px-4">Register</a>
    </div>
    <?php endif; ?>
</div>

<!-- ======================= FEATURE CARDS ======================= -->
<div class="row text-center mb-5">

    <h3 class="fw-bold mb-4">Portal Features</h3>

    <div class="col-md-4 mb-3">
        <div class="card border-0 shadow-sm p-4 h-100">
            <img src="./image/logo.png" width="70" class="mx-auto mb-3">
            <h5 class="fw-bold">Secure Login</h5>
            <p class="text-muted small">
                Protected with encrypted passwords and validated login attempts.
            </p>
        </div>
    </div>

    <div class="col-md-4 mb-3">
        <div class="card border-0 shadow-sm p-4 h-100">
            <img src="./image/dc-bars.png" width="70" class="mx-auto mb-3" style="border-radius: 6px;">
            <h5 class="fw-bold">Student Information</h5>
            <p class="text-muted small">
                View personal academic details and program information.
            </p>
        </div>
    </div>

    <div class="col-md-4 mb-3">
        <div class="card border-0 shadow-sm p-4 h-100">
            <img src="./image/durham-college-logo-png_seeklogo-310200.png" width="70" class="mx-auto mb-3">
            <h5 class="fw-bold">Grade Overview</h5>
            <p class="text-muted small">
                Review all course grades in one organized and easy-to-read place.
            </p>
        </div>
    </div>
</div>

<!-- ======================= QUICK NAVIGATION ======================= -->
<div class="row justify-content-center mb-5">
    <div class="col-md-6">
        <div class="card shadow-sm border-0 p-4">
            <h4 class="fw-bold">Quick Access</h4>
            <?php if (isset($_SESSION['user'])): ?>
                <p class="text-muted">Jump straight to your grades:</p>
                <a href="grades.php" class="btn btn-outline-secondary w-100">View Grades</a>
            <?php else: ?>
                <p class="text-muted">Already registered? Jump right into your dashboard.</p>
                <a href="login.php" class="btn btn-success w-100 mb-3">Go to Login</a>
                <a href="grades.php" class="btn btn-outline-secondary w-100">View Grades (Login Required)</a>
            <?php endif; ?>
        </div>
    </div>
</div>

<?php 
include('./includes/footer.php');
?>
