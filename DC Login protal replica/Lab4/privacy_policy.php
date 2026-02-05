<?php $Name = 'Pratig Thapa Magar' ?>
<?php $file = 'privacy_policy.php' ?>
<?php $desc = 'Displays the Privacy Policy required for Lab 04' ?>
<?php $day = date('M d Y') ?>

<!--
Name: <?php echo $Name . "\n"; ?>
File: <?php echo $file . "\n"; ?>
Desc: <?php echo $desc . "\n"; ?>
Date: <?php echo $day . "\n"; ?>
-->

<?php
// Page metadata for header
$title = "Privacy Policy";
$banner = "Privacy Policy";

// Include header
include('./includes/header.php');
?>

<div class="row">
    <div class="col-md-10 offset-md-1">

        <h3>Privacy Policy</h3>
        <p class="mt-3">
            This website collects and stores information submitted by students when creating an account, logging in, 
            or accessing academic features. Information collected includes your student ID, email address, first and last name, 
            program code, and login activity timestamps.
        </p>

        <p>
            All collected information is used solely for academic authentication and grade retrieval within the 
            INFT2100 Web Development course. No personal information is shared, sold, or used for external purposes.
        </p>

        <p>
            By using this website, you consent to the storage of your information in accordance with course requirements.
        </p>

    </div>
</div>

<?php include('./includes/footer.php'); ?>
