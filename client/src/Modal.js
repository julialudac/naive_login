import React from 'react';
import { useState } from 'react';


const MODAL_STYLES = {
  position: "fixed",
  top: "0%",
  left: "0%",
  backgroundColor: "gray",
  padding: "50px",
  zIndex: 1000
};


export function Modal({ open, onClose, changeMail}) {
  let [new_email, setEmail] = useState('');

  const handleNewEmailChange = e => setEmail(e.target.value);
  const updateMail = async () => {
    changeMail(new_email);
  }

  if (!open) return null;
  return (
    <div style={MODAL_STYLES}>
      new email: <input type="text" value={new_email} onChange={handleNewEmailChange} /> <br/>
      <button onClick={updateMail}>Change email</button>
      <button onClick={onClose}>Close modal</button>
    </div>
  );
}
