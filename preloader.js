(function(){
  var el = document.getElementById('preloader');
  if (!el) return;

  // Bot / crawler detection — skip preloader for bots
  if ((/bot|google|yandex|baidu|bing|msn|duckduckbot|teoma|slurp|crawler|spider|robot|crawling|facebook|twitter|linkedin/i.test(navigator.userAgent))) {
    el.style.display = 'none';
    return;
  }

  // Show preloader only once per session (first page load)
  if (typeof sessionStorage !== 'undefined' && sessionStorage.getItem('_visited') === 'y') {
    el.style.display = 'none';
    return;
  }

  var svg = el.querySelector('.preloader-svg');
  var MIN_SHOW_MS = 1500;
  var startTime = Date.now();
  var hidden = false;

  // Start SVG animation after 200ms
  setTimeout(function(){
    if (svg && !el.classList.contains('hidden')) svg.classList.add('animate');
  }, 200);

  function hide() {
    if (hidden) return;
    hidden = true;
    el.classList.add('hidden');
    setTimeout(function(){
      el.classList.add('hidden-done');
    }, 400);
    // Mark session as visited so next page load skips preloader
    try { sessionStorage.setItem('_visited', 'y'); } catch(e) {}
  }

  function tryHide() {
    var elapsed = Date.now() - startTime;
    if (elapsed < MIN_SHOW_MS) {
      setTimeout(tryHide, MIN_SHOW_MS - elapsed);
      return;
    }
    hide();
  }

  // Wait for nav to finish rendering, then hide
  var check = setInterval(function(){
    if (window.Nav && Nav._rendered) {
      clearInterval(check);
      clearTimeout(fallback);
      tryHide();
    }
  }, 100);

  var fallback = setTimeout(function(){
    clearInterval(check);
    if (!hidden) tryHide();
  }, 3000);
})();
