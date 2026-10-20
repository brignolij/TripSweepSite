/* Lightbox for the PhotoCull screenshots: a click on an <a class="window-frame"> opens the image in a modal on the same page
   (Esc, a click outside or the close button close it; arrows go to the previous/next screenshot). Without JavaScript the link
   simply opens the image file. */
(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('a.window-frame'));
  if (!links.length) return;

  var LABELS = {
    en: ['Close', 'Previous screenshot', 'Next screenshot'],
    fr: ['Fermer', 'Capture précédente', 'Capture suivante'],
    it: ['Chiudi', 'Schermata precedente', 'Schermata successiva'],
    de: ['Schließen', 'Vorheriger Screenshot', 'Nächster Screenshot'],
    es: ['Cerrar', 'Captura anterior', 'Captura siguiente']
  };
  var labels = LABELS[(document.documentElement.lang || 'en').slice(0, 2)] || LABELS.en;

  var overlay = document.createElement('div');
  overlay.className = 'lightbox';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-modal', 'true');
  overlay.hidden = true;
  overlay.innerHTML =
    '<button type="button" class="lightbox-close" aria-label="' + labels[0] + '">&times;</button>' +
    '<button type="button" class="lightbox-nav lightbox-prev" aria-label="' + labels[1] + '">&#8249;</button>' +
    '<figure class="lightbox-figure"><img alt="" /><figcaption></figcaption></figure>' +
    '<button type="button" class="lightbox-nav lightbox-next" aria-label="' + labels[2] + '">&#8250;</button>';
  document.body.appendChild(overlay);

  var img = overlay.querySelector('img');
  var caption = overlay.querySelector('figcaption');
  var closeButton = overlay.querySelector('.lightbox-close');
  var current = 0;
  var opener = null;

  function show(index) {
    current = (index + links.length) % links.length;
    var source = links[current].querySelector('img');
    img.src = links[current].getAttribute('href');
    img.alt = source ? source.alt : '';
    caption.textContent = img.alt;
  }

  function open(index, trigger) {
    opener = trigger;
    show(index);
    overlay.hidden = false;
    document.body.classList.add('lightbox-open');
    closeButton.focus();
  }

  function close() {
    overlay.hidden = true;
    document.body.classList.remove('lightbox-open');
    img.removeAttribute('src');
    if (opener) opener.focus();
  }

  links.forEach(function (link, index) {
    link.addEventListener('click', function (event) {
      event.preventDefault();
      open(index, link);
    });
  });

  overlay.addEventListener('click', function (event) {
    if (event.target === overlay || event.target.classList.contains('lightbox-figure')) close();
  });
  closeButton.addEventListener('click', close);
  overlay.querySelector('.lightbox-prev').addEventListener('click', function () { show(current - 1); });
  overlay.querySelector('.lightbox-next').addEventListener('click', function () { show(current + 1); });

  document.addEventListener('keydown', function (event) {
    if (overlay.hidden) return;
    if (event.key === 'Escape') close();
    else if (event.key === 'ArrowLeft') show(current - 1);
    else if (event.key === 'ArrowRight') show(current + 1);
  });
})();
