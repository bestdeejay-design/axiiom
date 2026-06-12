// SPA Demo Template — Mobile App Data & Render Functions

// Data stored in memory — edit with your own content
const appData = {
  profile: {
    name: 'Jane Doe',
    group: 'CS-401',
    faculty: 'Faculty of Computer Science',
    course: 3,
    form: 'Full-time',
    email: 'jane.doe@university.edu',
    phone: '+1 (555) 123-4567',
    avatar: 'JD',
    qrCode: 'DOE.J\\CS-401\\2025',
    room: 'Dorm 3, Room 412',
    subscriptions: {
      clubs: ['it', 'science'],
      eventCategories: ['schedule', 'clubs', 'institute']
    }
  },
  
  transcript: [
    { name: 'Mathematics', hours: 144, semester: 1, type: 'Exam', grade: '5', date: '15.01.2025' },
    { name: 'Physics', hours: 108, semester: 1, type: 'Exam', grade: '4', date: '17.01.2025' },
    { name: 'Computer Science', hours: 108, semester: 1, type: 'Credit', grade: 'passed', date: '20.12.2024' },
    { name: 'History', hours: 72, semester: 1, type: 'Credit', grade: 'passed', date: '22.12.2024' },
    { name: 'Mathematics', hours: 108, semester: 2, type: 'Exam', grade: '5', date: '15.06.2025' },
    { name: 'Programming', hours: 144, semester: 2, type: 'Exam', grade: '5', date: '18.06.2025' },
    { name: 'English Language', hours: 72, semester: 2, type: 'Credit', grade: 'passed', date: '20.05.2025' },
    { name: 'Physical Education', hours: 36, semester: 2, type: 'Credit', grade: 'passed', date: '25.05.2025' },
    { name: 'Algorithms & Data Structures', hours: 108, semester: 3, type: 'Exam', grade: '4', date: '' },
    { name: 'Databases', hours: 108, semester: 3, type: 'Credit', grade: 'passed', date: '' },
    { name: 'Probability Theory', hours: 72, semester: 3, type: 'Exam', grade: '', date: '' },
    { name: 'Networks & Telecommunications', hours: 72, semester: 3, type: 'Credit', grade: '', date: '' }
  ],
  
  schedule: [
    { time: '09:00', name: 'Algorithms', room: 'Room 101', current: true },
    { time: '11:00', name: 'Databases', room: 'Room 204', current: false },
    { time: '14:00', name: 'Probability Theory', room: 'Lab 3', current: false }
  ],
  
  scheduleFull: {
    '2025-05-18': [
      { day: 'Monday', time: '09:00', name: 'Algorithms & Data Structures', type: 'Lecture', room: 'Room 201', teacher: 'Prof. Smith J.' },
      { day: 'Monday', time: '11:00', name: 'Databases', type: 'Lab', room: 'Lab 3', teacher: 'Dr. Johnson K.' },
      { day: 'Monday', time: '14:00', name: 'Probability Theory', type: 'Practice', room: 'Room 105', teacher: 'Asst. Williams M.' },
      { day: 'Tuesday', time: '09:00', name: 'Networks & Telecommunications', type: 'Lab', room: 'Lab 5', teacher: 'Dr. Brown T.' },
      { day: 'Tuesday', time: '11:00', name: 'Algorithms & Data Structures', type: 'Practice', room: 'Lab 2', teacher: 'Prof. Smith J.' },
      { day: 'Wednesday', time: '09:00', name: 'Databases', type: 'Lecture', room: 'Room 204', teacher: 'Dr. Johnson K.' },
      { day: 'Wednesday', time: '11:00', name: 'Foreign Language', type: 'Practice', room: 'Room 301', teacher: 'Lect. Davis O.' },
      { day: 'Thursday', time: '10:00', name: 'Probability Theory', type: 'Lecture', room: 'Room 105', teacher: 'Asst. Williams M.' },
      { day: 'Thursday', time: '14:00', name: 'Networks & Telecommunications', type: 'Lecture', room: 'Room 102', teacher: 'Dr. Brown T.' },
      { day: 'Friday', time: '09:00', name: 'Databases', type: 'Practice', room: 'Lab 3', teacher: 'Dr. Johnson K.' },
      { day: 'Friday', time: '11:00', name: 'Physical Education', type: 'Practice', room: 'Gym', teacher: 'Coach Wilson D.' }
    ],
    '2025-05-25': [
      { day: 'Monday', time: '09:00', name: 'Algorithms & Data Structures', type: 'Practice', room: 'Lab 1', teacher: 'Prof. Smith J.' },
      { day: 'Monday', time: '11:00', name: 'Databases', type: 'Lab', room: 'Lab 3', teacher: 'Dr. Johnson K.' },
      { day: 'Monday', time: '14:00', name: 'Probability Theory', type: 'Lecture', room: 'Room 105', teacher: 'Asst. Williams M.' },
      { day: 'Tuesday', time: '09:00', name: 'Networks & Telecommunications', type: 'Lecture', room: 'Room 102', teacher: 'Dr. Brown T.' },
      { day: 'Tuesday', time: '11:00', name: 'Algorithms & Data Structures', type: 'Lab', room: 'Lab 2', teacher: 'Prof. Smith J.' },
      { day: 'Wednesday', time: '09:00', name: 'Databases', type: 'Lecture', room: 'Room 204', teacher: 'Dr. Johnson K.' },
      { day: 'Wednesday', time: '11:00', name: 'Foreign Language', type: 'Practice', room: 'Room 301', teacher: 'Lect. Davis O.' },
      { day: 'Thursday', time: '10:00', name: 'Probability Theory', type: 'Practice', room: 'Room 105', teacher: 'Asst. Williams M.' },
      { day: 'Thursday', time: '14:00', name: 'Networks & Telecommunications', type: 'Lab', room: 'Lab 5', teacher: 'Dr. Brown T.' },
      { day: 'Friday', time: '09:00', name: 'Databases', type: 'Practice', room: 'Lab 3', teacher: 'Dr. Johnson K.' },
      { day: 'Friday', time: '11:00', name: 'Physical Education', type: 'Practice', room: 'Gym', teacher: 'Coach Wilson D.' }
    ]
  },
  
  chats: [
    { name: "Dean's Office", lastMsg: 'Schedule updated', time: '12:30', icon: '<svg class="icon" style="width:18px;height:18px"><use href="#icon-wallet-giftcard"/></svg>' },
    { name: 'Advisor Miller', lastMsg: 'See you tomorrow', time: '11:15', icon: '<svg class="icon" style="width:18px;height:18px"><use href="#icon-user"/></svg>' },
    { name: 'Student Council', lastMsg: 'Hackathon announced', time: 'Yesterday', icon: '<svg class="icon" style="width:18px;height:18px"><use href="#icon-union"/></svg>' },
    { name: 'Student Union', lastMsg: 'Poll: choose topic', time: 'Yesterday', icon: '<svg class="icon" style="width:18px;height:18px"><use href="#icon-megaphone"/></svg>' }
  ],
  
  careers: [
    { company: 'TechCorp', position: 'Software Engineer Intern', salary: '$50K', location: 'New York', type: 'Internship' },
    { company: 'DataSystems', position: 'ML Engineer', salary: '$80K', location: 'San Francisco', type: 'Full-time' },
    { company: 'WebStudio', position: 'Frontend Developer', salary: '$100K', location: 'Remote', type: 'Full-time' }
  ],
  
  benefits: [
    { name: '50% off at cafeteria', desc: 'Show student ID', valid: 'until 30.06' },
    { name: 'Transport pass', desc: 'Student transit pass $60', valid: 'active' },
    { name: 'Student cinema discount', desc: 'Up to 30% off at cinemas', valid: 'active' }
  ],
  
  events: [
    { name: 'Consultation: Databases', date: 'May 14', time: '14:00', place: 'A-301', type: 'Consultation', category: 'schedule', club: null },
    { name: 'Exam: Machine Learning', date: 'May 22', time: '10:00', place: 'A-201', type: 'Exam', category: 'schedule', club: null },
    { name: 'Credit: Web Development', date: 'Jun 10', time: '14:00', place: 'B-205', type: 'Credit', category: 'schedule', club: null },
    { name: 'Programming Olympiad', date: 'May 18', time: '12:00', place: 'Lab 201', type: 'Contest', category: 'schedule', club: null },
    { name: 'Volleyball Tournament', date: 'May 16', time: '18:00', place: 'Gym', type: 'Sports', category: 'clubs', club: 'Sports Club' },
    { name: 'Song Club Concert', date: 'May 15', time: '19:00', place: 'Assembly Hall', type: 'Concert', category: 'clubs', club: 'Song Club' },
    { name: 'Python Meetup', date: 'May 19', time: '18:30', place: 'Lab 201', type: 'Meetup', category: 'clubs', club: 'IT Club' },
    { name: 'AI Future Discussion', date: 'May 21', time: '18:00', place: 'Conference Room', type: 'Discussion', category: 'clubs', club: 'Debate Club' },
    { name: 'Photo Walk Downtown', date: 'May 17', time: '12:00', place: 'Meeting at entrance', type: 'Creative', category: 'clubs', club: 'Art Club' },
    { name: 'Debate Tournament', date: 'May 23', time: '18:00', place: 'Conference Room', type: 'Debate', category: 'clubs', club: 'Debate Club' },
    { name: 'Hackathon: AI Projects', date: 'May 24', time: '10:00', place: 'Lab 201', type: 'Hackathon', category: 'clubs', club: 'IT Club' },
    { name: 'Science Club Meeting', date: 'May 20', time: '16:00', place: 'Library', type: 'Science', category: 'clubs', club: 'Science Club' },
    { name: 'Open Day', date: 'May 18', time: '14:00', place: 'Assembly Hall', type: 'Event', category: 'institute', club: null },
    { name: 'Field Trip to TechCorp', date: 'May 25', time: '16:00', place: 'TechCorp HQ', type: 'Excursion', category: 'institute', club: null },
    { name: 'Alumni Meetup', date: 'May 30', time: '18:00', place: 'Assembly Hall', type: 'Event', category: 'institute', club: null },
    { name: 'Energy Day', date: 'May 28', time: '14:00', place: 'Robotics Lab', type: 'Science', category: 'science', club: 'Energy Club' },
    { name: 'English Speaking Club', date: 'May 22', time: '18:00', place: 'Room 215', type: 'Languages', category: 'clubs', club: 'Language Club' },
    { name: 'Schedule Change', date: 'May 15', time: '09:00', place: '-', type: 'Announcement', category: 'dekanat', club: null },
    { name: 'Exam Session Starts June 1', date: 'May 12', time: '11:00', place: '-', type: 'Announcement', category: 'dekanat', club: null },
    { name: 'Professional Courses Sign-up', date: 'May 20', time: '10:00', place: "Dean's Office", type: 'Announcement', category: 'dekanat', club: null },
    { name: 'Career Fair', date: 'May 26', time: '14:00', place: 'Assembly Hall', type: 'Career', category: 'career', club: null },
    { name: 'HR Meet & Greet', date: 'May 27', time: '16:00', place: 'Conference Room', type: 'Career', category: 'career', club: null }
  ],
  
  aboutInstitute: {
    title: 'About University Demo',
    founded: 1900,
    age: 125,
    address: '123 University Ave, Demo City',
    stats: {
      students: '15,000+',
      teachers: '1,200+',
      departments: '50',
      postgraduate: '150+',
      academicians: '100+',
      faculties: '6'
    },
    description: 'University Demo is a leading educational institution offering programs in science, engineering, humanities, and business.',
    history: 'Founded in 1900, University Demo has grown from a small college to a comprehensive research university serving over 15,000 students across six faculties.',
    famousGraduates: [
      { name: 'John Smith', role: 'Nobel Laureate in Physics' },
      { name: 'Jane Williams', role: 'Founder of TechCorp' },
      { name: 'Robert Brown', role: 'Academy Award-winning filmmaker' }
    ],
    honoraryProfessors: [
      { year: 2000, name: 'Dr. Alan Turing', country: 'UK', role: 'Computer Science Pioneer' },
      { year: 2005, name: 'Dr. Marie Curie', country: 'France', role: 'Nobel Laureate in Chemistry' },
      { year: 2010, name: 'Dr. Richard Feynman', country: 'USA', role: 'Nobel Laureate in Physics' }
    ],
    faculties: [
      { name: '1. Faculty of Computer Science', desc: 'Software engineering, AI, data science' },
      { name: '2. Faculty of Engineering', desc: 'Mechanical, electrical, civil engineering' },
      { name: '3. Faculty of Sciences', desc: 'Physics, chemistry, biology, mathematics' },
      { name: '4. Faculty of Humanities', desc: 'Literature, philosophy, languages' },
      { name: '5. Faculty of Business', desc: 'Economics, management, finance' },
      { name: '6. Faculty of Arts', desc: 'Design, music, fine arts' }
    ]
  },

  navigator: {
    buildings: [
      { id: '1', name: 'Main Building', address: '123 University Ave', floors: ['Floor 2: Rooms 201-214', 'Floor 3: Rooms 301-314', 'Floor 4: Rooms 401-414'] },
      { id: '2', name: 'Building 2', address: '125 University Ave', floors: ['Floor 2: Continuing Education', 'Floor 1: Student Services'] },
      { id: '3', name: 'Science Building', address: '127 University Ave', floors: ['Floor 1: Labs 101-110', 'Floor 2: Lecture Halls'] }
    ],
    faculties: [
      { name: 'Computer Science', building: 'Main Building', floor: 'Floor 4' },
      { name: 'Engineering', building: 'Main Building', floor: 'Floor 3' },
      { name: 'Sciences', building: 'Science Building', floor: 'Floor 2' },
      { name: 'Humanities', building: 'Building 2', floor: 'Floor 2' },
      { name: 'Business', building: 'Building 2', floor: 'Floor 1' },
      { name: 'Arts', building: 'Main Building', floor: 'Floor 2' }
    ],
    pointsOfInterest: [
      { name: 'Main Library', icon: 'book', location: 'Main Building, Floor 1' },
      { name: 'Student Cafeteria', icon: 'meal', location: 'Building 2, Floor 1' },
      { name: 'Tech Lab', icon: 'tech', location: 'Science Building, Floor 1' },
      { name: 'Assembly Hall', icon: 'theater', location: 'Main Building, Floor 1' },
      { name: 'Sports Complex', icon: 'soccer', location: 'Behind Main Building' }
    ]
  },
  
  notes: [
    {
      subject: 'Databases',
      icon: 'folder',
      topics: [
        { title: 'Normalization', content: '1NF, 2NF, 3NF. Dependencies and anomalies.', updated: 'May 12' },
        { title: 'SQL Queries', content: 'SELECT, JOIN, GROUP BY, aggregate functions', updated: 'May 10' },
        { title: 'Indexes', content: 'B-tree, hash indexes, query optimization', updated: 'May 8' }
      ]
    },
    {
      subject: 'Machine Learning',
      icon: 'robot',
      topics: [
        { title: 'Linear Regression', content: 'Least squares method, gradient descent', updated: 'May 11' },
        { title: 'Classification', content: 'SVM, decision trees, random forest', updated: 'May 9' },
        { title: 'Neural Networks', content: 'Perceptron, backpropagation', updated: 'May 5' }
      ]
    },
    {
      subject: 'Web Development',
      icon: 'web',
      topics: [
        { title: 'HTML/CSS', content: 'Semantic markup, Flexbox, Grid', updated: 'May 14' },
        { title: 'JavaScript', content: 'Async, Promises, async/await', updated: 'May 13' },
        { title: 'React', content: 'Components, state, useState, useEffect hooks', updated: 'May 7' }
      ]
    }
  ],
    
  services: {
    moodle: 'https://lms.university.edu',
    payment: 'Tuition Payment'
  },
  
  alumni: {
    profile: {
      name: 'Jane Doe',
      graduationYear: 2018,
      specialty: 'Computer Science',
      photo: 'JD',
      work: {
        company: 'TechCorp',
        position: 'Senior Developer',
        since: '2020'
      },
      careerHistory: [
        { company: 'TechCorp', position: 'Senior Developer', years: '2020-present' },
        { company: 'Startup Inc.', position: 'Developer', years: '2018-2020' }
      ],
      email: 'jane.doe@email.com',
      phone: '+1 (555) 123-4567',
      linkedin: '',
      about: 'University Demo graduate of 2018. Working at TechCorp on backend development.'
    },
    subscriptions: {
      meetings: true,
      instituteNews: true,
      endowment: true
    },
    events: [
      {
        id: 1,
        title: 'Class of 2018 Reunion',
        date: 'June 15, 2026',
        time: '18:00',
        place: 'Assembly Hall',
        type: 'meeting',
        attendees: 45,
        maxAttendees: 100,
        registered: false,
        description: 'Ten-year reunion for the Class of 2018. Meet your classmates and professors!'
      },
      {
        id: 2,
        title: 'Research Vice-Dean Meet & Greet',
        date: 'June 20, 2026',
        time: '16:00',
        place: 'Conference Room',
        type: 'institute_meeting',
        attendees: 28,
        maxAttendees: 50,
        registered: false,
        description: 'Meet the Vice-Dean for Research. Discuss research projects and alumni involvement opportunities.'
      },
      {
        id: 3,
        title: 'Alumni IT Networking Night',
        date: 'June 25, 2026',
        time: '19:00',
        place: 'Coworking Space',
        type: 'aeho',
        attendees: 60,
        maxAttendees: 80,
        registered: false,
        description: 'Networking event for IT alumni. Exchange experience, job opportunities.'
      },
      {
        id: 4,
        title: 'Open Day Volunteer',
        date: 'June 28, 2026',
        time: '10:00',
        place: 'Main Building',
        type: 'volunteer',
        attendees: 12,
        maxAttendees: 20,
        registered: false,
        description: 'Help with organizing the university Open Day as a volunteer.'
      },
      {
        id: 5,
        title: 'Robotics Lab Tour',
        date: 'July 1, 2026',
        time: '14:00',
        place: 'Science Building',
        type: 'tour',
        attendees: 25,
        maxAttendees: 30,
        registered: false,
        description: 'Guided tour of the updated robotics laboratory. Explore modern developments.'
      }
    ],
    endowment: {
      totalRaised: 15000000,
      currency: '$',
      programs: [
        {
          id: 1,
          name: 'Scholarships for Talented Students',
          target: 10000000,
          raised: 5200000,
          description: 'Annual scholarships for the best students',
          active: true
        },
        {
          id: 2,
          name: '125th Anniversary Fund (2025)',
          target: 50000000,
          raised: 8500000,
          description: 'Fundraising for the 125th anniversary celebrations',
          active: true
        },
        {
          id: 3,
          name: 'Science Lab Renovation',
          target: 5000000,
          raised: 2100000,
          description: 'Modern equipment for science laboratories',
          active: true
        },
        {
          id: 4,
          name: 'Sports Development Fund',
          target: 1000000,
          raised: 450000,
          description: 'Support for sports clubs and competitions',
          active: true
        }
      ]
    },
    wallOfFame: {
      outstandingAlumni: [
        { name: 'John Smith', year: 2010, achievement: 'Founder of TechCorp', bio: 'Founded TechCorp, a leading tech company. Graduate of 2010, Faculty of Computer Science.' },
        { name: 'Anna Miller', year: 2008, achievement: 'Professor of Sciences', bio: 'PhD, Professor, Academy of Sciences member' },
        { name: 'David Brown', year: 2012, achievement: 'CEO of AI-Tech startup', bio: 'Founder and CEO of AI-Tech, a leading AI company' }
      ],
      awardWinners: [
        { name: 'Jane Doe', year: 2018, award: 'National Science Award' },
        { name: 'Maria Johnson', year: 2016, award: 'Young Scientists Medal' }
      ]
    }
  }
};

