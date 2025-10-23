import tempfile
from pathlib import Path

import DAL


def test_database_init_and_add_project(tmp_path: Path):
    # Use a temp DB path so we don't touch the repository DB
    temp_db = tmp_path / "projects_test.db"
    # Patch DAL.DB_PATH to point to the temp DB
    orig_db_path = DAL.DB_PATH
    try:
        DAL.DB_PATH = temp_db
        # Initialize DB
        DAL.init_db()
        projects_before = DAL.get_projects()
        # Add a project
        new_id = DAL.add_project("Test", "Desc", "test.png")
        assert isinstance(new_id, int) and new_id > 0
        projects_after = DAL.get_projects()
        assert len(projects_after) == len(projects_before) + 1
    finally:
        # restore
        DAL.DB_PATH = orig_db_path
