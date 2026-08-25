# 📚 Student Assessment Portal

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Latest-green?logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**A modern, intuitive platform for creating, managing, and evaluating student assessments**

[Features](#-features) • [Quick Start](#-quick-start) • [Usage](#-usage) • [Architecture](#-architecture) • [Security](#-security-notes)

</div>

---

## 📖 Overview

Student Assessment Portal is a comprehensive web-based solution designed to streamline the assessment process in educational institutions. It empowers administrators to create and manage assessments while providing students with an intuitive interface to take tests and receive instant feedback.

Whether you're running a small training program or managing classroom assessments, this platform offers the flexibility and ease of use you need.

---

## ✨ Features

### 👨‍💼 Administrator Dashboard
- ✅ Create new assessments with custom subjects
- ✅ Add multiple-choice questions with four options
- ✅ Track and analyze all student results
- ✅ View comprehensive performance metrics
- ✅ Manage user accounts and roles

### 👨‍🎓 Student Interface
- ✅ Browse available assessments
- ✅ Take timed assessments with ease
- ✅ Instant score calculation (Pass/Fail)
- ✅ View detailed performance feedback
- ✅ Access assessment history

### 🔒 Core Features
- ✅ **Secure Authentication**: Role-based login system (Admin/Student)
- ✅ **Session Management**: Automatic logout for security
- ✅ **Auto-Registration**: New users register on first login
- ✅ **Lightweight Storage**: JSON-based data persistence

---

## 🛠 Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML5, CSS3, Bootstrap |
| **Database** | JSON Files |
| **Server** | Python Built-in Development Server |

---

## 📁 Project Structure

```
Student Assessment Portal/
├── app.py                      # Main application entry point
├── Database/                   # Data persistence layer
│   ├── students.json          # User credentials & roles
│   ├── assessments.json       # Assessment definitions
│   ├── questions.json         # Question bank
│   └── results.json           # Student results
├── static/                     # Static assets (CSS, JS, images)
├── templates/                  # HTML templates
│   ├── login.html             # Authentication
│   ├── admin_dashboard.html   # Admin panel
│   ├── student_dashboard.html # Student panel
│   ├── create_assessment.html # Assessment builder
│   ├── add_questions.html     # Question editor
│   ├── assessment.html        # Test interface
│   ├── result.html            # Results display
│   └── view_assessment.html   # Assessment viewer
└── README.md                  # Documentation
```

---

## 🚀 Quick Start

### Prerequisites
```
✓ Python 3.6 or higher
✓ pip (Python package manager)
```

### Installation & Setup

```bash
# Navigate to project directory
cd "Student Assessment Portal"

# Install dependencies
pip install flask

# Run the application
python app.py

# Access in browser
http://localhost:5000
```

---

## 👥 Default Credentials

| Role | Username | Password |
|------|----------|----------|
| **Admin** | `admin` | `admin123` |
| **Student** | `student` | `student123` |

> ⚠️ Change these credentials immediately in production!

---

## 📊 How It Works

### Admin Workflow
```
Login → Create Assessment → Add Questions → Review Results → Analyze Performance
```

### Student Workflow
```
Login → View Assessments → Take Test → Submit Answers → View Score & Feedback
```

---

## 💡 Usage Guide

### For Administrators

1. **Login** with admin credentials
2. **Create Assessment**
   - Navigate to Create Assessment
   - Enter assessment name and subject
   - Save to create
3. **Add Questions**
   - Select target assessment
   - Enter question text and four options
   - Mark the correct answer
   - Repeat for all questions
4. **Monitor Results**
   - View all student submissions
   - Analyze performance trends
   - Download or export results

### For Students

1. **Login** with student credentials
2. **Browse Assessments**
   - View all available tests on dashboard
3. **Take Assessment**
   - Select an assessment
   - Answer all questions (one answer per question)
   - Review before submitting
4. **Submit & Review**
   - Submit your responses
   - Instantly see your score and performance

---

## 🔐 Security Notes

⚠️ **Important**: This is an educational project. Before using in production:

| Issue | Solution |
|-------|----------|
| **Default Secret Key** | Change `app.secret_key` in app.py to a random string |
| **Plain Text Passwords** | Implement password hashing using `bcrypt` or `werkzeug.security` |
| **Input Validation** | Add input sanitization and validation |
| **HTTPS** | Deploy with SSL/TLS certificates |
| **Auto-Registration** | Disable automatic user registration |
| **Database** | Migrate to production database (PostgreSQL, MySQL, etc.) |

---

## 🎯 Key Advantages

- 🎓 **Easy to Use**: Intuitive interface for both students and teachers
- ⚡ **Fast Setup**: Get started in minutes with minimal configuration
- 📊 **Real-time Feedback**: Students get instant assessment results
- 🔍 **Detailed Analytics**: Comprehensive reporting for administrators
- 🛡️ **Secure**: Built-in authentication and role-based access control
- 📱 **Responsive**: Works across desktop and mobile devices

---

## 🔮 Future Enhancements

- [ ] Password hashing & encryption
- [ ] Email notifications
- [ ] Assessment scheduling & time limits
- [ ] Question bank & randomization
- [ ] Advanced analytics & reporting
- [ ] User profile management
- [ ] Database migration (SQL)
- [ ] REST API endpoints
- [ ] Mobile app integration
- [ ] Negative marking & custom scoring

---

## 📝 License

This project is for **educational purposes only**.

---

<div align="center">

### Made with ❤️ for Education

**Last Updated**: 2026-07-31

</div>
