# tests/test_cli.py

import pytest
import subprocess

def test_help_command():
    result = subprocess.run(['python3', 'a2a_gateway_cli.py', '--help'], capture_output=True, text=True)
    assert 'A2A Gateway CLI Tool' in result.stdout

def test_invalid_command():
    result = subprocess.run(['python3', 'a2a_gateway_cli.py', 'invalid'], capture_output=True, text=True)
    combined_output = result.stdout + result.stderr  # <--- corregge qui
    assert 'usage' in combined_output.lower()
