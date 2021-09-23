(function () {
    const popupSliderGallery = new Splide( '.gallerySplidePopup' ).mount();

    const galleryPhoto = document.querySelectorAll('.galleryPhoto');

    [...galleryPhoto].forEach(el => {
        el.addEventListener('click', function () {
          window.dispatchEvent(new Event('resize'));
          const popupGallery = document.body.querySelector('.popupGallery');
          popupSliderGallery.go(Number(el.getAttribute('data-id')) - 1);

          popupGallery.classList.add('popupGalleryActive');
          document.body.classList.add('overlayBody');
        });
    });

    const closePopupGallery = document.querySelector('.closePopupGallery');

    closePopupGallery.addEventListener('click', function () {
        const popupGallery = document.body.querySelector('.popupGallery');

        popupGallery.classList.remove('popupGalleryActive');
        document.body.classList.remove('overlayBody');
    });
})()