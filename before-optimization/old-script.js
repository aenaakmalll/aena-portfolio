// ==========================================================
// MOBILE / FULL-SCREEN NAV MENU
// Toggles a class on <body> which style.css uses to show/hide
// the full-screen nav overlay and animate the hamburger icon.
// ==========================================================
const menuToggle = document.getElementById('menuToggle');
const navOverlay = document.getElementById('navOverlay');

menuToggle.addEventListener('click', () => {
  const isOpen = document.body.classList.toggle('nav-open');
  menuToggle.setAttribute('aria-expanded', isOpen);
  menuToggle.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
});

// Close the menu automatically when a nav link is clicked
// (otherwise the overlay would stay open after jumping to a section)
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    document.body.classList.remove('nav-open');
    menuToggle.setAttribute('aria-expanded', false);
    menuToggle.setAttribute('aria-label', 'Open menu');
  });
});

// ==========================================================
// GALLERY LIGHTBOX (only present on project case-study pages)
// Clicking a gallery thumbnail opens the full-size image;
// clicking the X, the dark background, or pressing Escape closes it.
// ==========================================================
const lightbox = document.getElementById('lightbox');

if (lightbox) {
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxClose = document.getElementById('lightboxClose');

  document.querySelectorAll('.gallery-item').forEach(item => {
    item.addEventListener('click', () => {
      lightboxImg.src = item.dataset.full;
      lightboxImg.alt = item.querySelector('img').alt;
      lightbox.classList.add('is-open');
    });
  });

  function closeLightbox() {
    lightbox.classList.remove('is-open');
    lightboxImg.src = '';
  }

  lightboxClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightbox();
  });
}

// ==========================================================
// FOOTER YEAR
// Automatically keeps the copyright year in the footer up to date
// so you never have to edit it by hand.
// ==========================================================
document.getElementById('year').textContent = new Date().getFullYear();


