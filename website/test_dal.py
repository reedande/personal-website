"""Test DAL functions: list projects, add a new one, and list again."""
from DAL import init_db, get_projects, add_project


def main():
    init_db()
    before = get_projects()
    print(f'Projects before insert: {len(before)}')
    for p in before:
        print('-', p['id'], p['title'], p.get('imageFileName'))

    new_id = add_project('Test Project', 'This is a test project inserted by test_dal.', 'test.png')
    print('Inserted new project with id', new_id)

    after = get_projects()
    print(f'Projects after insert: {len(after)}')
    for p in after[:5]:
        print('-', p['id'], p['title'], p.get('imageFileName'))


if __name__ == '__main__':
    main()
