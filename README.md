# Smart Pantry

## Project Overview
Smart Pantry is a web-based application designed to help users manage their pantry items efficiently. Users can track stock levels, receive notifications for expiring items, and scan barcodes for easy item management.

---

## Technology Stack

**Backend**
- Python 3.11
- FastAPI
- PostgreSQL
- Pydantic & pydantic-settings
- Docker

**Frontend**
- React 18
- Axios
- HTML5 QR Code Scanner
- React Router
- Docker

**Development Tools**
- Git for version control
- Conda environment for Python dependencies
- Node.js & npm for frontend
- Docker & Docker Compose for containerization

---

## Software Map

### Backend
- `main.py`: FastAPI application entry point.
- `config.py`: Environment settings using `pydantic-settings`.
- `database.py`: SQLAlchemy engine & Base.
- `models.py`: Database models (e.g., PantryItem, User).
- `schemas.py`: Pydantic schemas for request/response validation.
- `routers/pantry.py`: API endpoints for pantry CRUD operations.
- `.env`: Environment variables (e.g., database URL, secret key).
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Backend container setup.

### Frontend
- `index.js`: Entry point for React app.
- `App.js`: Main component and routing setup.
- `components/`: React components (e.g., Pantry, ItemList).
- `services/api.js`: Axios API calls to backend.
- `package.json`: Node.js dependencies.
- `Dockerfile`: Frontend container setup.

### Root
- `docker-compose.yml`: Orchestrates backend, frontend, and database containers.
- `.gitignore`: Ignored files for git.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/gvarul/smart-pantry.git
cd smart-pantry
```
### 2. Backend Setup

```bash
cd backend
conda create -n smart-pantry-backend python=3.11 -y
conda activate smart-pantry-backend
pip install -r requirements.txt
```
### 3. Frontend Setup
```bash
cd ../frontend
npm install --legacy-peer-deps

```

### 4. Run with Docker Compose
```bash
docker compose up --build

```
- Backend: http://localhost:8000

- Frontend: http://localhost:3000

##  Development Workflow

- Feature Branches: Use ```git checkout -b feature/<feature-name>``` for new features.

- Testing: Add unit tests in backend and frontend folders. Run tests before pull requests.

- Code Reviews: Push feature branch and create pull requests for review.

- Merging: Only merge after passing tests and reviews.

## Contribution Guidelines

- Follow PEP8 for Python code.

- Use consistent naming for React components.

- Document APIs in routers/ using docstrings.

- Update README or software map for new features.
