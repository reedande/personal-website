Prompt logging directory
========================

Purpose
-------

This directory stores a running log of user prompts and assistant notes in `dev_notes.md`.

How to append a prompt
----------------------

Use the helper script from the repository root:

    python scripts/log_prompt.py "Your prompt text here" --user "User"

The script will create the `.prompt` directory and `dev_notes.md` if they don't exist. Each entry is timestamped.

Manual edits
------------

You can also edit `dev_notes.md` directly if needed.
