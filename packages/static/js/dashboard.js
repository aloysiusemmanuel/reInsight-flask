/* ==========================================================
   reInsight Dashboard
   Dashboard JavaScript
========================================================== */

"use strict";

/* ==========================================================
   DOM READY
========================================================== */

document.addEventListener("DOMContentLoaded", () => {

    Dashboard.init();

});

/* ==========================================================
   DASHBOARD OBJECT
========================================================== */

const Dashboard = {

    init() {

        this.cacheDOM();

        this.bindEvents();

        this.restoreSidebarState();

        this.initializeTooltips();

        this.initializePopovers();

        this.initializeCounters();

        this.initializeCharts();

        this.initializeSearch();

        this.initializeNotifications();

    },

    /* ======================================================
       CACHE DOM
    ====================================================== */

    cacheDOM() {

        this.body = document.body;

        this.sidebar = document.getElementById("sidebar");

        this.sidebarToggle = document.getElementById("sidebarToggle");

        this.sidebarOverlay = document.getElementById("sidebarOverlay");

        this.mainWrapper = document.getElementById("mainWrapper");

        this.searchInput = document.getElementById("dashboardSearch");

    },

    /* ======================================================
       EVENTS
    ====================================================== */

    bindEvents() {

        if (this.sidebarToggle) {

            this.sidebarToggle.addEventListener("click", () => {

                this.toggleSidebar();

            });

        }

        if (this.sidebarOverlay) {

            this.sidebarOverlay.addEventListener("click", () => {

                this.closeSidebar();

            });

        }

        window.addEventListener("resize", () => {

            this.handleResize();

        });

    },

    /* ======================================================
       SIDEBAR
    ====================================================== */

    toggleSidebar() {

        this.body.classList.toggle("sidebar-open");

        localStorage.setItem(

            "sidebar",

            this.body.classList.contains("sidebar-open")

        );

    },

    closeSidebar() {

        this.body.classList.remove("sidebar-open");

        localStorage.setItem("sidebar", false);

    },

    restoreSidebarState() {

        const state = localStorage.getItem("sidebar");

        if (state === "true") {

            this.body.classList.add("sidebar-open");

        }

    },

    handleResize() {

        if (window.innerWidth < 992) {

            this.body.classList.remove("sidebar-open");

        }

    },

    /* ======================================================
       TOOLTIPS
    ====================================================== */

    initializeTooltips() {

        const tooltips = document.querySelectorAll(

            '[data-bs-toggle="tooltip"]'

        );

        tooltips.forEach(el => {

            new bootstrap.Tooltip(el);

        });

    },

    /* ======================================================
       POPOVERS
    ====================================================== */

    initializePopovers() {

        const popovers = document.querySelectorAll(

            '[data-bs-toggle="popover"]'

        );

        popovers.forEach(el => {

            new bootstrap.Popover(el);

        });

    },

    /* ======================================================
       COUNTERS
    ====================================================== */

    initializeCounters() {

        const counters = document.querySelectorAll("[data-counter]");

        counters.forEach(counter => {

            const target = Number(counter.dataset.counter);

            let current = 0;

            const increment = Math.max(1, Math.ceil(target / 100));

            const timer = setInterval(() => {

                current += increment;

                if (current >= target) {

                    current = target;

                    clearInterval(timer);

                }

                counter.textContent = current.toLocaleString();

            }, 15);

        });

    },

    /* ======================================================
       SEARCH PLACEHOLDER
    ====================================================== */

    initializeSearch() {

        if (!this.searchInput) return;

        this.searchInput.addEventListener("keyup", function () {

            console.log("Searching:", this.value);

        });

    },

    /* ======================================================
       NOTIFICATIONS
    ====================================================== */

    initializeNotifications() {

        const alerts = document.querySelectorAll(".alert");

        alerts.forEach(alert => {

            setTimeout(() => {

                const instance = bootstrap.Alert.getOrCreateInstance(alert);

                instance.close();

            }, 5000);

        });

    },

    /* ======================================================
       CHARTS
    ====================================================== */

    initializeCharts() {

        if (typeof Chart === "undefined") return;

        this.attendanceChart();

        this.behaviourChart();

    },

    attendanceChart() {

        const canvas = document.getElementById("attendanceChart");

        if (!canvas) return;

        new Chart(canvas, {

            type: "line",

            data: {

                labels: [

                    "Mon",

                    "Tue",

                    "Wed",

                    "Thu",

                    "Fri"

                ],

                datasets: [

                    {

                        label: "Attendance",

                        data: [

                            96,

                            94,

                            97,

                            95,

                            98

                        ],

                        tension: 0.4,

                        fill: true

                    }

                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false

            }

        });

    },

    behaviourChart() {

        const canvas = document.getElementById("behaviourChart");

        if (!canvas) return;

        new Chart(canvas, {

            type: "doughnut",

            data: {

                labels: [

                    "Excellent",

                    "Good",

                    "Needs Attention"

                ],

                datasets: [

                    {

                        data: [

                            72,

                            20,

                            8

                        ]

                    }

                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false

            }

        });

    }

};