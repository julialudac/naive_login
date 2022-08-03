import './App.css';
import { useState } from 'react';
import {Modal} from './Modal'

function App() {
  let [username, setUsername] = useState(''); 
  let [email, setEmail] = useState('');
  let [isLogged, setLogged] = useState(false);
  let [isOpen, setIsOpen] = useState(false);

  const handleNameChange = e => setUsername(e.target.value);

  const login = async () => {
    const url = "http://server/profile/" + username;

    const response = await fetch(url);
    if(response.status === 200) {
      setEmail((await response.json())["email"]);
      setLogged(true);
    }
  }

  const changeMail = async(new_email) => {
    const url = "http://server/edit";
  
    const response = await fetch(url, {
      method: 'POST',
      headers: {'Content-type': 'application/json'},
      body: JSON.stringify({"username": username, "new_email": new_email})
    });

    setEmail(new_email);
  }

  if (!isLogged) {
    return (
      <div className="App">
        username: <input type="text" value={username} onChange={handleNameChange} /> <br/>
        <button onClick={login}>Login</button>
      </div>
    );
  }
  return (
    <div>
      <h1>User infos</h1>
      <p>email: {email}</p>
      <button onClick={() => setIsOpen(true)}>Edit</button>

      <Modal open={isOpen} onClose={() => setIsOpen(false)} changeMail={changeMail}>
      </Modal>
    </div>
  );


}

export default App;