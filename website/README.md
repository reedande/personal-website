# Personal Website (Flask)

This repository now hosts a small Flask app for the personal website.

Structure
---------

```
website/
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── templates/           # Jinja2 templates
├── static/
│   ├── css/
│   └── images/
└── README.md
```

Run locally (PowerShell)
-------------------------

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py

Open http://127.0.0.1:5000 in your browser.

Notes
-----
- Copy any existing images from the old `images/` directory into `static/images/`.
- Replace `app.secret_key` in `app.py` with a secure random value before deploying.
- This app uses server-side validation for the contact form and client-side JS validation in the template.

Docker
------

Build the Docker image (PowerShell):

```powershell
docker build -t personal-website:latest .
```

Run with Docker:

```powershell
docker run --rm -p 5000:5000 --name personal-website personal-website:latest
```

Or with docker-compose:

```powershell
docker-compose up --build
```

Notes for production:
- Use a secure random `SECRET_KEY` instead of the placeholder in `app.py`. You can pass it as an environment variable and load it in your Flask app.
- If you want the SQLite DB to persist, mount a volume for `projects.db` or manage the DB outside the container.

Importing a pre-populated database
---------------------------------

If you'd rather create the SQLite DB from the provided SQL file (no Python needed), run:

```powershell
cd 'C:\Users\reedw\OneDrive\Desktop\AiDD\Assignment5\website'
sqlite3 projects.db < projects.sql
```

After that `projects.db` will exist and contain the sample projects. Ensure the image files referenced in `projects.sql` are placed into `static/images/`.
