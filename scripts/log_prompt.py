"""Append a prompt entry to .prompt/dev_notes.md.

Usage examples:
    python scripts/log_prompt.py "The prompt text here" --user "User Name"
    python scripts/log_prompt.py "The prompt text here" --user "User Name" --assistant "Short assistant summary"

This script will create the .prompt directory and dev_notes.md if missing. If
the optional `--assistant` text is provided the script will append the user's
prompt and then the assistant summary as a paired entry.
"""
from __future__ import annotations

import argparse
import datetime
from pathlib import Path


LOG_DIR = Path(__file__).resolve().parents[1] / '.prompt'
LOG_FILE = LOG_DIR / 'dev_notes.md'


def ensure_log():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    if not LOG_FILE.exists():
        LOG_FILE.write_text('# Development Prompt Log\n\nCreated: {}\n\n---\n\n'.format(datetime.date.today()))


def append_prompt(prompt: str, user: str | None, assistant: str | None = None):
    """Append one or two entries to the log.

    If `assistant` is provided, the function will append the user's prompt
    first and then the assistant summary under the same timestamp block.
    """
    ensure_log()
    ts = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
    header = f'### {ts}\n\n'
    entry = header
    if user:
        entry += f'{user}: "{prompt}"\n\n'
    else:
        entry += f'Prompt: "{prompt}"\n\n'

    if assistant:
        entry += f'Assistant summary: "{assistant}"\n\n'

    entry += '---\n\n'
    with LOG_FILE.open('a', encoding='utf-8') as fh:
        fh.write(entry)
    print(f'Appended prompt to {LOG_FILE}')


def main():
    parser = argparse.ArgumentParser(description='Append a prompt entry to .prompt/dev_notes.md')
    parser.add_argument('prompt', help='Prompt text to log')
    parser.add_argument('--user', help='User name or role (optional)', default='User')
    parser.add_argument('--assistant', help='Assistant summary text (optional)', default=None)
    args = parser.parse_args()
    append_prompt(args.prompt, args.user, args.assistant)


if __name__ == '__main__':
    main()
