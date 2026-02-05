<?php
$Name = 'Pratig Thapa Magar';
$file = 'functions.php';
$desc = 'Contains database connection and helper functions';
$day = date('M d Y');
?>

<?php
// -------------------- DATABASE CONNECTION --------------------
function db_connect() {
    static $conn = null;

    if ($conn === null) {
		$host = "127.0.0.1";
		$port = "5432";
		$dbname = "thapamagarp_db";
		$user = "thapamagarp";
		$password = "Passw0rd!!";


        $conn = pg_connect("host=$host port=$port dbname=$dbname user=$user password=$password");
        if (!$conn) {
            error_log("Database connection failed: " . pg_last_error());
            return false;
        }
    }

    return $conn;
}

// -------------------- PREPARE COMMONLY USED STATEMENTS --------------------
function prepareAllStatements() {
    $conn = db_connect();
    if (!$conn) return false;

    $statements = [
        "get_student_info" => "SELECT u.first_name, u.last_name, u.email, s.program_code 
                               FROM users u 
                               JOIN students s ON u.user_id = s.student_id 
                               WHERE u.user_id = $1",
        "get_student_marks" => "SELECT m.course_code, c.course_description, m.final_mark, m.achieved_at
                                FROM marks m 
                                JOIN courses c ON m.course_code = c.course_code 
                                WHERE m.student_id = $1 
                                ORDER BY m.achieved_at DESC",
        "get_all_students" => "SELECT u.user_id as student_id, u.first_name, u.last_name, u.email, s.program_code
                               FROM users u 
                               JOIN students s ON u.user_id = s.student_id
                               ORDER BY u.user_id"
    ];

    foreach ($statements as $name => $sql) {
        @pg_prepare($conn, $name, $sql); // suppress warning if already prepared
    }

    return true;
}

// -------------------- EXECUTE PREPARED STATEMENT --------------------
function executePrepared($statementName, $params = []) {
    $conn = db_connect();
    if (!$conn) return false;

    $result = pg_execute($conn, $statementName, $params);
    if (!$result) {
        error_log("Query failed ($statementName): " . pg_last_error($conn));
        return false;
    }

    return $result;
}

// -------------------- LOG USER ACTIVITY --------------------
function log_activity($message) {
    $conn = db_connect();
    if ($conn) {
        pg_query_params($conn, "INSERT INTO activity_log (message, created_at) VALUES ($1, NOW())", [$message]);
    } else {
        error_log($message);
    }
}

// -------------------- GENERATE UNIQUE 9-DIGIT USER ID --------------------
function generateUniqueUserId() {
    $conn = db_connect();
    if (!$conn) return false;

    do {
        $user_id = rand(100700000, 999999999);
        $check = pg_query_params($conn, "SELECT 1 FROM users WHERE user_id=$1", [$user_id]);
    } while ($check && pg_num_rows($check) > 0);

    return $user_id;
}
?>
