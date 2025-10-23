import sqlite3
from pathlib import Path
from typing import List, Dict, Any

DB_PATH = Path(__file__).parent / 'projects.db'


def get_connection():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create the projects table if it doesn't exist."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = get_connection()
    with conn:
        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                imageFileName TEXT
            )
            '''
        )
        # Seed with example projects if table is empty
        cur = conn.execute('SELECT COUNT(1) as cnt FROM projects')
        row = cur.fetchone()
        if row and row['cnt'] == 0:
            conn.execute(
                'INSERT INTO projects (title, description, imageFileName) VALUES (?, ?, ?)',
                ('Victory Harmonica Case', 'IT deliverables for a fictional harmonica company.', 'Project1.png')
            )
            conn.execute(
                'INSERT INTO projects (title, description, imageFileName) VALUES (?, ?, ?)',
                ('3+1 Case Competition', 'MSIS case competition centered around Digital Humans and IU Health.', 'Project2.png')
            )
    conn.close()


def add_project(title: str, description: str, imageFileName: str | None = None) -> int:
    conn = get_connection()
    with conn:
        cur = conn.execute(
            'INSERT INTO projects (title, description, imageFileName) VALUES (?, ?, ?)',
            (title, description, imageFileName),
        )
        project_id = cur.lastrowid
    conn.close()
    return project_id


def get_projects() -> List[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute('SELECT id, title, description, imageFileName FROM projects ORDER BY id DESC')
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]
