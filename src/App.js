import React from 'react';
import Button from '@material-ui/core/Button';
import axios from "axios";

const upload = () =>{
  fetch('http://localhost:8000/upload/', { method: 'POST'})
};
const display = () =>{
  fetch('http://localhost:8000/display/', { method: 'GET' }).then(response => alert(response.status))

};

const App = () => {

  return (
    <div style={{
      display: 'flex',
      margin: 'auto',
      width: 400,
      flexWrap: 'wrap',
    }}>
      <div style={{ width: '100%', float: 'left' }}>
        <h3>Hello, User</h3> <br />
      </div>
      <Button variant="contained" color="primary" onClick={upload}>
        Upload
      </Button>
      <Button variant="contained" color="primary"  onClick={display}>
        Display
      </Button>
    </div>
  );
}

export default App;