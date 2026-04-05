# 📝 Full-Stack Todo Application

A modern, high-performance Task Management system featuring a **Python (FastAPI)** backend and a **React (TypeScript)** frontend. This project demonstrates a complete CRUD (Create, Read, Update, Delete) workflow with a persistent SQLite database.

## 🚀 Key Features
- **Full CRUD Operations**: Create tasks, view the list, toggle completion status, and delete items.
- **Persistent Database**: Powered by SQLAlchemy ORM and SQLite.
- **Modern UI**: A clean, responsive interface with smooth transitions and status indicators.
- **Type Safety**: End-to-end type consistency using TypeScript and Pydantic.
- **RESTful API**: Clean, documented endpoints following industry standards.

---

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern, fast (high-performance) web framework for Python.
- **SQLAlchemy**: Powerful SQL Toolkit and Object-Relational Mapper (ORM).
- **SQLite**: Lightweight, serverless relational database.
- **Pydantic**: Data validation and settings management.

### Frontend
- **React 18**: Component-based UI library.
- **TypeScript**: Typed superset of JavaScript for reliable code.
- **Vite**: Ultra-fast frontend build tool and dev server.
- **CSS3**: Custom variables and Flexbox layout for styling.

---

## ⚙️ Installation and Setup

Follow these instructions to get the application running on your local machine.

### 1. Backend Setup (FastAPI)
Make sure you have **Python 3.10+** installed.

```bash
# Navigate to the project root or backend folder
cd pythonFastApi

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install fastapi uvicorn sqlalchemy

# Start the server
uvicorn main:app --reload
```


### 2. Frontend Setup (React)
```
# Open a new terminal and navigate to the frontend folder
cd todoappwithfastapi

# Install dependencies
npm install

# Run the development server
npm run dev
```