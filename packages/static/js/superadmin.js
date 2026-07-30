/*
=========================================================
reInsight School Management System
Super Admin Dashboard

Author : Emmelac Tutorial
File   : superadmin.js
Part   : 1

Application Initialization
Sidebar Management
Navigation
Bootstrap Components
=========================================================
*/

"use strict";

/* =====================================================
GLOBAL APPLICATION
===================================================== */

const SuperAdmin = {

    /* ==============================================
    CONFIGURATION
    ============================================== */

    config: {

        sidebarCollapsedKey: "reinsight_sidebar_collapsed",

        animationSpeed: 300

    },



    /* ==============================================
    DOM ELEMENTS
    ============================================== */

    dom: {},



    /* ==============================================
    INITIALIZE APPLICATION
    ============================================== */

    init() {

        this.cacheDOM();

        this.initializeBootstrap();

        this.initializeSidebar();

        this.initializeOverlay();

        this.initializeActiveMenu();

        this.restoreSidebarState();

        this.bindEvents();

        console.log("reInsight Super Admin Initialized");

    },



    /* ==============================================
    CACHE DOM
    ============================================== */

    cacheDOM() {

        this.dom.sidebar =
            document.getElementById("sidebar");

        this.dom.sidebarToggle =
            document.getElementById("sidebarToggle");

        this.dom.overlay =
            document.getElementById("sidebarOverlay");

        this.dom.mainContent =
            document.getElementById("mainContent");

    },



    /* ==============================================
    BOOTSTRAP
    ============================================== */

    initializeBootstrap() {

        const tooltips =
            [].slice.call(
                document.querySelectorAll(
                    '[data-bs-toggle="tooltip"]'
                )
            );

        tooltips.forEach(function (tooltip) {

            new bootstrap.Tooltip(tooltip);

        });

    },



    /* ==============================================
    SIDEBAR
    ============================================== */

    initializeSidebar() {

        if (!this.dom.sidebarToggle)
            return;

        this.dom.sidebarToggle.addEventListener(

            "click",

            () => {

                if (window.innerWidth <= 991) {

                    this.toggleMobileSidebar();

                } else {

                    this.toggleDesktopSidebar();

                }

            }

        );

    },



    /* ==============================================
    DESKTOP SIDEBAR
    ============================================== */

    toggleDesktopSidebar() {

        this.dom.sidebar.classList.toggle("collapsed");

        this.dom.mainContent.classList.toggle("expanded");

        localStorage.setItem(

            this.config.sidebarCollapsedKey,

            this.dom.sidebar.classList.contains("collapsed")

        );

    },



    /* ==============================================
    MOBILE SIDEBAR
    ============================================== */

    toggleMobileSidebar() {

        this.dom.sidebar.classList.toggle("show");

        this.dom.overlay.classList.toggle("show");

    },



    /* ==============================================
    OVERLAY
    ============================================== */

    initializeOverlay() {

        if (!this.dom.overlay)
            return;

        this.dom.overlay.addEventListener(

            "click",

            () => {

                this.dom.sidebar.classList.remove("show");

                this.dom.overlay.classList.remove("show");

            }

        );

    },



    /* ==============================================
    RESTORE SIDEBAR STATE
    ============================================== */

    restoreSidebarState() {

        const collapsed =

            localStorage.getItem(

                this.config.sidebarCollapsedKey

            );

        if (

            collapsed === "true" &&

            window.innerWidth > 991

        ) {

            this.dom.sidebar.classList.add("collapsed");

            this.dom.mainContent.classList.add("expanded");

        }

    },



    /* ==============================================
    ACTIVE MENU
    ============================================== */

    initializeActiveMenu() {

        const currentPath =

            window.location.pathname;

        const links =

            document.querySelectorAll(

                ".sidebar-menu a"

            );

        links.forEach(link => {

            if (

                currentPath ===

                new URL(link.href).pathname

            ) {

                link.classList.add("active");

            }

        });

    },



    /* ==============================================
    EVENTS
    ============================================== */

    bindEvents() {

        window.addEventListener(

            "resize",

            () => {

                if (window.innerWidth > 991) {

                    this.dom.overlay.classList.remove("show");

                    this.dom.sidebar.classList.remove("show");

                }

            }

        );

    }

};



/* =====================================================
HELPER FUNCTIONS
===================================================== */

