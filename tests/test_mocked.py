# tests/test_mocked.py

import pytest
import a2a_gateway_cli
from unittest.mock import patch

def test_publish_agent_mock():
    with patch('requests.post') as mock_post, patch('builtins.open', create=True):
        mock_post.return_value.json.return_value = {'status': 'ok'}
        mock_post.return_value.raise_for_status = lambda: None
        a2a_gateway_cli.publish_agent('fake_path.json')

def test_send_task_mock():
    with patch('requests.post') as mock_post:
        mock_post.return_value.json.return_value = {'task_id': '123'}
        mock_post.return_value.raise_for_status = lambda: None
        a2a_gateway_cli.send_task('agent-id', 'Do something')

def test_check_status_mock():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'status': 'done'}
        mock_get.return_value.raise_for_status = lambda: None
        a2a_gateway_cli.check_status('task-id')
