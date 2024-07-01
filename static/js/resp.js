function toggleMenu() {
  var menu = document.querySelector('.menu');
  var closeToggle = document.querySelector('.close-toggle');
  var bars = document.querySelectorAll('.bar');

  menu.classList.toggle('active');

  // Fermer le menu si la croix est cliquée
  if (menu.classList.contains('active')) {
    closeToggle.addEventListener('click', function() {
      menu.classList.remove('active');
      bars.forEach(function(bar) {
        bar.style.transform = 'none';
      });
    });
  } else {
    bars.forEach(function(bar) {
      bar.style.transform = 'none';
    });
  }
}