const Utils = {

    /* ==========================================
    SELECTOR
    ========================================== */

    qs(selector) {

        return document.querySelector(selector);

    },



    qsa(selector) {

        return document.querySelectorAll(selector);

    },



    /* ==========================================
    SMOOTH SCROLL
    ========================================== */

    scrollTop() {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    },



    /* ==========================================
    RANDOM ID
    ========================================== */

    randomID(length = 8) {

        return Math.random()

            .toString(36)

            .substring(2, length + 2);

    }

};



/* =====================================================
DOCUMENT READY
===================================================== */

document.addEventListener(

    "DOMContentLoaded",

    () => {

        SuperAdmin.init();

    }

);


/*
=========================================================
reInsight School Management System
Super Admin Dashboard

Author : Emmelac Tutorial
File   : superadmin.js
Part   : 2

Notifications
Search
Loading
Alerts
Utilities
=========================================================
*/

"use strict";


/* =====================================================
NOTIFICATIONS
===================================================== */

SuperAdmin.initializeNotifications = function () {

    const notificationButton =
        document.getElementById("notificationButton");

    if (!notificationButton)
        return;

    notificationButton.addEventListener(

        "click",

        () => {

            console.log("Notifications opened.");

        }

    );

};



/* =====================================================
MARK NOTIFICATION READ
===================================================== */

SuperAdmin.markNotificationRead = function (element) {

    if (!element)
        return;

    element.classList.remove("unread");

};



/* =====================================================
GLOBAL SEARCH
===================================================== */

SuperAdmin.initializeSearch = function () {

    const searchInput =
        document.getElementById("globalSearch");

    if (!searchInput)
        return;

    searchInput.addEventListener(

        "keyup",

        function () {

            const keyword =
                this.value.trim().toLowerCase();

            console.log("Searching:", keyword);

            /*
            Future:

            Fetch API

            Search Schools

            Search Users

            Search Reports

            */

        }

    );

};



/* =====================================================
LOADING OVERLAY
===================================================== */

SuperAdmin.showLoader = function () {

    const loader =
        document.getElementById("pageLoader");

    if (!loader)
        return;

    loader.classList.remove("d-none");

};



SuperAdmin.hideLoader = function () {

    const loader =
        document.getElementById("pageLoader");

    if (!loader)
        return;

    loader.classList.add("d-none");

};



/* =====================================================
SUCCESS ALERT
===================================================== */

SuperAdmin.success = function (message) {

    this.toast(

        message,

        "success"

    );

};



/* =====================================================
ERROR ALERT
===================================================== */

SuperAdmin.error = function (message) {

    this.toast(

        message,

        "danger"

    );

};



/* =====================================================
WARNING ALERT
===================================================== */

SuperAdmin.warning = function (message) {

    this.toast(

        message,

        "warning"

    );

};



/* =====================================================
TOAST
===================================================== */

SuperAdmin.toast = function (

    message,

    type = "primary"

) {

    const container =
        document.getElementById("toastContainer");

    if (!container)
        return;

    const toast =
        document.createElement("div");

    toast.className =
        `alert alert-${type} shadow-sm mb-3`;

    toast.innerHTML = `

        <div class="d-flex justify-content-between align-items-center">

            <span>${message}</span>

            <button
                class="btn-close">
            </button>

        </div>

    `;

    container.appendChild(toast);

    toast
        .querySelector(".btn-close")
        .addEventListener(

            "click",

            () => {

                toast.remove();

            }

        );

    setTimeout(

        () => {

            toast.remove();

        },

        4000

    );

};



/* =====================================================
PASSWORD TOGGLE
===================================================== */

SuperAdmin.initializePasswordToggle = function () {

    const toggles =
        document.querySelectorAll(

            ".password-toggle"

        );

    toggles.forEach(toggle => {

        toggle.addEventListener(

            "click",

            function () {

                const input =
                    document.querySelector(

                        this.dataset.target

                    );

                if (!input)
                    return;

                if (

                    input.type === "password"

                ) {

                    input.type = "text";

                    this.innerHTML =
                        '<i class="bi bi-eye-slash"></i>';

                } else {

                    input.type = "password";

                    this.innerHTML =
                        '<i class="bi bi-eye"></i>';

                }

            }

        );

    });

};