// Navigation history
let history = ['home'];

// Theme management
function toggleTheme() {
  const html = document.documentElement;
  const currentTheme = html.getAttribute('data-theme');
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  html.setAttribute('data-theme', newTheme);
  
  // Update theme icons
  updateThemeIcons(newTheme);
  
  // Save preference
  localStorage.setItem('univerid-theme', newTheme);
}

function updateThemeIcons(theme) {
  // Update sun/moon icons based on theme
  document.querySelectorAll('.theme-toggle .icon, .theme-toggle-small .icon-sm').forEach(icon => {
    const use = icon.querySelector('use');
    if (use) {
      use.setAttribute('href', theme === 'light' ? '#icon-moon' : '#icon-sun');
    }
  });
}

function loadTheme() {
  const saved = localStorage.getItem('univerid-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  updateThemeIcons(saved);
}

// User mode: student or graduate
let userMode = localStorage.getItem('univerid_userMode') || 'student';

function toggleUserMode() {
  const toggle = document.getElementById('modeToggle');
  userMode = userMode === 'student' ? 'graduate' : 'student';
  localStorage.setItem('univerid_userMode', userMode);
  
  if (toggle) {
    toggle.style.left = userMode === 'graduate' ? '30px' : '2px';
  }
}

function initUserMode() {
  userMode = localStorage.getItem('univerid_userMode') || 'student';
  const toggle = document.getElementById('modeToggle');
  if (toggle) {
    toggle.style.left = userMode === 'graduate' ? '30px' : '2px';
  }
  
  // Обновить заголовок кнопки QR
  const qrBtn = document.getElementById('headerQrBtn');
  if (qrBtn) {
    qrBtn.title = userMode === 'graduate' ? 'Event Pass' : 'Dormitory Access';
  }
  
  // Обновить нижнюю навигацию
  updateBottomNav();
}

function updateBottomNav() {
  const studentNav = document.querySelectorAll('.student-nav');
  const graduateNav = document.querySelectorAll('.graduate-nav');
  
  if (userMode === 'graduate') {
    studentNav.forEach(el => el.style.display = 'none');
    graduateNav.forEach(el => el.style.display = '');
  } else {
    studentNav.forEach(el => el.style.display = '');
    graduateNav.forEach(el => el.style.display = 'none');
  }
}

function handleHeaderQR() {
  if (userMode === 'graduate') {
    showPage('alumni-profile');
  } else {
    showPage('qr');
  }
}

function handleProfileClick() {
  if (userMode === 'graduate') {
    showPage('alumni-profile');
  } else {
    showPage('profile');
  }
}

// Navigation
function openApp() {
  document.getElementById('landing').classList.add('hidden');
  document.getElementById('app').classList.remove('hidden');
  localStorage.setItem('univerid_appOpen', 'true');
  updateBottomNav();
  showPage('home');
}

function closeApp() {
  document.getElementById('landing').classList.remove('hidden');
  document.getElementById('app').classList.add('hidden');
  history = ['home'];
  localStorage.setItem('univerid_appOpen', 'false');
}

function showPage(pageName, btnElement) {
  if (btnElement) {
    document.querySelectorAll('.nav-item').forEach(btn => btn.classList.remove('active'));
    btnElement.classList.add('active');
  }
  
  history.push(pageName);
  updateHeader(pageName);
  renderContent(pageName);
  
  // Save to localStorage
  localStorage.setItem('univerid_lastPage', pageName);
  localStorage.setItem('univerid_history', JSON.stringify(history));
  
  // Update back button visibility
  document.getElementById('backBtn').classList.toggle('hidden', history.length <= 1);
}

function goBack() {
  if (history.length > 1) {
    history.pop();
    const prevPage = history[history.length - 1];
    updateHeader(prevPage);
    renderContent(prevPage);
    
    // Save history to localStorage
    localStorage.setItem('univerid_lastPage', prevPage);
    localStorage.setItem('univerid_history', JSON.stringify(history));
    
    // If going back to home, close the app
    if (history.length === 1) {
      localStorage.removeItem('univerid_lastPage');
      localStorage.removeItem('univerid_history');
      localStorage.setItem('univerid_appOpen', 'false');
    }
    
    document.getElementById('backBtn').classList.toggle('hidden', history.length <= 1);
  }
}

function updateHeader(pageName) {
  const titles = {
    home: 'Home',
    grades: 'Grades',
    schedule: 'Schedule',
    chat: 'Messages',
    profile: 'Profile',
    qr: 'Access',
    career: 'Career',
    benefits: 'Benefits',
    eventsfeed: 'Events',
    'alumni-profile': 'My Profile',
    'alumni-events': 'Events',
    'alumni-endowment': 'Endowment Fund',
    'alumni-fame': 'Wall of Fame',
    'alumni-network': 'Alumni Network'
  };
  document.getElementById('appTitle').textContent = titles[pageName] || 'Home';
}

function renderContent(pageName) {
  const content = document.getElementById('content');
  
  // Если выпускник - показываем Alumni Home вместо обычного home
  if (pageName === 'home' && userMode === 'graduate') {
    content.innerHTML = renderAlumniHome();
  } else if (pageName === 'home') {
    content.innerHTML = renderHome();
  } else if (pageName === 'grades') {
    content.innerHTML = renderGrades();
  } else if (pageName === 'schedule') {
    content.innerHTML = renderSchedule();
  } else if (pageName === 'chat') {
    content.innerHTML = renderChat();
  } else if (pageName === 'profile') {
    content.innerHTML = renderProfile();
  } else if (pageName === 'qr') {
    content.innerHTML = renderQR();
  } else if (pageName === 'career') {
    content.innerHTML = renderCareer();
  } else if (pageName === 'benefits') {
    content.innerHTML = renderBenefits();
  } else if (pageName === 'eventsfeed') {
    content.innerHTML = renderEventsFeed();
  } else if (pageName === 'attendance') {
    content.innerHTML = renderAttendance();
  } else if (pageName === 'session') {
    content.innerHTML = renderSession();
  } else if (pageName === 'navigator') {
    content.innerHTML = renderNavigator();
  } else if (pageName === 'cards') {
    content.innerHTML = renderCards();
  } else if (pageName === 'clubs') {
    content.innerHTML = renderClubs();
  } else if (pageName === 'notes') {
    content.innerHTML = renderNotes();
  } else if (pageName === 'about') {
    content.innerHTML = renderAbout();
  } else if (pageName === 'alumni-profile') {
    content.innerHTML = renderAlumniProfile();
  } else if (pageName === 'alumni-events') {
    content.innerHTML = renderAlumniEvents();
  } else if (pageName === 'alumni-endowment') {
    content.innerHTML = renderAlumniEndowment();
  } else if (pageName === 'alumni-fame') {
    content.innerHTML = renderAlumniFame();
  } else if (pageName === 'alumni-network') {
    content.innerHTML = renderAlumniNetwork();
  }
}

function renderHome() {
  // Calculate stats from transcript
  const exams = appData.transcript.filter(t => t.type === 'Exam');
  const tests = appData.transcript.filter(t => t.type === 'Credit');
  const completed = appData.transcript.filter(t => t.grade !== '');
  
  const examAvg = exams.length > 0 
    ? (exams.reduce((sum, g) => sum + (g.grade ? parseInt(g.grade) : 0), 0) / exams.filter(g => g.grade).length) 
    : 0;
  
  const passedCredits = completed.reduce((sum, g) => sum + (g.hours / 36), 0);
  
  const modulesHtml = `
    <div class="modules-scroll">
      <div class="module-tile" onclick="showPage('attendance')">
        <svg class="icon"><use href="#icon-clock"/></svg>
        <span>Attendance</span>
      </div>
      <div class="module-tile" onclick="showPage('session')">
        <svg class="icon"><use href="#icon-clipboard"/></svg>
        <span>Session</span>
      </div>
      <div class="module-tile" onclick="showPage('navigator')">
        <svg class="icon"><use href="#icon-map"/></svg>
        <span>Navigator</span>
      </div>
<div class="module-tile" onclick="showPage('clubs')">
        <svg class="icon"><use href="#icon-clubs"/></svg>
        <span>Clubs</span>
      </div>
      <div class="module-tile" onclick="showPage('notes')">
        <svg class="icon"><use href="#icon-notes"/></svg>
        <span>Notes</span>
      </div>
      </div>
  `;
  
  const eventsHtml = `
    <div class="events-feed">
      <h3>Upcoming Events</h3>
      ${appData.events.map(e => `
        <div class="event-item">
          <div class="event-date">
            <span class="event-day">${e.date.split(' ')[0].replace(/[^\d]/g, '')}</span>
            <span class="event-month">${e.date.split(' ')[1] || ''}</span>
          </div>
          <div class="event-info">
            <h4>${e.name}</h4>
            <p>${e.time} • ${e.place}</p>
          </div>
          <span class="event-type">${e.type}</span>
        </div>
      `).join('')}
    </div>
  `;
  
  return `
    <div class="page-content">
      <div class="dashboard-grid">
        <div class="dashboard-card wide accent" style="grid-column:span 2" onclick="showPage('grades')">
          <div style="display:flex;align-items:center;gap:16px">
            <div style="flex:1">
               <svg class="icon" style="margin-bottom:8px"><use href="#icon-chart"/></svg>
               <h4>Academic Performance</h4>
               <p style="font-size:24px;font-weight:700">${examAvg > 0 ? examAvg.toFixed(1) : '—'} <span style="font-size:14px;font-weight:400">/ 5.0</span></p>
             </div>
             <div style="flex:1;border-left:1px solid rgba(255,255,255,0.1);padding-left:16px">
               <svg class="icon" style="margin-bottom:8px"><use href="#icon-book"/></svg>
               <h4>Hours</h4>
               <p style="font-size:24px;font-weight:700">${appData.transcript.reduce((s, g) => s + g.hours, 0)} <span style="font-size:14px;font-weight:400">h.</span></p>
            </div>
          </div>
        </div>
        
        <div class="dashboard-card" onclick="showPage('attendance')">
          <svg class="icon"><use href="#icon-clock"/></svg>
          <h4>Attend.</h4>
          <p>96%</p>
        </div>
        
        <div class="dashboard-card" onclick="showPage('chat')">
          <svg class="icon"><use href="#icon-chat"/></svg>
          <h4>Chat</h4>
          <p>${appData.chats.length}</p>
        </div>
      </div>
      
      <div class="dashboard-card wide accent" style="margin-top:12px" onclick="showPage('session')">
        <div style="display:flex;align-items:center;gap:12px">
          <svg class="icon" style="font-size:32px"><use href="#icon-clipboard"/></svg>
          <div>
            <h4>Until Session</h4>
            <div style="font-size:28px;font-weight:700;color:var(--accent)">7 days</div>
            <p style="font-size:12px;color:var(--text-muted);margin:4px 0 0">Next exam: Databases (May 18)</p>
          </div>
        </div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.1)">
          <div style="text-align:center">
            <div style="font-size:18px;font-weight:600">3</div>
            <div style="font-size:10px;color:var(--text-muted)">exams</div>
          </div>
          <div style="text-align:center">
            <div style="font-size:18px;font-weight:600">4</div>
            <div style="font-size:10px;color:var(--text-muted)">credits</div>
          </div>
          <div style="text-align:center">
            <div style="font-size:18px;font-weight:600">14</div>
            <div style="font-size:10px;color:var(--text-muted)">days</div>
          </div>
        </div>
      </div>
      
      ${modulesHtml}
      
      <div class="dashboard-card wide" style="margin-top:12px" onclick="showPage('about')">
        <div style="display:flex;align-items:center;gap:12px">
          <svg class="icon" style="font-size:32px"><use href="#icon-about"/></svg>
          <div>
            <h4>About</h4>
            <div style="font-size:14px;color:var(--text-muted)">University Demo</div>
            <p style="font-size:12px;color:var(--text-muted);margin:4px 0 0">15,000+ students &bull; 6 faculties &bull; 50 departments</p>
          </div>
        </div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.1)">
          <div style="text-align:center">
            <div style="font-size:18px;font-weight:600">1900</div>
            <div style="font-size:10px;color:var(--text-muted)">founded</div>
          </div>
          <div style="text-align:center">
            <div style="font-size:18px;font-weight:600">125</div>
            <div style="font-size:10px;color:var(--text-muted)">years</div>
          </div>
          <div style="text-align:center">
            <div style="font-size:18px;font-weight:600">100K+</div>
            <div style="font-size:10px;color:var(--text-muted)">alumni</div>
          </div>
        </div>
      </div>
      
      ${eventsHtml}
    </div>
  `;
}

function renderGrades() {
  const transcript = appData.transcript;
  const semesters = [...new Set(transcript.map(t => t.semester))].sort((a, b) => b - a);
  
  let html = '<div class="page-content">';
  
  const exams = transcript.filter(t => t.type === 'Exam' && t.grade);
  const passedExams = exams.filter(t => t.grade !== '2');
  const avg = passedExams.length > 0 
    ? (passedExams.reduce((sum, g) => sum + parseInt(g.grade), 0) / passedExams.length).toFixed(1) 
    : '—';
  
  const totalHours = transcript.reduce((s, g) => s + g.hours, 0);
  const totalCredits = Math.round(totalHours / 36);
  const passedCredits = transcript.filter(t => t.grade && (t.type === 'Credit' ? t.grade === 'passed' : t.grade !== '2'))
    .reduce((s, g) => s + g.hours, 0) / 36;
  
  html += `
    <div class="transcript-header">
      <div class="stat-box">
        <span class="stat-label">GPA</span>
        <span class="stat-value">${avg}</span>
      </div>
      <div class="stat-box">
        <span class="stat-label">Hours</span>
        <span class="stat-value">${totalHours}</span>
      </div>
      <div class="stat-box">
        <span class="stat-label">Credits</span>
        <span class="stat-value">${passedCredits}/${totalCredits}</span>
      </div>
    </div>
  `;
  
  // Group by semester
  semesters.forEach(sem => {
    const items = transcript.filter(t => t.semester === sem);
    const semesterHours = items.reduce((s, g) => s + g.hours, 0);
    const semesterCredits = Math.round(semesterHours / 36);
    const examsInSem = items.filter(t => t.type === 'Exam');
    const semAvg = examsInSem.filter(e => e.grade).length > 0
      ? (examsInSem.filter(e => e.grade).reduce((s, g) => s + parseInt(g.grade), 0) / examsInSem.filter(e => e.grade).length).toFixed(1)
      : '—';
    
    html += `
      <div class="semester-block">
        <div class="semester-header">
          <span class="semester-num">Semester ${sem}</span>
          <span class="semester-stats">${semesterHours} h. / ${semesterCredits} cr.</span>
        </div>
        <div class="transcript-table">
          <div class="table-header">
            <span>Subject</span>
            <span>H.</span>
            <span>Grade</span>
          </div>
    `;
    
    items.forEach(item => {
      const isExam = item.type === 'Exam';
      const grade = item.grade || '—';
      const gradeClass = !grade ? '' : isExam 
        ? (grade === '5' ? 'grade-5' : grade === '4' ? 'grade-4' : grade === '3' ? 'grade-3' : grade === '2' ? 'grade-2' : '')
        : (grade === 'passed' ? 'passed' : grade === 'failed' ? 'failed' : '');
      
      html += `
        <div class="table-row">
          <span class="discipline-name">
            <strong>${item.name}</strong>
            <small>${item.type}</small>
          </span>
          <span>${item.hours}</span>
          <span class="grade-cell ${gradeClass}">${grade}</span>
        </div>
      `;
    });
    
    if (parseFloat(semAvg) > 0) {
      html += `
        <div class="semester-avg">
          Semester GPA: <strong>${semAvg}</strong>
        </div>
      `;
    }
    
    html += '</div></div>';
  });
  
  html += '</div>';
  return html;
}

function renderSchedule() {
  const dates = Object.keys(appData.scheduleFull);
  const currentWeek = dates[0];
  
  const weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  
  let html = `
    <div class="page-content">
      <div class="week-selector">
        <button class="week-btn active" onclick="showWeek('${currentWeek}', this)">
          <span class="week-label">This Week</span>
          <span class="week-dates">${currentWeek.replace('2025-', '')} — ${dates[0].split('-')[1]} May</span>
        </button>
        <button class="week-btn" onclick="showWeek('${dates[1]}', this)">
          <span class="week-label">Next Week</span>
          <span class="week-dates">${dates[1].replace('2025-', '')} — ${dates[1].split('-')[1]} May</span>
        </button>
      </div>
      <div class="schedule-week" id="scheduleWeek">
  `;
  
  const lessons = appData.scheduleFull[currentWeek];
  let currentDay = '';
  
  lessons.forEach((l, i) => {
    if (l.day !== currentDay) {
      if (currentDay) html += '</div>';
      currentDay = l.day;
      html += `
        <div class="schedule-day">
          <div class="day-header">${l.day}</div>
          <div class="day-lessons">
      `;
    }
    const isNow = l.time === '09:00' && l.day === 'Monday';
    html += `
      <div class="lesson-item ${isNow ? 'current' : ''}">
        <div class="lesson-time">${l.time}</div>
        <div class="lesson-info">
          <h4>${l.name}</h4>
          <p>${l.type} • ${l.room} • ${l.teacher}</p>
        </div>
      </div>
    `;
  });
  
  html += `
          </div>
        </div>
      </div>
    </div>
  `;
  
  return html;
}

function showWeek(weekKey, btn) {
  // В реальном приложении здесь был бы переход на другую неделю
  document.querySelectorAll('.week-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  
  // Показываем данные другой недели (упрощено)
  const lesson = appData.scheduleFull[weekKey]?.[0];
  if (lesson) {
    alert('Switching to week: ' + weekKey + '\n\nThe demo only shows one week.');
  }
}

function renderChat() {
  let html = '<div class="page-content"><h3>Chats</h3><div class="chat-list">';
  
  const avatars = {"Dean's Office": '<svg class="icon" style="width:18px;height:18px"><use href="#icon-wallet-giftcard"/></svg>', 'Advisor Miller': '<svg class="icon" style="width:18px;height:18px"><use href="#icon-user"/></svg>', 'Student Council': '<svg class="icon" style="width:18px;height:18px"><use href="#icon-union"/></svg>', 'Student Union': '<svg class="icon" style="width:18px;height:18px"><use href="#icon-megaphone"/></svg>'};
  appData.chats.forEach(c => {
    const avatar = avatars[c.name] || '<svg class="icon" style="width:18px;height:18px"><use href="#icon-user"/></svg>';
    html += `
      <div class="chat-item">
        <div class="chat-avatar">${avatar}</div>
        <div class="chat-info">
          <h4>${c.name}</h4>
          <p>${c.lastMsg}</p>
        </div>
        <div class="chat-time">${c.time}</div>
      </div>
    `;
  });
  
  html += '</div></div>';
  return html;
}

function renderProfile() {
  const p = appData.profile;
  const subs = p.subscriptions;
  
  const eventCategories = [
    { id: 'schedule', name: '<svg class="icon" style="width:18px;height:18px"><use href="#icon-calendar"/></svg> Schedule', desc: 'Exams, credits, consultations' },
    { id: 'dekanat', name: '<svg class="icon" style="width:18px;height:18px"><use href="#icon-wallet-giftcard"/></svg> Dean\'s Office', desc: 'Announcements from the dean\'s office' },
    { id: 'institute', name: '<svg class="icon" style="width:18px;height:18px"><use href="#icon-wallet-giftcard"/></svg> Institute', desc: 'Institute-wide events' },
    { id: 'clubs', name: '<svg class="icon" style="width:18px;height:18px"><use href="#icon-target"/></svg> Clubs', desc: 'Club events' },
    { id: 'career', name: '<svg class="icon" style="width:18px;height:18px"><use href="#icon-briefcase"/></svg> Career', desc: 'Jobs, fairs' },
    { id: 'science', name: '<svg class="icon" style="width:18px;height:18px"><use href="#icon-science"/></svg> Science', desc: 'Conferences, research' }
  ];
  
  const clubs = [
    { id: 'sports', name: 'Sports Club', icon: 'soccer' },
    { id: 'songs', name: 'Song Club', icon: 'music' },
    { id: 'it', name: 'IT Club', icon: 'school' },
    { id: 'art', name: 'Art Workshop', icon: 'palette' },
    { id: 'debate', name: 'Debate Club', icon: 'speech' },
    { id: 'science', name: 'Science Society', icon: 'science' },
    { id: 'energy', name: 'Energy Club', icon: 'lightning' },
    { id: 'languages', name: 'Language Club', icon: 'globe' }
  ];
  
  return `
    <div class="page-content">
      <div class="profile-card">
        <div class="profile-avatar">${p.avatar}</div>
        <h3>${p.name}</h3>
        <p class="profile-group">${p.group}</p>
      </div>
      
      <div class="profile-info">
        <div class="info-row">
          <span class="info-label">Faculty</span>
          <span class="info-value">${p.faculty}</span>
        </div>
        <div class="info-row">
          <span class="info-label">Year</span>
          <span class="info-value">${p.course}</span>
        </div>
        <div class="info-row">
          <span class="info-label">Type</span>
          <span class="info-value">${p.form}</span>
        </div>
        <div class="info-row">
          <span class="info-label">Email</span>
          <span class="info-value">${p.email}</span>
        </div>
        <div class="info-row">
          <span class="info-label">Phone</span>
          <span class="info-value">${p.phone}</span>
        </div>
      </div>
      
      <!-- Подписки на события -->
      <div style="margin-top:20px">
        <h4 style="font-size:16px;margin-bottom:12px"><svg class="icon" style="width:18px;height:18px;margin-right:8px;vertical-align:middle"><use href="#icon-bell"/></svg>Event Subscriptions</h4>
        <p style="font-size:12px;color:var(--text-muted);margin-bottom:12px">Choose event categories for your feed</p>
        <div style="display:flex;flex-direction:column;gap:8px">
          ${eventCategories.map(cat => `
            <div class="dashboard-card" style="padding:10px 12px;cursor:pointer" onclick="toggleCategory('${cat.id}')">
              <div style="display:flex;justify-content:space-between;align-items:center">
                <div>
                  <div style="font-size:14px;font-weight:600">${cat.name}</div>
                  <div style="font-size:11px;color:var(--text-muted)">${cat.desc}</div>
                </div>
                <div style="width:40px;height:22px;border-radius:11px;background:${subs.eventCategories.includes(cat.id) ? 'var(--primary)' : 'rgba(255,255,255,0.15)'};position:relative;transition:0.3s">
                  <div style="width:18px;height:18px;background:#fff;border-radius:50%;position:absolute;top:2px;${subs.eventCategories.includes(cat.id) ? 'right:2px' : 'left:2px'};transition:0.3s"></div>
                </div>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
      
      <!-- Мои клубы -->
      <div style="margin-top:20px">
        <h4 style="font-size:16px;margin-bottom:12px"><svg class="icon" style="width:18px;height:18px;margin-right:8px;vertical-align:middle"><use href="#icon-target"/></svg>My Clubs</h4>
        <p style="font-size:12px;color:var(--text-muted);margin-bottom:12px">Join clubs to participate in events</p>
        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:8px">
          ${clubs.map(club => {
            const isMember = subs.clubs.includes(club.id);
            return `
              <div class="dashboard-card" style="padding:12px;text-align:center;cursor:pointer;${isMember ? 'border:2px solid var(--primary)' : ''}" onclick="toggleClub('${club.id}')">
                <div style="margin-bottom:6px"><svg class="icon" style="width:24px;height:24px"><use href="#icon-${club.icon}"/></svg></div>
                <div style="font-size:12px;font-weight:600">${club.name}</div>
                <div style="font-size:10px;color:${isMember ? 'var(--primary)' : 'var(--text-muted)'};margin-top:4px">${isMember ? 'Joined' : '+ Join'}</div>
              </div>
            `;
          }).join('')}
        </div>
      </div>
    </div>
  `;
}

function renderQR() {
  const p = appData.profile;
  return `
    <div class="page-content">
      <div class="qr-card">
        <div class="qr-code">
            <img src="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'><rect width='200' height='200' fill='%231e293b'/><text x='100' y='110' text-anchor='middle' fill='%23a855f7' font-size='48' font-family='monospace'>QR</text></svg>" style="width:200px;height:200px;object-fit:contain" alt="QR code">
        </div>
        <p class="qr-name">${p.name}</p>
        <p class="qr-group">${p.group}</p>
        <p class="qr-room">${p.room}</p>
      </div>
      <p class="qr-hint">Show QR code at dormitory entrance</p>
    </div>
  `;
}

function openMoodle() {
  window.open(appData.services.moodle, '_blank');
}

function openPayment() {
    alert('Tuition Payment\n\nStudent: ' + appData.profile.name + '\nGroup: ' + appData.profile.group);
}

function renderCareer() {
  return `
    <div class="page-content">
      <h3>Jobs & Internships</h3>
      <div class="list">
        ${appData.careers.map(c => `
          <div class="list-item">
            <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-briefcase"/></svg></div>
            <div class="list-info">
              <h4>${c.position}</h4>
              <p>${c.company} • ${c.location}</p>
              <span class="salary">${c.salary}</span>
            </div>
            <span class="badge">${c.type}</span>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

function renderBenefits() {
  return `
    <div class="page-content">
      <h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-tag"/></svg>Benefits & Discounts</h3>
      <div class="list">
        ${appData.benefits.map(b => `
          <div class="list-item">
            <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-tag"/></svg></div>
            <div class="list-info">
              <h4>${b.name}</h4>
              <p>${b.desc}</p>
              <span class="valid">${b.valid}</span>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

function renderEventsFeed() {
  const examEvents = appData.events.filter(e => e.type === 'Exam' || e.type === 'Credit' || e.type === 'Consultation');
  const clubEvents = appData.events.filter(e => e.club);
  const otherEvents = appData.events.filter(e => !e.club && e.type !== 'Exam' && e.type !== 'Credit' && e.type !== 'Consultation');
  
  let html = '<div class="page-content">';
  
  // Сессия
  if (examEvents.length > 0) {
    html += '<h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-doc"/></svg>Exam Session</h3>';
    html += '<div class="events-full">';
    examEvents.forEach(e => {
      html += `
        <div class="event-card" style="border-left:3px solid var(--primary)">
          <div class="event-date-card">
            <span class="day">${e.date.split(' ')[0].replace(/[^\d]/g, '')}</span>
            <span class="month">${e.date.split(' ')[1] || ''}</span>
          </div>
          <div class="event-details">
            <h4>${e.name}</h4>
            <p>${e.time} • ${e.place}</p>
            <span class="event-type" style="background:var(--primary)">${e.type}</span>
          </div>
        </div>
      `;
    });
    html += '</div>';
  }
  
  // Клубы
  if (clubEvents.length > 0) {
    html += '<h3 style="margin-top:20px"><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-target"/></svg>Clubs & Societies</h3>';
    html += '<div class="events-full">';
    clubEvents.forEach(e => {
      html += `
        <div class="event-card" style="border-left:3px solid var(--accent)">
          <div class="event-date-card">
            <span class="day">${e.date.split(' ')[0].replace(/[^\d]/g, '')}</span>
            <span class="month">${e.date.split(' ')[1] || ''}</span>
          </div>
          <div class="event-details">
            <h4>${e.name}</h4>
            <p>${e.time} • ${e.place}</p>
            <span class="event-type" style="background:var(--secondary)">${e.type}</span>
            ${e.club ? `<span style="font-size:11px;color:var(--text-muted);display:block;margin-top:4px"><svg class="icon" style="width:12px;height:12px;margin-right:4px;vertical-align:middle"><use href="#icon-tag"/></svg>${e.club}</span>` : ''}
          </div>
        </div>
      `;
    });
    html += '</div>';
  }
  
  // Общие
  if (otherEvents.length > 0) {
    html += '<h3 style="margin-top:20px"><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-calendar"/></svg>Events</h3>';
    html += '<div class="events-full">';
    otherEvents.forEach(e => {
      html += `
        <div class="event-card">
          <div class="event-date-card">
            <span class="day">${e.date.split(' ')[0].replace(/[^\d]/g, '')}</span>
            <span class="month">${e.date.split(' ')[1] || ''}</span>
          </div>
          <div class="event-details">
            <h4>${e.name}</h4>
            <p>${e.time} • ${e.place}</p>
            <span class="event-type">${e.type}</span>
          </div>
        </div>
      `;
    });
    html += '</div>';
  }
  
  html += '</div>';
  return html;
}

function renderAttendance() {
  return `
    <div class="page-content">
      <h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-chart"/></svg>Attendance</h3>
      <div class="stats-grid" style="grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:20px">
        <div class="dashboard-card">
          <div class="stat-label">Attended</div>
          <div class="stat-value" style="color:#22c55e">142/156</div>
        </div>
        <div class="dashboard-card">
          <div class="stat-label">Percentage</div>
          <div class="stat-value" style="color:#22c55e">91%</div>
        </div>
      </div>
      <div class="list">
        <div class="list-item">
          <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-check"/></svg></div>
          <div class="list-info">
            <h4>Databases</h4>
            <p>12/12 attended</p>
          </div>
        </div>
        <div class="list-item">
          <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-check"/></svg></div>
          <div class="list-info">
            <h4>Web Development</h4>
            <p>11/12 attended</p>
          </div>
        </div>
        <div class="list-item">
          <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-alert-circle"/></svg></div>
          <div class="list-info">
            <h4>Operating Systems</h4>
            <p>10/12 attended</p>
          </div>
        </div>
      </div>
    </div>
  `;
}

function renderSession() {
  return `
    <div class="page-content">
      <h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-clipboard"/></svg>Winter Session</h3>
      <div class="dashboard-card accent" style="margin-bottom:20px">
        <div class="stat-label">Until session starts</div>
        <div class="stat-value" style="color:#f59e0b">7 days</div>
      </div>
      <h4>Exams</h4>
      <div class="list">
        <div class="list-item">
          <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-book"/></svg></div>
          <div class="list-info">
            <h4>Databases</h4>
            <p>Dec 18, 10:00, A-301</p>
          </div>
        </div>
        <div class="list-item">
          <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-book"/></svg></div>
          <div class="list-info">
            <h4>Machine Learning</h4>
            <p>Dec 22, 14:00, A-201</p>
          </div>
        </div>
      </div>
      <h4>Credits</h4>
      <div class="list">
        <div class="list-item">
          <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-check"/></svg></div>
          <div class="list-info">
            <h4>Web Development</h4>
            <p>Jan 10, ready</p>
          </div>
        </div>
      </div>
    </div>
  `;
}

function renderNavigator() {
  const nav = appData.navigator;
  let html = '<div class="page-content">';
  html += '<h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-map"/></svg>Campus Navigator</h3>';
  
  html += '<h4><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-building"/></svg>Buildings</h4>';
  html += '<div class="list">';
  nav.buildings.forEach(b => {
    html += `
      <div class="list-item">
        <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-building"/></svg></div>
        <div class="list-info">
          <h4>${b.name}</h4>
          <p>${b.address}</p>
          <p style="font-size:11px;color:var(--primary)">${b.floors[0]}</p>
        </div>
      </div>
    `;
  });
  html += '</div>';
  
  html += '<h4 style="margin-top:16px"><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-grad"/></svg>Faculties</h4>';
  html += '<div class="list">';
  nav.faculties.forEach(f => {
    html += `
      <div class="list-item">
        <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-grad"/></svg></div>
        <div class="list-info">
          <h4>${f.name}</h4>
          <p>${f.building}, ${f.floor}</p>
        </div>
      </div>
    `;
  });
  html += '</div>';
  
  html += '<h4 style="margin-top:16px"><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-location"/></svg>Rooms & Services</h4>';
  html += '<div class="list">';
  nav.pointsOfInterest.forEach(p => {
    html += `
      <div class="list-item">
        <div class="list-icon"><svg class="icon" style="width:20px;height:20px"><use href="#icon-${p.icon}"/></svg></div>
        <div class="list-info">
          <h4>${p.name}</h4>
          <p>${p.location}</p>
        </div>
      </div>
    `;
  });
  html += '</div>';
  
  html += '</div>';
  return html;
}

function renderCards() {
  return `
    <div class="page-content">
      <h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-wallet-giftcard"/></svg>My Cards</h3>
      <div class="dashboard-card accent" style="margin-bottom:16px">
        <div style="display:flex;align-items:center;gap:12px">
          <div><svg class="icon" style="width:32px;height:32px"><use href="#icon-grad"/></svg></div>
          <div>
            <div style="font-weight:600">Student Card</div>
            <div style="font-size:12px;color:var(--text-muted)">№ 1234567890</div>
          </div>
        </div>
        <div style="margin-top:12px;padding:8px;background:rgba(255,255,255,0.1);border-radius:8px;text-align:center">
          <div style="font-size:12px;color:var(--text-muted)">QR code for access</div>
          <div style="font-family:monospace;margin-top:4px">████████████</div>
        </div>
      </div>
      <div class="dashboard-card" style="margin-bottom:16px">
        <div style="display:flex;align-items:center;gap:12px">
          <div><svg class="icon" style="width:32px;height:32px"><use href="#icon-wallet-giftcard"/></svg></div>
          <div>
            <div style="font-weight:600">Transport Card</div>
            <div style="font-size:12px;color:var(--text-muted)">Balance: $125.00</div>
          </div>
        </div>
      </div>
      <div class="dashboard-card" style="margin-bottom:16px">
        <div style="display:flex;align-items:center;gap:12px">
          <div style="font-size:64px;text-align:center;color:var(--text-muted)">QR</div>
          <div>
            <div style="font-weight:600">Dormitory Pass</div>
            <div style="font-size:12px;color:var(--text-muted)">Dormitory 1, Room 205</div>
          </div>
        </div>
      </div>
    </div>
  `;
}

function renderClubs() {
  const clubs = [
    {
      id: 'sports',
      name: 'Sports Club',
      icon: 'soccer',
      description: 'Football, basketball, volleyball, swimming, athletics',
      schedule: [
        { day: 'Monday', time: '18:00-20:00', activity: 'Volleyball (gym)' },
        { day: 'Wednesday', time: '18:00-20:00', activity: 'Basketball (gym)' },
        { day: 'Friday', time: '17:00-19:00', activity: 'Swimming (pool)' },
        { day: 'Saturday', time: '10:00-13:00', activity: 'Tournament' }
      ],
      leader: 'John Smith',
      location: 'Sports Complex'
    },
    {
      id: 'songs',
      name: 'Song Club',
      icon: 'music',
      description: 'Poetry, guitar, songwriting, concerts',
      schedule: [
        { day: 'Tuesday', time: '19:00-21:00', activity: 'Rehearsal (Rm 305)' },
        { day: 'Thursday', time: '19:00-21:00', activity: 'Guitar workshop' },
        { day: '15th', time: '20:00-22:00', activity: 'Concert (Assembly Hall)' }
      ],
      leader: 'Anna Miller',
      location: 'Floor 3, Room 305'
    },
    {
      id: 'it',
      name: 'IT Club',
      icon: 'school',
      description: 'Hackathons, meetups, competitions, tech learning',
      schedule: [
        { day: 'Monday', time: '18:30-20:30', activity: 'Python meetup' },
        { day: 'Wednesday', time: '18:30-20:30', activity: 'Frontend dev' },
        { day: 'Saturday', time: '10:00-18:00', activity: 'Hackathon (monthly)' },
        { day: 'On request', time: '', activity: 'Employer meetings' }
      ],
      leader: 'David Brown',
      location: 'Lab 201'
    },
    {
      id: 'art',
      name: 'Art Workshop',
      icon: 'palette',
      description: 'Drawing, painting, design, photography, video',
      schedule: [
        { day: 'Tuesday', time: '17:00-19:00', activity: 'Drawing & painting' },
        { day: 'Thursday', time: '17:00-19:00', activity: 'Digital design (Figma)' },
        { day: 'Saturday', time: '12:00-15:00', activity: 'Photo walk / shoot' }
      ],
      leader: 'Sarah Johnson',
      location: 'Room 412'
    },
    {
      id: 'debate',
      name: 'Debate Club',
      icon: 'speech',
      description: 'Debates, discussions, round tables, public speaking',
      schedule: [
        { day: 'Wednesday', time: '18:00-20:00', activity: 'Debate practice' },
        { day: 'Friday', time: '18:00-20:00', activity: 'Debate tournament' },
        { day: '1st Thursday', time: '19:00-21:00', activity: 'Expert round table' }
      ],
      leader: 'Paul Wilson',
      location: 'Conference Room'
    },
    {
      id: 'science',
      name: 'Science Society',
      icon: 'science',
      description: 'Conferences, research, publications, grants',
      schedule: [
        { day: 'Monday', time: '16:00-18:00', activity: 'Project seminar' },
        { day: 'Friday', time: '16:00-18:00', activity: 'Publication prep' },
        { day: 'Monthly', time: '', activity: 'Science conference' }
      ],
      leader: 'Prof. Ivan Miller',
      location: 'Library'
    },
    {
      id: 'energy',
      name: 'Energy Club',
      icon: 'lightning',
      description: 'Engineering projects, robotics, competitions',
      schedule: [
        { day: 'Tuesday', time: '17:00-19:00', activity: 'Project work' },
        { day: 'Thursday', time: '17:00-19:00', activity: 'Robot assembly' },
        { day: 'Saturday', time: '10:00-14:00', activity: 'Model testing' }
      ],
      leader: 'Chris Novak',
      location: 'Robotics Lab'
    },
    {
      id: 'languages',
      name: 'Language Club',
      icon: 'globe',
      description: 'English, German, Chinese; conversation clubs',
      schedule: [
        { day: 'Monday', time: '18:00-19:30', activity: 'English conversation' },
        { day: 'Wednesday', time: '18:00-19:30', activity: 'German language' },
        { day: 'Friday', time: '18:00-19:30', activity: 'Chinese language' }
      ],
      leader: 'Maria Lee',
      location: 'Room 215'
    }
  ];

  let html = '<div class="page-content"><h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-target"/></svg>Clubs & Societies</h3>';
  
  clubs.forEach(club => {
    html += `
      <div class="dashboard-card" style="margin-bottom:16px">
        <div style="display:flex;align-items:flex-start;gap:12px;margin-bottom:12px">
          <div><svg class="icon" style="width:28px;height:28px"><use href="#icon-${club.icon}"/></svg></div>
          <div style="flex:1">
            <h4 style="margin:0 0 4px">${club.name}</h4>
            <p style="margin:0;font-size:12px;color:var(--text-muted)">${club.description}</p>
            <p style="margin:4px 0 0;font-size:11px;color:var(--primary)"><svg class="icon" style="width:12px;height:12px;margin-right:4px;vertical-align:middle"><use href="#icon-user"/></svg>${club.leader} • <svg class="icon" style="width:12px;height:12px;margin-right:4px;vertical-align:middle"><use href="#icon-location"/></svg>${club.location}</p>
          </div>
        </div>
        <div style="background:var(--bg-card);border-radius:8px;padding:8px">
          <div style="font-size:11px;color:var(--text-muted);margin-bottom:8px"><svg class="icon" style="width:12px;height:12px;margin-right:4px;vertical-align:middle"><use href="#icon-calendar"/></svg>Schedule:</div>
          ${club.schedule.map(s => `
            <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid rgba(255,255,255,0.05);font-size:12px">
              <span style="color:var(--primary)">${s.day}</span>
              <span style="color:var(--text-muted)">${s.time || ''}</span>
              <span style="flex:1;text-align:right;margin-left:8px">${s.activity}</span>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  });
  
  html += '</div>';
  return html;
}

// Главная страница выпускника
function renderAlumniHome() {
  const alum = appData.alumni;
  const profile = alum.profile;
  
  // Ближайшие события
  const upcomingEvents = alum.events.slice(0, 3);
  
  // Программы эндаумента
  const topPrograms = alum.endowment.programs.slice(0, 2);
  
  let html = `
    <div class="page-content">
      <!-- Приветствие выпускника -->
      <div class="dashboard-card accent" style="margin-bottom:20px">
        <div style="display:flex;align-items:center;gap:16px">
          <div><svg class="icon" style="width:48px;height:48px"><use href="#icon-grad"/></svg></div>
          <div>
            <h3 style="margin:0">Welcome, Alumni!</h3>
            <p style="margin:6px 0 0;font-size:14px;color:var(--text-muted)">Class of ${profile.graduationYear}</p>
            <p style="margin:4px 0 0;font-size:12px;color:var(--primary)">${profile.work.company} · ${profile.work.position}</p>
          </div>
        </div>
      </div>
      
      <!-- Модули быстрого доступа -->
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:20px">
        <div class="module-tile" onclick="showPage('alumni-profile')">
          <div><svg class="icon" style="width:24px;height:24px"><use href="#icon-user"/></svg></div>
          <span style="font-size:11px">Profile</span>
        </div>
        <div class="module-tile" onclick="showPage('alumni-events')">
          <div><svg class="icon" style="width:24px;height:24px"><use href="#icon-calendar"/></svg></div>
          <span style="font-size:11px">Events</span>
        </div>
        <div class="module-tile" onclick="showPage('alumni-endowment')">
          <div><svg class="icon" style="width:24px;height:24px"><use href="#icon-wallet-giftcard"/></svg></div>
          <span style="font-size:11px">Fund</span>
        </div>
        <div class="module-tile" onclick="showPage('alumni-fame')">
          <div><svg class="icon" style="width:24px;height:24px"><use href="#icon-trophy"/></svg></div>
          <span style="font-size:11px">Wall of Fame</span>
        </div>
        <div class="module-tile" onclick="showPage('alumni-network')">
          <div><svg class="icon" style="width:24px;height:24px"><use href="#icon-globe"/></svg></div>
          <span style="font-size:11px">Network</span>
        </div>
        <div class="module-tile" onclick="showPage('navigator')">
          <div><svg class="icon" style="width:24px;height:24px"><use href="#icon-map"/></svg></div>
          <span style="font-size:11px">Navigator</span>
        </div>
      </div>
      
      <!-- Ближайшие события -->
      <h4 style="font-size:16px;margin-bottom:12px"><svg class="icon" style="width:18px;height:18px;margin-right:8px;vertical-align:middle"><use href="#icon-calendar"/></svg>Upcoming Events</h4>
      ${upcomingEvents.map(e => `
        <div class="dashboard-card" style="margin-bottom:12px;cursor:pointer" onclick="toggleEventRSVP(${e.id}, 'home')">
          <div style="display:flex;justify-content:space-between;align-items:flex-start">
            <div style="flex:1">
              <div style="font-weight:600;font-size:14px">${e.title}</div>
              <div style="font-size:12px;color:var(--text-muted);margin-top:4px">${e.date} · ${e.time} · ${e.place}</div>
              <div style="font-size:11px;color:var(--text-muted);margin-top:2px">${e.description.substring(0, 60)}...</div>
            </div>
            <div style="text-align:right">
              <div style="font-size:11px;color:var(--text-muted)">${e.attendees}/${e.maxAttendees}</div>
              <div style="font-size:12px;font-weight:600;color:${e.registered ? 'var(--primary)' : 'var(--text-muted)'};margin-top:4px">
                ${e.registered ? 'Going' : '+ Going'}
              </div>
            </div>
          </div>
        </div>
      `).join('')}
      <div class="dashboard-card" style="text-align:center;padding:12px;margin-bottom:20px" onclick="showPage('alumni-events')">
        <span style="color:var(--primary);font-size:13px">All Events →</span>
      </div>
      
      <!-- Эндаумент-фонд -->
      <h4 style="font-size:16px;margin-bottom:12px"><svg class="icon" style="width:18px;height:18px;margin-right:8px;vertical-align:middle"><use href="#icon-wallet-giftcard"/></svg>Endowment Fund</h4>
      ${topPrograms.map(p => `
        <div class="dashboard-card" style="margin-bottom:12px" onclick="showPage('alumni-endowment')">
          <div style="font-weight:600;font-size:14px">${p.name}</div>
          <div style="margin-top:8px">
            <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px">
              <span style="color:var(--text-muted)">Raised</span>
              <span style="color:var(--primary)">${(p.raised/1000000).toFixed(1)}M / ${(p.target/1000000).toFixed(1)}M ${end.currency}</span>
            </div>
            <div style="height:6px;background:rgba(255,255,255,0.1);border-radius:3px;overflow:hidden">
              <div style="height:100%;width:${(p.raised/p.target*100).toFixed(0)}%;background:var(--primary);border-radius:3px"></div>
            </div>
          </div>
        </div>
      `).join('')}
      <div class="dashboard-card" style="text-align:center;padding:12px;margin-bottom:20px" onclick="showPage('alumni-endowment')">
        <span style="color:var(--primary);font-size:13px">Support the Fund →</span>
      </div>
      
      <!-- Выдающиеся выпускники -->
      <h4 style="font-size:16px;margin-bottom:12px"><svg class="icon" style="width:18px;height:18px;margin-right:8px;vertical-align:middle"><use href="#icon-trophy"/></svg>Outstanding Alumni</h4>
      <div class="dashboard-card" style="margin-bottom:20px" onclick="showPage('alumni-fame')">
        ${alum.wallOfFame.outstandingAlumni.slice(0, 2).map(a => `
          <div style="display:flex;align-items:center;gap:12px;padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.08)">
            <div><svg class="icon" style="width:24px;height:24px"><use href="#icon-user"/></svg></div>
            <div>
              <div style="font-weight:600;font-size:13px">${a.name}</div>
              <div style="font-size:11px;color:var(--text-muted)">${a.achievement}</div>
            </div>
          </div>
        `).join('')}
        <div style="text-align:center;padding:8px;font-size:12px;color:var(--primary)">Show All →</div>
      </div>
    </div>
  `;
  
  return html;
}

// Переключение RSVP на событие
function toggleEventRSVP(eventId, fromPage) {
  const event = appData.alumni.events.find(e => e.id === eventId);
  if (event) {
    event.registered = !event.registered;
    event.attendees += event.registered ? 1 : -1;
    
    // Перерисовать текущую страницу в зависимости от того, где находимся
    if (userMode === 'graduate') {
      if (fromPage === 'alumni-events') {
        document.getElementById('content').innerHTML = renderAlumniEvents();
      } else {
        document.getElementById('content').innerHTML = renderAlumniHome();
      }
    }
  }
}

// Профиль выпускника
function renderAlumniProfile() {
  const p = appData.alumni.profile;
  const registeredEvents = appData.alumni.events.filter(e => e.registered);
  
  return `
    <div class="page-content">
      <div class="profile-card" style="text-align:center">
        <div class="profile-avatar" style="width:80px;height:80px;font-size:32px">${p.photo}</div>
        <h3 style="margin-top:12px">${p.name}</h3>
        <p class="profile-group">Class of ${p.graduationYear}</p>
        <p style="font-size:14px;color:var(--text-muted)">${p.specialty}</p>
      </div>
      
      ${registeredEvents.length > 0 ? `
        <h4 style="margin:20px 0 12px;font-size:16px">Event Pass</h4>
        ${registeredEvents.slice(0,1).map(e => `
          <div class="dashboard-card accent" style="margin-bottom:16px">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
              <svg class="icon" style="width:32px;height:32px"><use href="#icon-qr"/></svg>
              <div>
                <div style="font-weight:600">${e.title}</div>
                <div style="font-size:12px;color:var(--text-muted)">${e.date} · ${e.time}</div>
                <div style="font-size:12px;color:var(--text-muted)">${e.place}</div>
              </div>
            </div>
            <img src="/images/qr-code-3.png" style="width:150px;height:150px;display:block;margin:0 auto;border-radius:8px" alt="QR код">
            <p style="text-align:center;font-size:12px;color:var(--text-muted);margin-top:8px">Show QR code at entrance</p>
          </div>
        `).join('')}
      ` : `
        <h4 style="margin:20px 0 12px;font-size:16px">Пропуск на мероприятие</h4>
        <div class="dashboard-card" style="text-align:center;padding:20px">
          <svg class="icon" style="width:40px;height:40px;margin-bottom:8px;opacity:0.5"><use href="#icon-qr"/></svg>
          <p style="font-size:14px;color:var(--text-muted)">Register for an event to get a pass</p>
        </div>
      `}
      
      <div class="profile-info">
        <div class="info-row">
          <span class="info-label">Current Position</span>
          <span class="info-value">${p.work.position}</span>
        </div>
        <div class="info-row">
          <span class="info-label">Company</span>
          <span class="info-value">${p.work.company}</span>
        </div>
        <div class="info-row">
          <span class="info-label">Email</span>
          <span class="info-value">${p.email}</span>
        </div>
      </div>
      
      <h4 style="margin:20px 0 12px;font-size:16px">Career</h4>
      ${p.careerHistory.map(job => `
        <div class="dashboard-card" style="margin-bottom:12px">
          <div style="font-weight:600;font-size:14px">${job.position}</div>
          <div style="font-size:13px;color:var(--text-muted)">${job.company}</div>
          <div style="font-size:12px;color:var(--primary);margin-top:4px">${job.years}</div>
        </div>
      `).join('')}
      
      <h4 style="margin:20px 0 12px;font-size:16px">About</h4>
      <div class="dashboard-card">
        <p style="font-size:14px;line-height:1.5">${p.about}</p>
      </div>
    </div>
  `;
}

// События выпускников
function renderAlumniEvents() {
  const events = appData.alumni.events;
  return `
    <div class="page-content">
      <h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-calendar"/></svg>Alumni Events</h3>
      ${events.map(e => `
        <div class="dashboard-card" style="margin-bottom:16px">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px">
            <div>
              <div style="font-weight:600;font-size:15px">${e.title}</div>
              <div style="font-size:13px;color:var(--text-muted);margin-top:4px">${e.date} · ${e.time}</div>
              <div style="font-size:12px;color:var(--text-muted)"><svg class="icon" style="width:12px;height:12px;margin-right:4px;vertical-align:middle"><use href="#icon-location"/></svg>${e.place}</div>
            </div>
            <div style="text-align:right">
              <div style="font-size:12px;color:var(--text-muted)">${e.attendees}/${e.maxAttendees}</div>
            </div>
          </div>
          <p style="font-size:13px;color:var(--text-muted);margin:8px 0">${e.description}</p>
          <button onclick="toggleEventRSVP(${e.id}, 'alumni-events')" style="width:100%;padding:10px;background:${e.registered ? 'var(--accent)' : 'var(--primary)'};border:none;border-radius:8px;color:#fff;font-weight:600;cursor:pointer">
            ${e.registered ? '✓ Going' : 'I\'m Going'}
          </button>
        </div>
      `).join('')}
    </div>
  `;
}

// Эндаумент-фонд
function renderAlumniEndowment() {
  const end = appData.alumni.endowment;
  return `
    <div class="page-content">
      <div class="dashboard-card accent" style="margin-bottom:20px">
        <h3 style="margin:0 0 8px">Endowment Fund</h3>
        <p style="font-size:14px;color:var(--text-muted)">Target capital to support the institute</p>
        <div style="margin-top:16px">
          <div style="font-size:24px;font-weight:700;color:var(--primary)">${(end.totalRaised/1000000).toFixed(1)}M ${end.currency}</div>
          <div style="font-size:12px;color:var(--text-muted)">raised in total</div>
        </div>
      </div>
      
      <h4 style="margin-bottom:12px">Fundraising Programs</h4>
      ${end.programs.map(p => `
        <div class="dashboard-card" style="margin-bottom:16px">
          <div style="font-weight:600;font-size:15px">${p.name}</div>
          <p style="font-size:13px;color:var(--text-muted);margin:8px 0">${p.description}</p>
          <div style="margin-top:12px">
            <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:6px">
              <span>Raised</span>
              <span style="color:var(--primary)">${(p.raised/1000000).toFixed(1)}M / ${(p.target/1000000).toFixed(1)}M ${end.currency}</span>
            </div>
            <div style="height:8px;background:rgba(255,255,255,0.1);border-radius:4px;overflow:hidden">
              <div style="height:100%;width:${(p.raised/p.target*100).toFixed(0)}%;background:var(--primary);border-radius:4px"></div>
            </div>
          </div>
          <button style="width:100%;margin-top:12px;padding:10px;background:var(--primary);border:none;border-radius:8px;color:#fff;font-weight:600;cursor:pointer">
            Donate
          </button>
        </div>
      `).join('')}
    </div>
  `;
}

// Доска почёта
function renderAlumniFame() {
  const wf = appData.alumni.wallOfFame;
  return `
    <div class="page-content">
      <h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-trophy"/></svg>Wall of Fame</h3>
      
      <h4 style="margin:20px 0 12px">Outstanding Alumni</h4>
      ${wf.outstandingAlumni.map(a => `
        <div class="dashboard-card" style="margin-bottom:12px">
          <div style="display:flex;align-items:center;gap:12px">
            <div><svg class="icon" style="width:36px;height:36px"><use href="#icon-user"/></svg></div>
            <div style="flex:1">
              <div style="font-weight:600;font-size:15px">${a.name}</div>
              <div style="font-size:13px;color:var(--primary)">Class of ${a.year}</div>
              <div style="font-size:13px;margin-top:4px">${a.achievement}</div>
              <div style="font-size:12px;color:var(--text-muted);margin-top:4px">${a.bio}</div>
            </div>
          </div>
        </div>
      `).join('')}
      
      <h4 style="margin:20px 0 12px">Award Winners</h4>
      ${wf.awardWinners.map(a => `
        <div class="dashboard-card" style="margin-bottom:12px;padding:12px">
          <div style="font-weight:600">${a.name}</div>
          <div style="font-size:13px;color:var(--primary)">${a.award}</div>
          <div style="font-size:12px;color:var(--text-muted)">${a.year}</div>
        </div>
      `).join('')}
    </div>
  `;
}

// Профессиональная сеть
function renderAlumniNetwork() {
  return `
    <div class="page-content">
      <h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-globe"/></svg>Alumni Network</h3>
      
      <div class="dashboard-card accent" style="margin-bottom:20px;padding:16px">
        <p style="font-size:14px">Find and connect with university alumni</p>
      </div>
      
      <h4 style="margin-bottom:12px">Search Alumni</h4>
      <div class="dashboard-card" style="margin-bottom:16px;padding:12px">
        <input type="text" placeholder="Search by name, graduation year..." style="width:100%;padding:10px;background:rgba(255,255,255,0.1);border:none;border-radius:8px;color:#fff;font-size:14px">
      </div>
      
      <h4 style="margin-bottom:12px">Online Alumni</h4>
      <div class="dashboard-card">
        <div style="display:flex;align-items:center;gap:8px;padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.08)">
          <div style="width:10px;height:10px;background:#4caf50;border-radius:50%"></div>
          <div style="font-size:14px">Jane D. (TechCorp) — 2018</div>
        </div>
        <div style="display:flex;align-items:center;gap:8px;padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.08)">
          <div style="width:10px;height:10px;background:#4caf50;border-radius:50%"></div>
          <div style="font-size:14px">Maria S. (DataSystems) — 2017</div>
        </div>
        <div style="display:flex;align-items:center;gap:8px;padding:8px 0">
          <div style="width:10px;height:10px;background:#4caf50;border-radius:50%"></div>
          <div style="font-size:14px">Ivan K. (Startup Inc.) — 2019</div>
        </div>
      </div>
    </div>
  `;
}

function renderNotes() {
  const notes = appData.notes;
  
  let html = '<div class="page-content">';
  html += '<h3><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-notes"/></svg>Subject Notes</h3>';
  
  notes.forEach(subject => {
    html += `
      <div class="dashboard-card" style="margin-bottom:16px">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
          <div style="font-size:28px">${subject.icon}</div>
          <div style="flex:1">
            <h4 style="margin:0">${subject.subject}</h4>
            <p style="margin:4px 0 0;font-size:12px;color:var(--text-muted)">${subject.topics.length} notes</p>
          </div>
        </div>
        <div style="background:var(--bg-card);border-radius:8px;padding:8px">
          ${subject.topics.map(topic => `
            <div style="padding:8px;border-bottom:1px solid rgba(255,255,255,0.05);cursor:pointer" onclick="alert('Note: ${topic.title}\\n\\n${topic.content}')">
              <div style="font-size:13px;font-weight:500;margin-bottom:4px">${topic.title}</div>
              <div style="font-size:11px;color:var(--text-muted)">${topic.content.substring(0, 60)}...</div>
              <div style="font-size:10px;color:var(--primary);margin-top:4px">Updated: ${topic.updated}</div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  });
  
  html += '</div>';
  return html;
}

function renderAbout() {
  const about = appData.aboutInstitute;
  let html = '<div class="page-content">';
  html += '<h3><svg class="icon" style="width:18px;height:18px"><use href="#icon-wallet-giftcard"/></svg> ' + about.title + '</h3>';
  
  // Main info
  html += '<div class="dashboard-card accent" style="margin-bottom:20px;border-radius:16px">';
  html += '<div style="display:flex;align-items:center;gap:16px;margin-bottom:16px">';
  html += '<div><svg class="icon" style="width:56px;height:56px"><use href="#icon-grad"/></svg></div>';
  html += '<div>';
  html += '<h4 style="margin:0;font-size:18px">Founded in ' + about.founded + '</h4>';
  html += '<p style="margin:6px 0 0;font-size:15px;color:var(--text-muted)">' + about.age + ' years of history</p>';
  html += '</div></div>';
  html += '<p style="font-size:14px;color:var(--text-muted);line-height:1.5">' + about.description + '</p>';
  html += '<p style="font-size:13px;color:var(--primary);margin-top:12px"><svg class="icon" style="width:14px;height:14px;margin-right:4px;vertical-align:middle"><use href="#icon-location"/></svg>' + about.address + '</p>';
  html += '</div>';
  
  // Stats
  html += '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:20px">';
  html += '<div class="dashboard-card" style="text-align:center;padding:16px"><div style="font-size:28px;font-weight:700;color:var(--primary)">' + about.stats.students + '</div><div style="font-size:12px;color:var(--text-muted);margin-top:4px">students</div></div>';
  html += '<div class="dashboard-card" style="text-align:center;padding:16px"><div style="font-size:28px;font-weight:700;color:var(--primary)">' + about.stats.faculties + '</div><div style="font-size:12px;color:var(--text-muted);margin-top:4px">faculties</div></div>';
  html += '<div class="dashboard-card" style="text-align:center;padding:16px"><div style="font-size:28px;font-weight:700;color:var(--primary)">' + about.stats.departments + '</div><div style="font-size:12px;color:var(--text-muted);margin-top:4px">departments</div></div>';
  html += '</div>';
  
  // History
  html += '<div class="dashboard-card" style="margin-bottom:20px;padding:16px">';
  html += '<h4 style="margin-bottom:12px;font-size:16px"><svg class="icon" style="width:18px;height:18px;margin-right:8px;vertical-align:middle"><use href="#icon-book"/></svg>History</h4>';
  html += '<p style="font-size:13px;color:var(--text-muted);line-height:1.6">' + about.history + '</p>';
  html += '</div>';
  
  // Famous graduates
  html += '<div class="dashboard-card" style="margin-bottom:20px;padding:16px">';
  html += '<h4 style="margin-bottom:16px;font-size:16px"><svg class="icon" style="width:18px;height:18px;margin-right:8px;vertical-align:middle"><use href="#icon-star"/></svg>Famous Graduates</h4>';
  about.famousGraduates.forEach((g, i) => {
    html += '<div style="padding:12px 0' + (i < about.famousGraduates.length - 1 ? ';border-bottom:1px solid rgba(255,255,255,0.08)' : '') + '">';
    html += '<div style="font-size:15px;font-weight:600">' + g.name + '</div>';
    html += '<div style="font-size:12px;color:var(--text-muted);margin-top:2px">' + g.role + '</div>';
    html += '</div>';
  });
  html += '</div>';
  
  // Почётные доктора и профессора ТИ
  html += '<div class="dashboard-card" style="margin-bottom:20px;padding:16px">';
  html += '<h4 style="margin-bottom:16px;font-size:16px"><svg class="icon" style="width:18px;height:18px;margin-right:8px;vertical-align:middle"><use href="#icon-medal"/></svg>Почётные доктора и профессора ТИ</h4>';
  html += '<p style="font-size:12px;color:var(--text-muted);margin-bottom:16px">С 1967 года Учёный Совет присваивает звания иностранным учёным за вклад в развитие научных отношений между вузами</p>';
  about.honoraryProfessors.slice(0, 10).forEach((p, i) => {
    html += '<div style="padding:10px 0' + (i < 9 ? ';border-bottom:1px solid rgba(255,255,255,0.08)' : '') + '">';
    html += '<div style="display:flex;justify-content:space-between;align-items:center">';
    html += '<div style="font-size:14px;font-weight:600">' + p.name + '</div>';
    html += '<div style="font-size:11px;color:var(--accent);background:rgba(0,0,0,0.2);padding:2px 8px;border-radius:10px">' + p.year + '</div>';
    html += '</div>';
    html += '<div style="font-size:11px;color:var(--text-muted);margin-top:2px">' + p.country + ' · ' + p.role + '</div>';
    html += '</div>';
  });
  if (about.honoraryProfessors.length > 10) {
    html += '<div style="text-align:center;padding:12px;font-size:12px;color:var(--text-muted)">... ещё ' + (about.honoraryProfessors.length - 10) + ' почётных докторов</div>';
  }
  html += '</div>';
  
  // Факультеты
  html += '<div class="dashboard-card" style="padding:16px">';
  html += '<h4 style="margin-bottom:16px;font-size:16px"><svg class="icon" style="width:20px;height:20px;margin-right:8px;vertical-align:middle"><use href="#icon-grad"/></svg>Факультеты</h4>';
  about.faculties.forEach((f, i) => {
    html += '<div style="padding:12px 0' + (i < about.faculties.length - 1 ? ';border-bottom:1px solid rgba(255,255,255,0.08)' : '') + '">';
    html += '<div style="font-size:14px;font-weight:600">' + f.name + '</div>';
    html += '<div style="font-size:12px;color:var(--text-muted);margin-top:2px">' + f.desc + '</div>';
    html += '</div>';
  });
  html += '</div>';
  
  html += '</div>';
  return html;
}

// Status bar
function updateStatus() {
  const battery = Math.floor(Math.random() * 10) + 90;
  document.querySelector('.status-bar').textContent = battery + '%';
}

// Подписки - переключение категорий событий
function toggleCategory(categoryId) {
  const subs = appData.profile.subscriptions;
  const idx = subs.eventCategories.indexOf(categoryId);
  if (idx > -1) {
    subs.eventCategories.splice(idx, 1);
  } else {
    subs.eventCategories.push(categoryId);
  }
  // Перерисовать профиль
  document.getElementById('content').innerHTML = renderProfile();
}

// Подписки - переключение клуба
function toggleClub(clubId) {
  const subs = appData.profile.subscriptions;
  const idx = subs.clubs.indexOf(clubId);
  if (idx > -1) {
    subs.clubs.splice(idx, 1);
  } else {
    subs.clubs.push(clubId);
  }
  // Перерисовать профиль
  document.getElementById('content').innerHTML = renderProfile();
}

// Init
document.addEventListener('DOMContentLoaded', () => {
  loadTheme();
  initUserMode();
  setInterval(updateStatus, 60000);
  updateStatus();
  
  // Check if app was open and restore state
  const wasAppOpen = localStorage.getItem('univerid_appOpen');
  
  if (wasAppOpen === 'true') {
    // App was open before refresh - restore it
    document.getElementById('landing').classList.add('hidden');
    document.getElementById('app').classList.remove('hidden');
    
    // Restore last page from localStorage
    const lastPage = localStorage.getItem('univerid_lastPage');
    const savedHistory = localStorage.getItem('univerid_history');
    
    if (lastPage && savedHistory) {
      try {
        history = JSON.parse(savedHistory);
        if (history.length > 0) {
          updateHeader(lastPage);
          renderContent(lastPage);
          document.getElementById('backBtn').classList.toggle('hidden', history.length <= 1);
        }
      } catch (e) {
        // If error, show home
        showPage('home');
      }
    } else {
      showPage('home');
    }
  }
});