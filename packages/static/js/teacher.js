/*
=========================================================
reInsight Teacher Dashboard
File: teacher.js
=========================================================
*/

"use strict";

/* =====================================================
GLOBAL APP
===================================================== */

const TeacherApp = {

    config: {
        sidebarKey: "reinsight_teacher_sidebar",
        themeKey: "reinsight_teacher_theme"
    },

    dom: {},

    init() {

        this.cacheDOM();

        this.initializeBootstrap();

        this.initializeSidebar();

        this.initializeActiveMenu();

        this.restoreSidebarState();

        this.initializeCounters();

        this.initializeProgressBars();

        this.initializeCharts();

        this.initializeTableSearch();

        this.initializeSelectAll();

        this.initializeQuickActions();

        this.initializeBackToTop();

        this.initializeTheme();

        this.bindEvents();

        console.log("Teacher Dashboard Initialized");
    },

    cacheDOM() {

        this.dom.sidebar =
            document.getElementById("teacherSidebar");

        this.dom.sidebarToggle =
            document.getElementById("teacherSidebarToggle");

        this.dom.overlay =
            document.getElementById("teacherSidebarOverlay");

        this.dom.backToTop =
            document.getElementById("backToTop");
    },

    initializeBootstrap() {

        document
            .querySelectorAll('[data-bs-toggle="tooltip"]')
            .forEach(el => new bootstrap.Tooltip(el));
    },

initializeSidebar() {

    if (!this.dom.sidebarToggle || !this.dom.sidebar)
        return;

    this.dom.sidebarToggle.addEventListener("click", () => {

        this.dom.sidebar.classList.toggle("show");

        this.dom.overlay?.classList.toggle("show");
    });

    this.dom.overlay?.addEventListener("click", () => {

        this.dom.sidebar.classList.remove("show");

        this.dom.overlay.classList.remove("show");
    });
},

    restoreSidebarState() {

        const collapsed =
            localStorage.getItem(this.config.sidebarKey);

        if (
            collapsed === "true" &&
            window.innerWidth > 991
        ) {

            this.dom.sidebar?.classList.add("collapsed");
        }
    },

    initializeActiveMenu() {

        const current =
            window.location.pathname;

        document
            .querySelectorAll(".teacher-menu .nav-link")
            .forEach(link => {

                const path =
                    new URL(link.href).pathname;

                if (current === path) {

                    link.classList.add("active");
                }
            });
    },

    initializeCounters() {

        document
            .querySelectorAll(".counter")
            .forEach(counter => {

                const target =
                    parseInt(counter.dataset.target || 0);

                const duration = 1200;

                const step =
                    target / (duration / 20);

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
    },

    initializeProgressBars() {

        document
            .querySelectorAll(".progress-bar[data-width]")
            .forEach(bar => {

                const width =
                    bar.dataset.width;

                bar.style.width = "0%";

                setTimeout(() => {

                    bar.style.width = width;

                }, 250);
            });
    },

    initializeCharts() {

        if (typeof Chart === "undefined")
            return;

        /* Performance Chart */

        const performance =
            document.getElementById("performanceChart");

        if (performance) {

            new Chart(performance, {

                type: "line",

                data: {

                    labels: [
                        "Mon",
                        "Tue",
                        "Wed",
                        "Thu",
                        "Fri"
                    ],

                    datasets: [{

                        label: "Average Score",

                        data: [
                            72,
                            75,
                            78,
                            80,
                            82
                        ],

                        borderColor: "#2563EB",

                        backgroundColor:
                            "rgba(37,99,235,.12)",

                        fill: true,

                        tension: .35
                    }]
                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false
                }
            });
        }

        /* Attendance Chart */

        const attendance =
            document.getElementById("teacherAttendanceChart");

        if (attendance) {

            new Chart(attendance, {

                type: "doughnut",

                data: {

                    labels: [
                        "Present",
                        "Absent",
                        "Late"
                    ],

                    datasets: [{

                        data: [
                            92,
                            5,
                            3
                        ],

                        backgroundColor: [
                            "#16A34A",
                            "#DC2626",
                            "#F59E0B"
                        ]
                    }]
                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false
                }
            });
        }
    },

    initializeTableSearch() {

        document
            .querySelectorAll(".table-search")
            .forEach(input => {

                input.addEventListener("keyup", function () {

                    const keyword =
                        this.value.toLowerCase();

                    const table =
                        document.querySelector(
                            this.dataset.table
                        );

                    if (!table)
                        return;

                    table
                        .querySelectorAll("tbody tr")
                        .forEach(row => {

                            row.style.display =
                                row.textContent
                                    .toLowerCase()
                                    .includes(keyword)
                                    ? ""
                                    : "none";
                        });
                });
            });
    },

    initializeSelectAll() {

        document
            .querySelectorAll(".check-all")
            .forEach(master => {

                master.addEventListener("change", function () {

                    const table =
                        document.querySelector(
                            this.dataset.table
                        );

                    table
                        ?.querySelectorAll(".row-check")
                        .forEach(box => {

                            box.checked =
                                master.checked;
                        });
                });
            });
    },

    initializeQuickActions() {

        document
            .querySelectorAll(".quick-action")
            .forEach(btn => {

                btn.addEventListener("click", function () {

                    console.log(
                        "Quick action:",
                        this.dataset.action
                    );
                });
            });
    },

    initializeBackToTop() {

        if (!this.dom.backToTop)
            return;

        window.addEventListener("scroll", () => {

            if (window.scrollY > 400) {

                this.dom.backToTop.classList.remove("d-none");

            } else {

                this.dom.backToTop.classList.add("d-none");
            }
        });

        this.dom.backToTop.addEventListener("click", () => {

            window.scrollTo({

                top: 0,

                behavior: "smooth"
            });
        });
    },

    initializeTheme() {

        const toggle =
            document.getElementById("themeToggle");

        const stored =
            localStorage.getItem(this.config.themeKey);

        if (stored === "dark") {

            document.body.classList.add("dark-mode");
        }

        toggle?.addEventListener("click", () => {

            document.body.classList.toggle("dark-mode");

            localStorage.setItem(
                this.config.themeKey,
                document.body.classList.contains("dark-mode")
                    ? "dark"
                    : "light"
            );
        });
    },

    toast(message, type = "primary") {

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
                <button class="btn-close"></button>
            </div>
        `;

        container.appendChild(toast);

        toast.querySelector(".btn-close")
            .addEventListener("click", () => toast.remove());

        setTimeout(() => toast.remove(), 4000);
    },

    bindEvents() {

        window.addEventListener("resize", () => {

            if (window.innerWidth > 991) {

                this.dom.sidebar?.classList.remove("show");

                this.dom.overlay?.classList.remove("show");
            }
        });
    }
};

/* =====================================================
HELPERS
===================================================== */

const TeacherUtils = {

    qs(selector) {

        return document.querySelector(selector);
    },

    qsa(selector) {

        return document.querySelectorAll(selector);
    },

    copy(text) {

        navigator.clipboard.writeText(text);
    }
};

/* =====================================================
READY
===================================================== */

document.addEventListener("DOMContentLoaded", () => {

    TeacherApp.init();
});

document.getElementById('markAllPresent')?.addEventListener('click', () => {
    document.querySelectorAll('input[value="present"]').forEach(r => r.checked = true);
});

document.getElementById('markAllLate')?.addEventListener('click', () => {
    document.querySelectorAll('input[value="late"]').forEach(r => r.checked = true);
});

document.getElementById('markAllAbsent')?.addEventListener('click', () => {
    document.querySelectorAll('input[value="absent"]').forEach(r => r.checked = true);
});