/* =====================================================
BACK TO TOP
===================================================== */

SuperAdmin.initializeBackToTop = function () {

    const button =
        document.getElementById("backToTop");

    if (!button)
        return;

    window.addEventListener(

        "scroll",

        () => {

            if (

                window.scrollY > 400

            ) {

                button.classList.remove("d-none");

            }

            else {

                button.classList.add("d-none");

            }

        }

    );

    button.addEventListener(

        "click",

        () => {

            Utils.scrollTop();

        }

    );

};



/* =====================================================
AUTO DISMISS ALERTS
===================================================== */

SuperAdmin.initializeAlerts = function () {

    const alerts =
        document.querySelectorAll(

            ".auto-dismiss"

        );

    alerts.forEach(alert => {

        setTimeout(

            () => {

                alert.remove();

            },

            5000

        );

    });

};



/* =====================================================
INITIALIZE PART 2
===================================================== */

const originalInit = SuperAdmin.init;

SuperAdmin.init = function () {

    originalInit.call(this);

    this.initializeNotifications();

    this.initializeSearch();

    this.initializePasswordToggle();

    this.initializeBackToTop();

    this.initializeAlerts();

};


/*
=========================================================
reInsight School Management System
Super Admin Dashboard

Author : Emmelac Tutorial
File   : superadmin.js
Part   : 3

Dashboard Widgets
Charts
Statistics
Tables
Forms
AJAX Utilities
=========================================================
*/

"use strict";

/* =====================================================
COUNTER ANIMATION
===================================================== */

SuperAdmin.initializeCounters = function () {

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = parseInt(counter.dataset.target || 0);

        const duration = 1200;

        const step = target / (duration / 20);

        let current = 0;

        const timer = setInterval(() => {

            current += step;

            if (current >= target) {

                counter.textContent =
                    target.toLocaleString();

                clearInterval(timer);

            } else {

                counter.textContent =
                    Math.floor(current).toLocaleString();

            }

        }, 20);

    });

};



/* =====================================================
PROGRESS BAR ANIMATION
===================================================== */

SuperAdmin.initializeProgressBars = function () {

    const bars = document.querySelectorAll(".progress-bar");

    bars.forEach(bar => {

        const width = bar.dataset.width || "0%";

        bar.style.width = "0%";

        setTimeout(() => {

            bar.style.width = width;

        }, 300);

    });

};



/* =====================================================
CHART.JS
===================================================== */

