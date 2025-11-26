import json

def test_create_comment(client):
    response = client.post('/comments', json={'task_id': 1, 'content': 'Test comment'})
    assert response.status_code == 201

def test_get_comments(client):
    response = client.get('/comments?task_id=1')
    assert response.status_code == 200

def test_update_comment(client):
    client.post('/comments', json={'task_id': 1, 'content': 'Old'})
    response = client.put('/comments/1', json={'content': 'Updated'})
    assert response.status_code == 200

def test_delete_comment(client):
    client.post('/comments', json={'task_id': 2, 'content': 'To delete'})
    response = client.delete('/comments/2')
    assert response.status_code == 200
