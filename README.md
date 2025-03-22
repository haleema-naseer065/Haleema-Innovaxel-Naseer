# URL Shortener Service (Django + MySQL)

## 📌 Overview
This is a **Django-based URL Shortener API** that allows users to:
- Create short URLs from long URLs.
- Retrieve the original URL using the short link.
- Update an existing short URL.
- Delete a short URL.
- Get statistics on URL access count.

## 🏗 Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **Tools:** Python, Postman for API testing

## 🚀 Features
- Generate a **unique short code** for each long URL.
- **Redirect users** to the original URL using the short link.
- **Track access count** (how many times a short URL is accessed).
- CRUD operations on URLs (Create, Retrieve, Update, Delete).
- RESTful API design with JSON responses.

## ⚙️ Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
    git clone https://github.com/haleema-naseer065/Haleema-Innovaxel-Naseer.git
    cd Haleema-Innovaxel-Naseer
```

### 2️⃣ **Set Up Virtual Environment**
```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```bash
    pip install -r requirements.txt
```

### 4️⃣ **Configure MySQL Database**
Make sure MySQL is installed and running. Then, create a database:
```sql
    CREATE DATABASE url;
```
Edit `settings.py` and configure database connection:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'url',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ **Run Migrations**
```bash
    python manage.py makemigrations
    python manage.py migrate
```

### 6️⃣ **Run the Development Server**
```bash
    python manage.py runserver
```
Server will start at: `http://127.0.0.1:8000/`

## 📡 API Endpoints
| Method | Endpoint             | Description                        |
|--------|----------------------|------------------------------------|
| POST   | `/shorten/`          | Create a short URL                 |
| GET    | `/shorten/<code>/`   | Retrieve the original URL          |
| PUT    | `/shorten/<code>/`   | Update a short URL                 |
| DELETE | `/shorten/<code>/`   | Delete a short URL                 |
| GET    | `/statistics/<code>/`| Get access count statistics        |

### 📍 Example Request: Create Short URL
**Request:**
```json
POST /shorten/
{
    "url": "https://www.example.com/long-url"
}
```

**Response:**
```json
{
    "id": "1",
    "url": "https://www.example.com/long-url",
    "shortCode": "abc123",
    "createdAt": "2024-03-20T12:00:00Z",
    "updatedAt": "2024-03-20T12:00:00Z"
}
```

### 📍 Example Request: Retrieve Original URL
**Request:**
```bash
GET /shorten/abc123/
```
**Response:** *(Redirects to original URL)*

---

🚀 Happy Coding & Keep Innovating! 🎉

