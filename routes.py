from flask import Blueprint, request, jsonify
from .models import db, Comment

comment_routes = Blueprint('comments', __name__)

@comment_routes.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    comment = Comment(task_id=data['task_id'], content=data['content'])
    db.session.add(comment)
    db.session.commit()
    return jsonify({'id': comment.id}), 201

@comment_routes.route('/comments', methods=['GET'])
def get_comments():
    task_id = request.args.get('task_id')
    comments = Comment.query.filter_by(task_id=task_id).all()
    return jsonify([{'id': c.id, 'content': c.content} for c in comments])

@comment_routes.route('/comments/<int:id>', methods=['PUT'])
def update_comment(id):
    data = request.get_json()
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({'error': 'Not found'}), 404
    comment.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Updated'})

@comment_routes.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({'error': 'Not found'}), 404
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Deleted'})
