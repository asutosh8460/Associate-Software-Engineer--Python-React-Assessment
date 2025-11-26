import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Comments({ taskId }) {
  const [comments, setComments] = useState([]);
  const [text, setText] = useState('');

  useEffect(() => {
    axios.get(`/comments?task_id=${taskId}`).then(res => setComments(res.data));
  }, [taskId]);

  const handleAdd = () => {
    axios.post('/comments', { task_id: taskId, content: text }).then(() => {
      setText('');
      axios.get(`/comments?task_id=${taskId}`).then(res => setComments(res.data));
    });
  };

  return (
    <div>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={handleAdd}>Add Comment</button>
      <ul>
        {comments.map(c => <li key={c.id}>{c.content}</li>)}
      </ul>
    </div>
  );
}

export default Comments;
