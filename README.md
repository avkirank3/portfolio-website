# portfolio-website

A polished personal portfolio for a Python Django and AI developer, built with React frontend and Django backend.

## Stack
- React + Vite + JavaScript
- Django + Django REST Framework
- Responsive and animated UI
- Light, deploy-friendly structure

## Features
- Elegant hero section with premium light green and dark golden yellow palette
- About, expertise, experience, projects, and contact sections
- Animated glassmorphism cards and subtle motion effects
- Contact actions and downloadable resume link
- Django API to serve portfolio data

## Quick start

### 1) Backend
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### 2) Frontend
```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

Then open the frontend URL shown in terminal and the API will be available at:
- http://localhost:8000/api/profile

## Production build

```bash
cd frontend
npm run build
```

The production static bundle can be served from Django or deployed separately.
