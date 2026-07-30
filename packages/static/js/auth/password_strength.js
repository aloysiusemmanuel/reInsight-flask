/*
=========================================================
reInsight Password Strength Meter
=========================================================
*/

document.addEventListener("DOMContentLoaded", function () {

    const passwordInput = document.getElementById("new_password");

    const bar = document.getElementById("passwordStrengthBar");

    const text = document.getElementById("passwordStrengthText");

    if (!passwordInput) {
        return;
    }

    passwordInput.addEventListener("input", function () {

        const password = this.value;

        let score = 0;

        //-------------------------------------------------
        // Length
        //-------------------------------------------------

        if (password.length >= 8) score++;

        if (password.length >= 12) score++;

        //-------------------------------------------------
        // Lowercase
        //-------------------------------------------------

        if (/[a-z]/.test(password)) score++;

        //-------------------------------------------------
        // Uppercase
        //-------------------------------------------------

        if (/[A-Z]/.test(password)) score++;

        //-------------------------------------------------
        // Numbers
        //-------------------------------------------------

        if (/\d/.test(password)) score++;

        //-------------------------------------------------
        // Special Characters
        //-------------------------------------------------

        if (/[!@#$%^&*(),.?":{}|<>]/.test(password))
            score++;

        updateStrength(score);

    });


    function updateStrength(score) {

        let width = 0;

        let message = "";

        let color = "";

        switch (true) {

            case (score <= 1):

                width = 20;
                color = "bg-danger";
                message = "Very Weak";

                break;

            case (score === 2):

                width = 40;
                color = "bg-warning";
                message = "Weak";

                break;

            case (score === 3):

                width = 60;
                color = "bg-info";
                message = "Fair";

                break;

            case (score === 4):

                width = 80;
                color = "bg-primary";
                message = "Good";

                break;

            default:

                width = 100;
                color = "bg-success";
                message = "Strong";

        }

        bar.style.width = width + "%";

        bar.className =
            "progress-bar " + color;

        text.innerHTML =
            "<strong>" + message + "</strong>";

    }

});