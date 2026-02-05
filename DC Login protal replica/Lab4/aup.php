<?php $Name = 'Pratig Thapa Magar' ?>
<?php $file = 'aup.php' ?>
<?php $desc = 'Displays Acceptable Use Policy required for Lab 04' ?>
<?php $day = date('M d Y') ?>

<!--
Name: <?php echo $Name . "\n"; ?>
File: <?php echo $file . "\n"; ?>
Desc: <?php echo $desc . "\n"; ?>
Date: <?php echo $day . "\n"; ?>
-->

<?php
$title = "Acceptable Use Policy";
$banner = "Acceptable Use Policy";

include('./includes/header.php');
?>

<div class="row">
    <div class="col-md-10 offset-md-1">

        <h3>Acceptable Use Policy</h3>
        <p class="mt-3">
            This system is intended for educational use only as part of the INFT2100 Web Development course. 
            Students must use the system responsibly and ethically.
        </p>

        <ul>
            <li>Users may only access their own academic information.</li>
            <li>Sharing login credentials is not permitted.</li>
            <li>Malicious use, hacking attempts, or unauthorized data access is strictly prohibited.</li>
            <li>All login attempts and activity may be logged for academic evaluation.</li>
        </ul>

        <p>
            By using this service, you agree to comply with the acceptable use rules listed above.
        </p>

    </div>
</div>

<?php include('./includes/footer.php'); ?>
