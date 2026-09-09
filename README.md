# Student Authentication and Attendance Management System

A robust microservices-based application designed to manage student authentication, enrollment, and attendance tracking for educational institutions. The platform provides distinct interfaces and capabilities for Admins, Lecturers, and Students.

## Architecture Overview

This project follows a microservices architecture to ensure high scalability, separation of concerns, and ease of deployment.

### Services

- **`auth_service`**: Centralized authentication and authorization using JWT. Handles user registration, login, and role management.
- **`student_service`**: Manages student records, demographics, courses enrolled, and profiles.
- **`attendance_service`**: The core engine for creating class sessions and marking student attendance (Present, Absent, Late). Generates analytics and history.
- **`frontend`**: A modern, highly responsive React (Vite) Single Page Application (SPA). Styled with a premium SaaS aesthetic using Tailwind CSS and Shadcn-like components.

## Features by Role

### 🛡️ Admin
- Full system access.
- Manage users (Students & Lecturers).
- Create and manage courses.
- System-wide attendance reporting and analytics.

### 👨‍🏫 Lecturer
- View assigned courses.
- Create attendance sessions (Date, Time, Module).
- Rapidly mark attendance using quick-toggle buttons.
- View individual course statistics.

### 🎓 Student
- View enrolled courses.
- Track personal attendance history.
- View overall attendance percentages.

## Getting Started

### Prerequisites
- Docker and Docker Compose (for running backend services)
- Node.js 18+ (for running the frontend locally)

### Running the Backend

The backend microservices' Docker images are built automatically via **GitHub Actions** CI/CD pipelines. You do not need to build the images locally.

To spin up the pre-built backend services locally using the remote images, simply run:

```bash
docker-compose up -d
```
This will start the `auth_service`, `student_service`, and `attendance_service` along with any required databases.

### Running the Frontend

To run the modern dashboard UI locally:

```bash
cd frontend
npm install
npm run dev
```

Navigate to `http://localhost:5173` in your browser.

## Tech Stack

- **Frontend**: React, Vite, TypeScript, Tailwind CSS, Lucide React, Recharts, React Router
- **Backend Architecture**: Microservices
- **CI/CD & Builds**: GitHub Actions
- **Containerization**: Docker

## License

This project is proprietary and confidential.
