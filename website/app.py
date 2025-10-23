from flask import Flask, render_template, request, redirect, url_for, flash
import DAL

app = Flask(__name__)
app.secret_key = 'replace-this-with-a-secure-key'

# Initialize the database at import time. This ensures the DB and tables exist
# when running under a WSGI server (gunicorn) which may not call Flask's
# request lifecycle decorators the same way as the development server.
DAL.init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/projects')
def projects():
    projects = DAL.get_projects()
    return render_template('projects.html', projects=projects)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # This form now submits new projects to the projects DB table
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        imageFileName = request.form.get('imageFileName', '').strip() or None

        errors = []
        if not title:
            errors.append('Title is required')
        if not description:
            errors.append('Description is required')

        if errors:
            for e in errors:
                flash(e, 'error')
            return redirect(url_for('contact'))

        DAL.add_project(title, description, imageFileName)
        flash('Project added successfully!', 'success')
        return redirect(url_for('projects'))

    return render_template('contact.html')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)