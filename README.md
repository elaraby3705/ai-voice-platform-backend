# AI Voice Platform Backend

## Project Overview
This repository contains the backend for an **AI Voice platform**. The backend handles:

- Real-time voice sessions with LiveKit
- User authentication and management
- Project and session CRUD operations
- Scalable cloud deployment (GCP / AWS)
- Performance optimizations and caching

**Tech Stack:**
- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Caching & Async:** Redis, Cloud Pub/Sub
- **Cloud / Deployment:** GCP (Cloud Run, Cloud SQL, Memorystore), AWS (S3, Lambda)
- **Realtime / Voice:** LiveKit
- **Testing:** Django TestCase, DRF APITestCase

---

## Milestones & Roadmap

| Milestone | Due Date | Goal |
|-----------|----------|------|
| **M1: Core Setup & Authentication** | 2025-11-18 | Setup Django project, PostgreSQL, User/Auth endpoints, initial unit tests |
| **M2: Project & CRUD API** | 2025-11-24 | Implement Project & VoiceSession models and REST APIs |
| **M3: LiveKit & Session API** | 2025-11-29 | Integrate LiveKit, generate access tokens, create session endpoints |
| **M4: GCP Infrastructure Prototype** | 2025-12-04 | Deploy to Cloud Run, connect Cloud SQL & Redis, setup CI/CD |
| **M5: Performance & Async** | 2025-12-10 | Optimize APIs, caching, async tasks, unit tests, documentation cleanup |

---

## Issues Structure

**Issue types used in this project:**
- **FEAT** – New feature / endpoint / integration
- **TASK** – Task, setup, test, or administrative work
- **CHORE** – Routine maintenance, cleanup, or documentation
- **BUG** – Fix a functional bug

Each milestone has associated issues, e.g.:

### M1: Core Setup & Authentication
- `[CHORE]` Initialize Django project & settings
- `[CHORE]` Configure local PostgreSQL database
- `[FEAT]` Implement User Model & Auth endpoints (Register, Login, Token Refresh)
- `[TASK]` Write unit tests for all Auth views
- `[CHORE]` Initial Cloud Run deployment template

*(Subsequent milestones follow a similar structure.)*

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/voice_ai_api.git
cd voice_ai_api
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment variables (.env example)**
```
DATABASE_URL=postgres://user:password@localhost:5432/voice_ai
SECRET_KEY=<your-secret-key>
DEBUG=True
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Run server**
```bash
python manage.py runserver
```

---

## Contribution Guidelines
- Use meaningful branches:
  - feature/, task/, chore/
- Follow Conventional Commits:
  - feat:, fix:, chore:, task:
- Link PRs to issues & milestones

---

## Testing
```bash
python manage.py test
```
Minimum **90% coverage** required.

---

## License
Hammad .
