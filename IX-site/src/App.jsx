import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'

function App() {
  const [count, setCount] = useState(0)
  const [char, setChar] = useState("")
  const [uid, setUid] = useState("")
  const api = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    withCredentials: true,  // Include cookies in requests
  })

  const findUser = async(e) => {
    console.log(uid)
    e.preventDefault()
    const response = await api.post('/testRoute/'+{uid}+'/4')
    .then(response =>{
      console.log(response.data.showcase)
        setChar(response.data.showcase)
      })
      .catch(error => {
        console.log('error')
      })
  }
  return (
    <>
      <h1>HSR-IX</h1>
      <div className="card">
        <form>
          <label htmlFor="input-bar">UID: </label>
          <input 
            type="text"
            onChange={(e) => setUid(e.target.value)}
            placeholder="Enter UID"
          />
          <button onClick={findUser}>
            Find characters
          </button>
        </form>
      </div>
      {char !== "" ? (
  char.map((characters, index) => (
    <div key={index}>
      Character: {characters}
    </div>
  ))
) : (
  <></>
)}
    </>
  )
}

export default App
