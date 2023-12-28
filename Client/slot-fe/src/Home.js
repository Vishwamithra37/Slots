import React from 'react'
import { useNavigate } from 'react-router-dom';

const Home = () =>{
  const navigate =useNavigate()


  function handleClick() {
    navigate('/register');
  }
  
  function handleClicklogin() {
    navigate('/login');
  }
    return (
        <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-green-500">
            <h1 className="text-4xl font-bold text-blue-900">welcome to home page</h1>
            <br/>

            <button className="bg-blue-500 hover:bg-blue-700 text-white 
            font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type='submit' onClick={handleClick}> admin Registration</button>
            <br/>
            <p className="inline-block align-baseline font-bold text-sm text-red-500 hover:text-blue-800">
              Already registered user then click login</p><br/>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 
            rounded focus:outline-none focus:shadow-outline" type='submit'  onClick={handleClicklogin}>login</button>
      </div>
    )
  }


export default Home;