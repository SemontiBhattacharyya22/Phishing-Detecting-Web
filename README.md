# 🔐 PhishGuard – Phishing Email Detection System

A full-stack web application to detect phishing emails using rule-based analysis.  
Built with React (frontend) and Django REST Framework (backend), featuring JWT authentication and user-specific scan history.

---

## 🚀 Features

- 🔐 JWT Authentication (Login system)
- 📩 Email phishing detection (rule-based)
- 🌐 URL analysis for suspicious patterns
- 📊 Dashboard with scan statistics
- 📜 Scan history (user-specific)
- 🔒 Protected API endpoints
- ⚛️ React frontend with Bootstrap UI

---

## 🧠 Detection Logic

The system analyzes emails based on:

- Suspicious keywords (e.g., "urgent", "verify", "bank")
- Presence of links
- URL patterns:
  - IP-based URLs
  - Long URLs
  - Special characters (@, -)

---

## 🏗️ Tech Stack

### Frontend:
- React (Vite)
- Bootstrap
- Axios

### Backend:
- Django
- Django REST Framework
- JWT Authentication

### Database:
- SQLite (default Django DB)

