(() => {
  const root = document.querySelector(".slideshow");
  const track = root.querySelector(".slideshow__track");
  const slides = Array.from(root.querySelectorAll(".slideshow__slide"));
  const btnPrev = root.querySelector(".slideshow__btn--prev");
  const btnNext = root.querySelector(".slideshow__btn--next");
  const dotsWrap = root.querySelector(".slideshow__dots");

  let index = 0;
  const intervalMs = 4000;
  let timer = null;
  let isPointerDown = false,
    startX = 0,
    deltaX = 0;

  // Build dots
  slides.forEach((_, i) => {
    const b = document.createElement("button");
    b.type = "button";
    b.setAttribute("role", "tab");
    b.setAttribute("aria-label", `Go to slide ${i + 1}`);
    b.addEventListener("click", () => goTo(i, true));
    dotsWrap.appendChild(b);
  });

  function goTo(i, announce = false) {
    index = (i + slides.length) % slides.length;
    track.style.transform = `translateX(-${index * 100}%)`;
    [...dotsWrap.children].forEach((d, k) =>
      d.setAttribute("aria-selected", k === index ? "true" : "false")
    );
    if (announce) root.setAttribute("aria-live", "polite");
  }

  const next = () => goTo(index + 1);
  const prev = () => goTo(index - 1);

  // Autoplay
  const start = () => (timer = setInterval(next, intervalMs));
  const stop = () => timer && clearInterval(timer);
  root.addEventListener("mouseenter", stop);
  root.addEventListener("mouseleave", start);

  // Buttons
  btnNext.addEventListener("click", () => {
    stop();
    next();
    start();
  });
  btnPrev.addEventListener("click", () => {
    stop();
    prev();
    start();
  });

  // Keyboard
  root.tabIndex = 0;
  root.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") {
      stop();
      next();
      start();
    }
    if (e.key === "ArrowLeft") {
      stop();
      prev();
      start();
    }
  });

  // Touch / mouse swipe
  const onDown = (x) => {
    isPointerDown = true;
    startX = x;
    deltaX = 0;
    stop();
  };
  const onMove = (x) => {
    if (!isPointerDown) return;
    deltaX = x - startX;
  };
  const onUp = () => {
    if (!isPointerDown) return;
    isPointerDown = false;
    if (Math.abs(deltaX) > 50) deltaX < 0 ? next() : prev();
    start();
  };

  // Touch
  root.addEventListener("touchstart", (e) => onDown(e.touches[0].clientX), {
    passive: true,
  });
  root.addEventListener("touchmove", (e) => onMove(e.touches[0].clientX), {
    passive: true,
  });
  root.addEventListener("touchend", onUp);

  // Mouse
  root.addEventListener("mousedown", (e) => onDown(e.clientX));
  root.addEventListener("mousemove", (e) => onMove(e.clientX));
  document.addEventListener("mouseup", onUp);

  // Init
  goTo(0);
  start();
})();
