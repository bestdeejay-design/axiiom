(function(w){
var cfg = w.AXIIOM_CONFIG || {};
var c = cfg.company || {};
var year = new Date().getFullYear();
var start = c.copyrightStart || 2024;
document.getElementById('footerCopy').innerHTML =
  '<p class="copy">' +
    '<a href="/" class="footer-link">' + (c.shortName || 'AXIIOM') + '</a> · ' +
    '<a href="/#services" class="footer-link">Услуги</a> · ' +
    '<a href="/calculator/" class="footer-link">Калькулятор</a> · ' +
    '<a href="/demo/app/" class="footer-link">Демо</a> · ' +
    '<a href="/tools/" class="footer-link">Инструменты</a>' +
  '</p>' +
  '<p class="copy" style="font-size:.7rem;margin-top:8px;border:none;padding-top:0;">' +
    '<a href="/privacy/" class="footer-link">Политика конфиденциальности</a> · ' +
    '<a href="/terms/" class="footer-link">Пользовательское соглашение</a>' +
  '</p>' +
  '<p class="copy" style="font-size:.65rem;margin-top:8px;border:none;padding-top:0;text-transform:none;letter-spacing:0;">' +
    '\u00A9 ' + start + '\u2013' + year + ' ' + (c.name || 'AXIIOM') + ' (' + (c.nameRu || 'ООО Аксиома') + '). Все права защищены.' +
  '</p>';
})(window);
