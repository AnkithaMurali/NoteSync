A sleek and secure note-taking web app built with Django. Log in, take notes, pin important ones, search instantly — all in a distraction-free interface.


## 🚀 Features

- Create, Edit, and Delete Notes
- Pin/Unpin Notes (Pinned notes always stay on top)
- Instant Search functionality
- Authentication (Signup, Login, Logout)
- Clean, Responsive UI with Bootstrap
- User-specific Notes — Your data stays private
- Notes ordered by creation time


## 🛠️ Tech Stack

- **Backend**: Django 5.x
- **Frontend**: HTML, Bootstrap 5
- **Database**: SQLite (default)  
- **Auth**: Django's built-in auth system

### 📁 Project Structure
```
notesync/
├── backend/
│ ├── notesync/ # Main project settings
│ ├── notes/ # Notes app (models, views, urls)
│ ├── templates/ # HTML templates (home, auth, notes)
│ ├── static/ # CSS/JS (optional)
│ └── manage.py
├── venv/ # Python virtual environment
├── requirements.txt
└── README.md
```




## 🛠️ Setup Instructions


```bash
1. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

2. Install Dependencies
pip install -r requirements.txt

3. Apply Migrations
python manage.py makemigrations
python manage.py migrate

4. Create a Superuser
python manage.py createsuperuser

5. Run the Development Server
python manage.py runserver

6. Open in Browser
Visit: http://127.0.0.1:8000/
```


