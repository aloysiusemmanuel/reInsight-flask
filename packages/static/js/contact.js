document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("contactForm");

    if (!form) return;

    form.addEventListener("submit", function (e) {

        let valid = true;

        const requiredFields = [

            "full_name",

            "email",

            "subject",

            "message"

        ];

        requiredFields.forEach(id => {

            const field = document.getElementById(id);

            if (field.value.trim() === "") {

                field.classList.add("is-invalid");

                valid = false;

            } else {

                field.classList.remove("is-invalid");

                field.classList.add("is-valid");

            }

        });

        const email = document.getElementById("email");

        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!regex.test(email.value)) {

            email.classList.add("is-invalid");

            valid = false;

        }

        if (!valid) {

            e.preventDefault();

        }

    });

});