<?php $Name = 'Pratig Thapa Magar' ?>
<?php $file = 'footer.php' ?>
<?php $desc = 'Contains the footer section for all pages' ?>
<?php $day = date('M d Y') ?>

<!-- 
Name: <?php echo $Name . "\n"; ?>
File: <?php echo $file . "\n"; ?>
Desc: <?php echo $desc . "\n"; ?>
Date: <?php echo $day . "\n"; ?>
-->

    </div> <!-- End content wrapper -->

<footer class="bg-dark text-white mt-5 py-4">
    <div class="container">

        <div class="row text-center text-md-start align-items-center">

            <!-- LEFT SIDE -->
            <div class="col-md-4">
                <p class="mb-0">&copy; <?php echo date('Y'); ?> INFT2100 Student Portal</p>
            </div>

            <!-- CENTER -->
            <div class="col-md-4 d-flex justify-content-center align-items-center" style="gap: 10px;">
                <span>Success Matters</span>
                <img src="./image/logo.png" alt="Durham College Logo" style="width:55px; height:auto;">
            </div>

            <!-- RIGHT SIDE -->
            <div class="col-md-4 text-md-end mt-3 mt-md-0">
                <p class="mb-1">Lab Assignment 04 - PHP User Authentication</p>

                <a href="privacy_policy.php" class="text-white me-3">Privacy Policy</a>
                <a href="aup.php" class="text-white">Acceptable Use Policy</a>
            </div>

        </div>

    </div>
</footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
