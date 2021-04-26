(function () {
    var doc = document.documentElement,
        body = document.body;

    // Highlight current navigation item
    // =================================
    var navigationItems = document.querySelectorAll(".sidebar-items-container .outer-link, .sidebar-items-container .inner-link");

    for (var i = 0; i < navigationItems.length; i++) {
        var el = navigationItems[i],
            re = new RegExp("^" + el.href);

        var isRoot = el.classList.contains("root");

        if (isRoot && el.href == location.href) {
            el.classList.add("active");
        } else if (re.test(location.href) && !isRoot) {
            el.classList.add("active");
        }
    }

    // Toggle the sidebar
    // ==================
    var menu = document.querySelector(".sidebar .menu");

    if (menu !== null) {
        menu.addEventListener("click", function () {
            var width = window.innerWidth || doc.clientWidth || body.clientWidth;

            if (width < 940) {
                body.classList.toggle("opened");
            } else {
                body.classList.toggle("closed");
            }
        });
    }

    // Toggle sidebar items
    // ====================
    var navigationHeaders = document.querySelectorAll(".sidebar-inner-container h5");

    for (var i = 0; i < navigationHeaders.length; i++) {
        var el = navigationHeaders[i];

        el.addEventListener("click", function (e) {
            // Click would target icon as well
            var p = e.target.className == ""
                ? e.target.parentElement
                : e.target.parentElement.parentElement;

            if (p.classList.contains("open")) {
                p.classList.toggle("open");
                p.classList.add("closed");
            } else if (p.classList.contains("closed")) {
                p.classList.toggle("closed");
                p.classList.add("open");
            }
        });
    }

    // Open last visited sidebar group
    // ======================================
    if (window.localStorage.history) {
        const savedSection = JSON.parse(window.localStorage.history);
        const course = document.querySelector("header.navigation h4").textContent;
        if (savedSection.course === course) {
            document.querySelectorAll(".sidebar-inner-container h5").forEach((element) => {
                if (element.textContent === savedSection.section) {
                    element.parentElement.classList.toggle("closed");
                    element.parentElement.classList.add("open");
                }
            });
        }
    }

    // Save last visited sidebar group
    // ======================================
    document.querySelectorAll(".sidebar-inner-container h5").forEach((element) => {
        element.addEventListener("click", function (e) {
            const lastVisitedSection = e.target.textContent;
            const course = document.querySelector("header.navigation h4").textContent;
            window.localStorage.history = JSON.stringify({
                section: lastVisitedSection,
                course: course
            });
        });
    });


    // Adds anchor to content headers (h1-h3)
    // ======================================
    function setHeaderAnchors() {
        var headers = document.querySelectorAll(".content h1, .content h2, .content h3");

        for (var i = 0, len = headers.length; i < len; i++) {
            if (headers[i].id) {
                var header = headers[i],
                    id = header.id,
                    anchor = document.createElement("a");

                anchor.href = "#" + id;
                anchor.className = "header-anchor icon-link";
                header.appendChild(anchor);
            }
        }
    }

    // Make external links open in a new tab
    // =====================================
    function setTargetBlankForLinks() {
        var anchors = document.getElementsByTagName("a"),
            re1 = new RegExp("^https://mau-webb.github.io");
        re2 = new RegExp("^http://localhost");

        for (var i = 0, len = anchors.length; i < len; i++) {
            var anchor = anchors[i];

            if (!re1.test(anchor.href) && !re2.test(anchor.href)) {
                anchor.target = "_blank";
            }
        }
    }

    window.onload = function () {
        setHeaderAnchors();
        setTargetBlankForLinks();
    };
})();