SuperAdmin.initializeCharts = function () {

    if (typeof Chart === "undefined")
        return;

    const revenueCanvas =
        document.getElementById("revenueChart");

    if (revenueCanvas) {

        new Chart(revenueCanvas, {

            type: "line",

            data: {

                labels: [

                    "Jan",

                    "Feb",

                    "Mar",

                    "Apr",

                    "May",

                    "Jun"

                ],

                datasets: [{

                    label: "Revenue",

                    data: [

                        120,

                        180,

                        220,

                        260,

                        340,

                        420

                    ],

                    borderColor: "#2563EB",

                    backgroundColor:
                        "rgba(37,99,235,.15)",

                    fill: true,

                    tension: .4

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false

            }

        });

    }

 const schoolCanvas =
    document.getElementById("schoolGrowthChart");

if (schoolCanvas) {

    const ctx = schoolCanvas.getContext("2d");

    new Chart(ctx, {

        type: "bar",

        data: {

            labels: [

                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun"

            ],

            datasets: [{

                label: "Schools",

                data: [

                    4,
                    7,
                    5,
                    8,
                    10,
                    12

                ],

                backgroundColor: "#2563EB"

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false

        }

    });

}   
};



/* =====================================================
TABLE SEARCH
===================================================== */

SuperAdmin.initializeTableSearch = function () {

    const searchInputs =
        document.querySelectorAll(".table-search");

    searchInputs.forEach(input => {

        input.addEventListener(

            "keyup",

            function () {

                const keyword =
                    this.value.toLowerCase();

                const table =
                    document.querySelector(

                        this.dataset.table

                    );

                if (!table)
                    return;

                const rows =
                    table.querySelectorAll("tbody tr");

                rows.forEach(row => {

                    const text =
                        row.textContent.toLowerCase();

                    row.style.display =
                        text.includes(keyword)
                        ? ""
                        : "none";

                });

            }

        );

    });

};



/* =====================================================
SELECT ALL CHECKBOX
===================================================== */

SuperAdmin.initializeSelectAll = function () {

    const masters =
        document.querySelectorAll(".check-all");

    masters.forEach(master => {

        master.addEventListener(

            "change",

            function () {

                const table =
                    document.querySelector(

                        this.dataset.table

                    );

                if (!table)
                    return;

                table.querySelectorAll(

                    ".row-check"

                ).forEach(box => {

                    box.checked =
                        master.checked;

                });

            }

        );

    });

};



/* =====================================================
FORM VALIDATION
===================================================== */

SuperAdmin.initializeForms = function () {

    const forms =
        document.querySelectorAll(

            ".needs-validation"

        );

    forms.forEach(form => {

        form.addEventListener(

            "submit",

            function (event) {

                if (!form.checkValidity()) {

                    event.preventDefault();

                    event.stopPropagation();

                }

                form.classList.add(

                    "was-validated"

                );

            }

        );

    });

};



/* =====================================================
AJAX HELPER
===================================================== */

SuperAdmin.request = async function (

    url,

    options = {}

) {

    try {

        this.showLoader();

        const response =

            await fetch(url, options);

        this.hideLoader();

        return response;

    }

    catch (error) {

        this.hideLoader();

        console.error(error);

        this.error(

            "Unable to connect to the server."

        );

    }

};



/* =====================================================
DELETE CONFIRMATION
===================================================== */

SuperAdmin.confirmDelete = function (

    callback

) {

    if (

        confirm(

            "Are you sure you want to delete this record?"

        )

    ) {

        callback();

    }

};



/* =====================================================
QUICK ACTION BUTTONS
===================================================== */

SuperAdmin.initializeQuickActions = function () {

    document.querySelectorAll(

        ".quick-action"

    ).forEach(button => {

        button.addEventListener(

            "click",

            function () {

                console.log(

                    "Quick Action:",

                    this.dataset.action

                );

            }

        );

    });

};



/* =====================================================
CARD HOVER EFFECT
===================================================== */

SuperAdmin.initializeCards = function () {

    document.querySelectorAll(

        ".stat-card"

    ).forEach(card => {

        card.addEventListener(

            "mouseenter",

            () => {

                card.classList.add("shadow-lg");

            }

        );

        card.addEventListener(

            "mouseleave",

            () => {

                card.classList.remove("shadow-lg");

            }

        );

    });

};



/* =====================================================
PART 3 INITIALIZER
===================================================== */

const previousInit = SuperAdmin.init;

SuperAdmin.init = function () {

    previousInit.call(this);

    this.initializeCounters();

    this.initializeProgressBars();

    this.initializeCharts();

    this.initializeTableSearch();

    this.initializeSelectAll();

    this.initializeForms();

    this.initializeQuickActions();

    this.initializeCards();


};


/*
=========================================================
reInsight School Management System
Super Admin Dashboard

Author : Emmelac Tutorial
File   : superadmin.js
Part   : 4

Session
Keyboard Shortcuts
Theme
Export
Auto Refresh
Utilities
=========================================================
*/

"use strict";


/* =====================================================
SESSION TIMEOUT
===================================================== */

SuperAdmin.initializeSession = function () {

    const SESSION_LIMIT = 30 * 60 * 1000;

    let sessionTimer;

    const resetSession = () => {

        clearTimeout(sessionTimer);

        sessionTimer = setTimeout(() => {

            this.warning(
                "Your session is about to expire."
            );

            console.log("Session timeout.");

        }, SESSION_LIMIT);

    };

    [
        "mousemove",
        "keydown",
        "click",
        "scroll"
    ].forEach(event => {

        document.addEventListener(

            event,

            resetSession

        );

    });

    resetSession();

};



/* =====================================================
KEYBOARD SHORTCUTS
===================================================== */

SuperAdmin.initializeKeyboardShortcuts = function () {

    document.addEventListener(

        "keydown",

        (event) => {

            if (!event.ctrlKey)
                return;

            switch (event.key.toLowerCase()) {

                case "/":

                    event.preventDefault();

                    document
                        .getElementById("globalSearch")
                        ?.focus();

                    break;

                case "d":

                    event.preventDefault();

                    location.href =
                        "/superadmin/";

                    break;

                case "u":

                    event.preventDefault();

                    location.href =
                        "/superadmin/users";

                    break;

                case "s":

                    event.preventDefault();

                    location.href =
                        "/superadmin/schools";

                    break;

            }

        }

    );

};



/* =====================================================
DARK MODE
===================================================== */

SuperAdmin.initializeTheme = function () {

    const button =
        document.getElementById("themeToggle");

    if (!button)
        return;

    const stored =
        localStorage.getItem("dashboard-theme");

    if (stored === "dark") {

        document.body.classList.add("dark-mode");

    }

    button.addEventListener(

        "click",

        () => {

            document.body.classList.toggle(

                "dark-mode"

            );

            localStorage.setItem(

                "dashboard-theme",

                document.body.classList.contains(

                    "dark-mode"

                )

                    ? "dark"

                    : "light"

            );

        }

    );

};



/* =====================================================
COPY TO CLIPBOARD
===================================================== */

SuperAdmin.copy = function (text) {

    navigator.clipboard.writeText(text);

    this.success("Copied successfully.");

};



/* =====================================================
CSV EXPORT
===================================================== */

SuperAdmin.exportCSV = function (

    tableID,

    filename = "export.csv"

) {

    const table =
        document.getElementById(tableID);

    if (!table)
        return;

    let csv = [];

    table.querySelectorAll("tr").forEach(row => {

        let rowData = [];

        row.querySelectorAll("th, td").forEach(cell => {

            rowData.push(cell.innerText);

        });

        csv.push(rowData.join(","));

    });

    const blob =
        new Blob(

            [csv.join("\n")],

            {

                type: "text/csv"

            }

        );

    const url =
        URL.createObjectURL(blob);

    const link =
        document.createElement("a");

    link.href = url;

    link.download = filename;

    link.click();

};



/* =====================================================
PRINT PAGE
===================================================== */

SuperAdmin.print = function () {

    window.print();

};



/* =====================================================
AUTO REFRESH DASHBOARD
===================================================== */

SuperAdmin.initializeAutoRefresh = function () {

    const refresh =
        document.body.dataset.refresh;

    if (!refresh)
        return;

    setInterval(

        () => {

            console.log(

                "Refreshing dashboard..."

            );

        },

        parseInt(refresh) * 1000

    );

};



/* =====================================================
SCROLL ANIMATION
===================================================== */

SuperAdmin.initializeAnimations = function () {

    const observer =

        new IntersectionObserver(

            entries => {

                entries.forEach(entry => {

                    if (entry.isIntersecting) {

                        entry.target.classList.add(

                            "fade-in"

                        );

                    }

                });

            },

            {

                threshold: .2

            }

        );

    document.querySelectorAll(

        ".animate"

    ).forEach(element => {

        observer.observe(element);

    });

};



/* =====================================================
WINDOW TITLE
===================================================== */

SuperAdmin.setTitle = function (

    title

) {

    document.title =
        title +
        " | reInsight";

};



/* =====================================================
DATE & TIME
===================================================== */

SuperAdmin.initializeClock = function () {

    const clock =
        document.getElementById("liveClock");

    if (!clock)
        return;

    const update = () => {

        clock.innerHTML =
            new Date().toLocaleString();

    };

    update();

    setInterval(update, 1000);

};



/* =====================================================
NETWORK STATUS
===================================================== */

SuperAdmin.initializeNetwork = function () {

    window.addEventListener(

        "offline",

        () => {

            this.error(

                "Internet connection lost."

            );

        }

    );

    window.addEventListener(

        "online",

        () => {

            this.success(

                "Connection restored."

            );

        }

    );

};



/* =====================================================
DEVELOPER MODE
===================================================== */

SuperAdmin.debug = function (

    value

) {

    if (

        window.location.hostname ===

        "localhost"

    ) {

        console.log(value);

    }

};



/* =====================================================
PART 4 INITIALIZER
===================================================== */

const initPart3 = SuperAdmin.init;

SuperAdmin.init = function () {

    initPart3.call(this);

    this.initializeSession();

    this.initializeKeyboardShortcuts();

    this.initializeTheme();

    this.initializeAutoRefresh();

    this.initializeAnimations();

    this.initializeClock();

    this.initializeNetwork();

    this.debug("Super Admin Ready.");

};