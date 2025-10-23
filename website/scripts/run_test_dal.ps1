# Run DAL tests locally: creates/seeds projects.db and lists projects
Set-Location -Path (Join-Path $PSScriptRoot '..')
python - <<'PY'
from DAL import init_db, get_projects, add_project
init_db()
print('DB initialized/seeding complete')
projects = get_projects()
print('Before insert:', len(projects))
for p in projects:
    print('-', p['id'], p['title'], p.get('imageFileName'))
new_id = add_project('PS Test Project', 'Inserted from PowerShell script', 'ps_test.png')
print('Inserted new project id', new_id)
projects = get_projects()
print('After insert:', len(projects))
for p in projects[:5]:
    print('-', p['id'], p['title'], p.get('imageFileName'))
PY