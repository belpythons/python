document.addEventListener('DOMContentLoaded', function () {
    const sections = document.querySelectorAll('.section');
    const links = document.querySelectorAll('.navbar a');

    // Mengatur efek scroll
    function scrollToSection(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        targetSection.scrollIntoView({ behavior: 'smooth' });
    }

    // Menambahkan event listener untuk setiap tautan
    links.forEach(link => {
        link.addEventListener('click', scrollToSection);
    });

    // Animasi saat menggulir
    window.addEventListener('scroll', () => {
        const scrollPos = window.scrollY + window.innerHeight;

        sections.forEach(section => {
            if (scrollPos > section.offsetTop + section.offsetHeight / 4) {
                section.classList.add('active');
            }
        });
    });
});
