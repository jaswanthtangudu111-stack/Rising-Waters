// ======================================
// Rising Waters JavaScript
// ======================================

// Navbar Shadow on Scroll

window.addEventListener("scroll", function () {

    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 50) {

        navbar.style.boxShadow = "0 10px 30px rgba(0,0,0,0.15)";

    } else {

        navbar.style.boxShadow = "none";

    }

});

// Smooth Scroll

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        document.querySelector(this.getAttribute("href"))
            .scrollIntoView({

                behavior: "smooth"

            });

    });

});

// Number Input Validation

document.querySelectorAll("input[type='number']").forEach(input => {

    input.addEventListener("input", function () {

        if (this.value < 0)
            this.value = 0;

        if (this.value > 20)
            this.value = 20;

    });

});

// Fade Animation

const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.classList.add("show");

        }

    });

});

document.querySelectorAll(".feature-card,.input-card,.about-card,.result-card").forEach(card => {

    observer.observe(card);

});