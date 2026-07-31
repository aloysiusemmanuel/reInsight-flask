/**
 * =========================================================
 * reInsight Parent Dashboard
 * =========================================================
 */

class ParentDashboard {

    constructor() {

        this.dom = {
            sidebar: document.getElementById("parentSidebar"),
            sidebarToggle: document.getElementById("parentSidebarToggle"),
            overlay: document.getElementById("parentSidebarOverlay"),
            backToTop: document.getElementById("backToTop")
        };

        this.init();
    }

    init() {

        this.initializeSidebar();
        this.initializeBackToTop();
        this.initializeAlerts();
        this.initializeTooltips();
        this.initializeActiveLinks();
        this.handleResize();
    }

    /* =====================================================
       SIDEBAR
    ====================================================== */

    initializeSidebar() {

        if (!this.dom.sidebar || !this.dom.sidebarToggle) return;

        this.dom.sidebarToggle.addEventListener("click", () => {

            this.dom.sidebar.classList.toggle("show");
            this.dom.overlay?.classList.toggle("show");
        });

        this.dom.overlay?.addEventListener("click", () => {

            this.closeSidebar();
        });

        // Close sidebar when a link is clicked on mobile
        this.dom.sidebar.querySelectorAll(".nav-link").forEach(link => {

            link.addEventListener("click", () => {

                if (window.innerWidth < 992) {

                    this.closeSidebar();
                }
            });
        });
    }

    closeSidebar() {

        this.dom.sidebar?.classList.remove("show");
        this.dom.overlay?.classList.remove("show");
    }

    /* =====================================================
       BACK TO TOP
    ====================================================== */

    initializeBackToTop() {

        if (!this.dom.backToTop) return;

        window.addEventListener("scroll", () => {

            if (window.scrollY > 300) {

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
    }

    /* =====================================================
       AUTO HIDE ALERTS
    ====================================================== */

    initializeAlerts() {

        const alerts = document.querySelectorAll(".alert-dismissible");

        alerts.forEach(alert => {

            setTimeout(() => {

                const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
                bsAlert.close();

            }, 5000);
        });
    }

    /* =====================================================
       BOOTSTRAP TOOLTIPS
    ====================================================== */

    initializeTooltips() {

        const tooltipTriggerList = [].slice.call(
            document.querySelectorAll('[data-bs-toggle="tooltip"]')
        );

        tooltipTriggerList.map(trigger => new bootstrap.Tooltip(trigger));
    }

    /* =====================================================
       ACTIVE MENU LINK
    ====================================================== */

    initializeActiveLinks() {

        const currentPath = window.location.pathname;

        document.querySelectorAll(".parent-menu .nav-link").forEach(link => {

            const href = link.getAttribute("href");

            if (href && currentPath === href) {

                document
                    .querySelectorAll(".parent-menu .nav-link")
                    .forEach(l => l.classList.remove("active"));

                link.classList.add("active");
            }
        });
    }

    /* =====================================================
       RESPONSIVE HANDLING
    ====================================================== */

    handleResize() {

        window.addEventListener("resize", () => {

            if (window.innerWidth >= 992) {

                this.closeSidebar();
            }
        });
    }

    /* =====================================================
       TOAST HELPER
    ====================================================== */

    static showToast(message, type = "primary") {

        const container = document.getElementById("toastContainer");

        if (!container) return;

        const toast = document.createElement("div");

        toast.className = `toast align-items-center text-bg-${type} border-0 mb-2`;

        toast.setAttribute("role", "alert");

        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button"
                        class="btn-close btn-close-white me-2 m-auto"
                        data-bs-dismiss="toast"></button>
            </div>
        `;

        container.appendChild(toast);

        const bsToast = new bootstrap.Toast(toast, {
            delay: 4000
        });

        bsToast.show();

        toast.addEventListener("hidden.bs.toast", () => toast.remove());
    }
}

/* =========================================================
INIT
========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    window.parentDashboard = new ParentDashboard();
});

/* =========================================================
GLOBAL HELPERS
========================================================= */

// Example usage:
// showSuccess("Report downloaded successfully");

window.showSuccess = (message) =>
    ParentDashboard.showToast(message, "success");

window.showError = (message) =>
    ParentDashboard.showToast(message, "danger");

window.showInfo = (message) =>
    ParentDashboard.showToast(message, "info");

window.showWarning = (message) =>
    ParentDashboard.showToast(message, "warning");