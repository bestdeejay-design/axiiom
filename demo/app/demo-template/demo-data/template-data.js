// Minimal generic demo data — copy into js/app.js to populate the SPA
const templateData = {
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
      { name: 'Faculty of Computer Science', desc: 'Software engineering, AI, data science' },
      { name: 'Faculty of Engineering', desc: 'Mechanical, electrical, civil engineering' },
      { name: 'Faculty of Sciences', desc: 'Physics, chemistry, biology, mathematics' },
      { name: 'Faculty of Humanities', desc: 'Literature, philosophy, languages' },
      { name: 'Faculty of Business', desc: 'Economics, management, finance' },
      { name: 'Faculty of Arts', desc: 'Design, music, fine arts' }
    ]
  },

  navigator: {
    buildings: [
      { id: '1', name: 'Main Building', address: '123 University Ave', floors: ['Floor 2: Rooms 201-214', 'Floor 3: Rooms 301-314', 'Floor 4: Rooms 401-414'] },
      { id: '2', name: 'Building 2', address: '125 University Ave', floors: ['Floor 2: Continuing Education Center', 'Floor 1: Student Services'] },
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
        { name: 'John Smith', year: 2010, achievement: 'Founder of TechCorp', bio: 'Founded TechCorp, a leading tech company. Graduate of 2010, Faculty of Computer Science' },
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
