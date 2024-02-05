import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {ReactComponent as ArrowLeft} from '../assets/arrow-left.svg'


const NotePage = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [note, setNote] = useState(null);
const getNote = async () => {
    try {
      if (id === 'new') return
      const response = await fetch(`/api/notes/${id}/`);
      const data = await response.json();
      setNote(data);
    } catch (error) {
      console.error('Error fetching note:', error);
    }
  };
  useEffect(() => {
    getNote();
  }, [id]);

  
  

  const updateNote = async () => {
    try {
      
      await fetch(`/api/notes/${id}/update/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(note),
      });
    } catch (error) {
      console.error('Error updating note:', error);
    }
  };

  const createNote = async () => {
    try {
      await fetch('/api/notes/create/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(note),
      });
    } catch (error) {
      console.error('Error updating note:', error);
    }
  };

let deleteNote =async ()=>{
  try {
    await fetch(`/api/notes/${id}/delete/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      
    });
    navigate('/');
    // this a comment
  } catch (error) {
    console.error('Error updating note:', error);
  }
}

  const handleSubmit = async () => {
    if(id !=='new' && !note.body){
     await deleteNote()
    }
    else if(id !== 'new'){
      await updateNote();
    }
    else if(id === 'new' && note !== null){
      
     await createNote()
    }
    
    navigate('/');
  };

  return (
    <div className="note">
      <div className="note-header">
        <h3 onClick={handleSubmit}><ArrowLeft/></h3>
        {id !== 'new'?(<button onClick={deleteNote}>Delete</button>):(<button onClick={handleSubmit}>Done</button>)}
        
      </div>
      <textarea
        onChange={(e) => {
          setNote({ ...note, body: e.target.value });
        }}
        defaultValue={note?.body}
      ></textarea>
    </div>
  );
};

export default NotePage;
