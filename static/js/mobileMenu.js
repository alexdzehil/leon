(function () {
    const openMobileMenu = document.querySelector('.openMobileMenu');
    const menuMobilePopup = document.querySelector('.menuMobilePopup');
    const menuMobile = document.querySelector('.menuMobile');

    openMobileMenu.addEventListener('click', function () {
        if (openMobileMenu.getAttribute('class').includes('activeMenu')) {
            openMobileMenu.classList.remove('activeMenu');
            document.body.classList.remove('lockBody');
            menuMobilePopup.classList.remove('activePopup');
        } else {
            openMobileMenu.classList.add('activeMenu');
            document.body.classList.add('lockBody');
            menuMobilePopup.classList.add('activePopup');
        }
    });

    const allLinks = menuMobile.querySelectorAll('.hardLink');

    [...allLinks].forEach(element => {
        element.addEventListener('click', function (e) {
            e.preventDefault();
            openMobileMenu.classList.remove('activeMenu');
            document.body.classList.remove('lockBody');
            menuMobilePopup.classList.remove('activePopup');
            location.hash = e.target.getAttribute('href');
        })
    });
})()