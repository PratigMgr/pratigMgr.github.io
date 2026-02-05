<?php
$Name = 'Pratig Thapa Magar';
$file = 'grades.php';
$desc = 'Displays student information and marks based on URL parameter with proper error handling';
$day = date('M d Y');

require_once('includes/functions.php');
$title = "Student Marks";
$banner = "Student Marks and Information";

// Start session
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}

// --- REDIRECT IF NOT LOGGED IN ---
if (!isset($_SESSION['user'])) {
    $_SESSION['message'] = "Please login to access grades.";
    header("Location: login.php");
    exit();
}

include('./includes/header.php');

// Prepare statements
if (!prepareAllStatements()) {
    echo '<p>Database Error</p>';
    include('./includes/footer.php');
    exit();
}

// Get student ID from query string
$student_id = isset($_GET['id']) ? trim($_GET['id']) : null;
?>

<h3>Search Student Grades</h3>
<form method="GET" action="grades.php">
    <input type="text" name="id" placeholder="Enter Student ID" value="" required>
    <input type="submit" value="Search">
</form>

<?php
// Display all students for reference
$ref_result = executePrepared("get_all_students", array());
if ($ref_result) {
    $records = pg_num_rows($ref_result);
    if ($records > 0) {
        echo '<h4>Available Students:</h4>';
        echo '<table border="1" width="100%">';
        echo '<tr><th>Student ID</th><th>First Name</th><th>Last Name</th><th>Email</th><th>Program Code</th></tr>';
        
        for ($i = 0; $i < $records; $i++) {
            echo '<tr>';
            echo '<td>'.pg_fetch_result($ref_result, $i, "student_id").'</td>';
            echo '<td>'.pg_fetch_result($ref_result, $i, "first_name").'</td>';
            echo '<td>'.pg_fetch_result($ref_result, $i, "last_name").'</td>';
            echo '<td>'.pg_fetch_result($ref_result, $i, "email").'</td>';
            echo '<td>'.pg_fetch_result($ref_result, $i, "program_code").'</td>';
            echo '</tr>';
        }
        echo '</table><br>';
    }
}

// Display selected student info and marks
if ($student_id) {
    if (!is_numeric($student_id)) {
        echo '<p>Error: Student ID must be numeric</p>';
    } else {
        $student_result = executePrepared("get_student_info", array($student_id));
        if ($student_result && pg_num_rows($student_result) > 0) {
            echo '<h3>Student Information</h3>';
            echo '<p><strong>ID:</strong> '.htmlspecialchars($student_id).'</p>';
            echo '<p><strong>Name:</strong> '.htmlspecialchars(pg_fetch_result($student_result, 0, "first_name").' '.pg_fetch_result($student_result, 0, "last_name")).'</p>';
            echo '<p><strong>Program:</strong> '.htmlspecialchars(pg_fetch_result($student_result, 0, "program_code")).'</p>';
            echo '<p><strong>Email:</strong> '.htmlspecialchars(pg_fetch_result($student_result, 0, "email")).'</p>';
            
            $marks_result = executePrepared("get_student_marks", array($student_id));
            if ($marks_result) {
                $records = pg_num_rows($marks_result);
                if ($records > 0) {
                    echo '<h3>Academic Performance</h3>';
                    echo '<table border="1" width="100%">';
                    echo '<tr><th>Course Code</th><th>Course Description</th><th>Final Mark</th><th>Date</th></tr>';
                    
                    for ($i = 0; $i < $records; $i++) {
                        echo '<tr>';
                        echo '<td>'.pg_fetch_result($marks_result, $i, "course_code").'</td>';
                        echo '<td>'.pg_fetch_result($marks_result, $i, "course_description").'</td>';
                        echo '<td>'.pg_fetch_result($marks_result, $i, "final_mark").'%</td>';
                        echo '<td>'.pg_fetch_result($marks_result, $i, "achieved_at").'</td>';
                        echo '</tr>';
                    }
                    echo '</table>';
                } else {
                    echo '<p>No marks recorded</p>';
                }
            }
        } else {
            echo '<p>Student Not Found</p>';
        }
    }
    echo '<br><a href="grades.php">Search Another</a> | ';
}
?>
<a href="index.php">Home</a>

<?php
include('./includes/footer.php');
?>
