# 🌐 Minimalist Python Django Developer Portfolio

[![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-5.0.x-green.svg)](https://www.djangoproject.com/)
[![Platform](https://img.shields.io/badge/deployment-Render-orange.svg)](https://render.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance, production-ready developer portfolio built using the **Python-Django** framework. This project follows an elegant editorial minimalist design pattern, featuring optimized asset delivery and modular backend architecture.

🔗 **Live Deployment Link:** [ https://my-django-portfolio-15y9.onrender.com/ ].
---

## 🛠️ Tech Stack & Production Architecture

The system is architected using industry-standard backend and infrastructure practices:

* **Core Framework:** `Python` & `Django 5.0` (MVC Architecture)
* **Frontend Engine:** Responsive HTML5 styled with utility-first `Tailwind CSS`
* **Production Server:** `Gunicorn` (Green Unicorn) WSGI HTTP Server
* **Static Assets Handling:** `WhiteNoise Middleware` for direct, high-speed static asset injection
* **Hosting Infrastructure:** Fully automated CI/CD pipeline integrated via `Render`

---

## 🌟 Featured Flagship Project

### 🤖 AI Resume Analyzer
An automated talent acquisition tool that parses, processes, and evaluates candidate resumes using backend NLP workflows.

* **Text Extraction:** Extracts raw semantic data from unstructured PDF/Word formats.
* **Scoring Engine:** Computes skill compliance coefficients directly against specialized job descriptions.
* **Gap Analysis:** Instantly highlights missing technical capabilities and soft skill requirements.
* **Smart Analytics:** Generates comprehensive career roadmaps and automated job recommendations based on compliance metrics.

---

## ⚙️ Local Installation & Environment Setup

To clone and execute this repository locally, initialize the following environment workflows:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Kuldeepkumar1289/my_django_portfolio.git](https://github.com/Kuldeepkumar1289/my_django_portfolio.git)
    cd my_django_portfolio
    ```

2.  **Initialize & Activate Virtual Environment:**
    ```bash
    python -m venv venv
    # On Windows (CMD/PowerShell):
    venv\Scripts\activate
    ```

3.  **Install Application Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute Migrations & Static Engine:**
    ```bash
    python manage.py migrate
    python manage.py collectstatic --noinput
    ```

5.  **Launch Local Development Server:**
    ```bash
    python manage.py runserver
    ```
    Open your browser and navigate to: `http://127.0.0.1:8000/`

---

## 📬 Contact & Professional Networks

* **LinkedIn Profile:** [Kuldeep Kumar ↗](https://linkedin.com/in/kuldeep-kumar-5529372b0/)
* **GitHub Repository:** [@Kuldeepkumar1289 ↗](https://github.com/Kuldeepkumar1289)
* **Direct Email:** [kuldeepkumar76106@gmail.com](mailto:kuldeepkumar76106@gmail.com)
