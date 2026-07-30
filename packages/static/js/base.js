/* ==========================================================
   reInsight Public Website
   File: base.js
   Version: 1.0
========================================================== */

document.addEventListener("DOMContentLoaded", () => {

    initializeLoader();
    initializeNavbar();
    initializeBackToTop();
    initializeSmoothScrolling();
    initializeAnimations();
    initializeActiveNavigation();

});


/* ==========================================================
   PAGE LOADER
========================================================== */

function initializeLoader() {

    const loader = document.getElementById("pageLoader");

    if (!loader) return;

    window.addEventListener("load", () => {

        loader.style.opacity = "0";

        setTimeout(() => {

            loader.style.display = "none";

        }, 400);

    });

}


/* ==========================================================
   STICKY NAVBAR
========================================================== */

function initializeNavbar() {

    const navbar = document.querySelector(".navbar");

    if (!navbar) return;

    window.addEventListener("scroll", () => {

        if (window.scrollY > 50) {

            navbar.classList.add("navbar-scrolled");

        } else {

            navbar.classList.remove("navbar-scrolled");

        }

    });

}


/* ==========================================================
   BACK TO TOP BUTTON
========================================================== */

function initializeBackToTop() {

    const button = document.getElementById("backToTop");

    if (!button) return;

    window.addEventListener("scroll", () => {

        if (window.scrollY > 400) {

            button.style.display = "flex";

        } else {

            button.style.display = "none";

        }

    });

    button.addEventListener("click", () => {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });

}


/* ==========================================================
   SMOOTH SCROLL
========================================================== */

function initializeSmoothScrolling() {

    document.querySelectorAll('a[href^="#"]').forEach(link => {

        link.addEventListener("click", function (e) {

            const target = document.querySelector(this.getAttribute("href"));

            if (!target) return;

            e.preventDefault();

            target.scrollIntoView({

                behavior: "smooth",

                block: "start"

            });

        });

    });

}


/* ==========================================================
   FADE-UP ANIMATION
========================================================== */

function initializeAnimations() {

    const elements = document.querySelectorAll(".fade-up");

    if (!elements.length) return;

    const observer = new IntersectionObserver(entries => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

            }

        });

    }, {

        threshold: 0.15

    });

    elements.forEach(element => observer.observe(element));

}


/* ==========================================================
   ACTIVE NAVIGATION
========================================================== */

function initializeActiveNavigation() {

    const currentPath = window.location.pathname;

    document.querySelectorAll(".navbar .nav-link").forEach(link => {

        const href = link.getAttribute("href");

        if (!href) return;

        if (href === currentPath) {

            link.classList.add("active");

        }

    });

}


/* ==========================================================
   UTILITY
========================================================== */

function debounce(callback, delay = 200) {

    let timeout;

    return (...args) => {

        clearTimeout(timeout);

        timeout = setTimeout(() => {

            callback(...args);

        }, delay);

    };

}


/* ==========================================================
   WINDOW RESIZE
========================================================== */

window.addEventListener("resize", debounce(() => {

    console.log("Viewport:", window.innerWidth);

}));


/* ==========================================================
   FUTURE MODULES
========================================================== */

/*

Future enhancements:

✔ Dark / Light mode
✔ Theme switcher
✔ Search modal
✔ Newsletter subscription
✔ Language switcher
✔ Notification banner
✔ Cookie consent
✔ Live chat widget
✔ Video modal
✔ Pricing calculator
✔ FAQ accordion enhancements
✔ Testimonial carousel
✔ Dashboard preview slider

*/