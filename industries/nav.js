var INDUSTRIES = [
  { name: 'Restaurant Automation', path: 'avtomatizaciya-restoranov.html' },
  { name: 'Construction Software', path: 'po-stroitelnye-kompanii.html' },
  { name: 'Medical CRM', path: 'crm-medcentry.html' },
  { name: 'Logistics & Freight', path: 'sistemy-logistika.html' },
  { name: 'SaaS for Startups', path: 'saas-startupy.html' },
  { name: 'Manufacturing ERP', path: 'erp-proizvodstvo.html' },
  { name: 'Agriculture Systems', path: 'selskokhozyaystvo.html' },
  { name: 'Fitness Apps', path: 'fitness-apps.html' },
  { name: 'E-Learning Platforms', path: 'online-obuchenie.html' },
  { name: 'Hotel Booking Systems', path: 'bronirovanie-gostinits.html' },
  { name: 'Real Estate CRM', path: 'crm-nedvizhimost.html' },
  { name: 'Remote Work Tools', path: 'udalennaya-rabota.html' },
  { name: 'Marketing Analytics', path: 'marketing-analitika.html' },
  { name: 'Cybersecurity', path: 'kiberbezopasnost.html' },
  { name: 'Project Management', path: 'upravlenie-proektami.html' },
  { name: 'Freelance Platforms', path: 'platforma-frilans.html' },
  { name: 'Smart Home IoT', path: 'iot-umnyy-dom.html' },
  { name: 'Crowdfunding Platforms', path: 'kraudfanding.html' },
  { name: 'Supply Chain Management', path: 'upravlenie-cepochkami.html' },
  { name: 'Legal Software', path: 'pravovie-firmu.html' },
  { name: 'Auto Service Software', path: 'avtoservice.html' },
  { name: 'Food Delivery Platforms', path: 'dostavka-edы.html' }
];

function initIndustriesNav(currentPath) {
  var base = '/industries/';
  var desktopNav = document.getElementById('industriesNav');
  var mobileNav = document.getElementById('industriesNavMobile');

  if (mobileNav) {
    var extraLinks = [
      { name: 'На главную mobiap.com', href: '/' },
      { name: 'Industries', href: '/industries/' }
    ];
    extraLinks.forEach(function(e) {
      var a = document.createElement('a');
      a.href = e.href;
      a.textContent = e.name;
      var li = document.createElement('li');
      li.className = 'nav-extra-link';
      li.appendChild(a);
      mobileNav.appendChild(li);
    });
    var sep = document.createElement('li');
    sep.className = 'nav-separator';
    mobileNav.appendChild(sep);
  }

  INDUSTRIES.forEach(function(t) {
    var isActive = t.path === currentPath;
    var link = document.createElement('a');
    link.href = base + t.path;
    link.textContent = t.name;
    if (isActive) link.className = 'nav-active';
    var li = document.createElement('li');
    li.appendChild(link);
    if (desktopNav) {
      desktopNav.appendChild(li.cloneNode(true));
    }
    if (mobileNav) {
      mobileNav.appendChild(li.cloneNode(true));
    }
  });
}
