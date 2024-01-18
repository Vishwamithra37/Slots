import React from 'react'
import { useNavigate } from 'react-router-dom';

const Landing = () =>{
  const navigate =useNavigate()


  function handleClick() {
    navigate('/register');
  }
  
  function handleClicklogin() {
    navigate('/login');
  }
    return (
     

        <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-cover bg-center" 
          
    
      style={{
       backgroundImage: "url('tic.jpg')",
       backgroundSize: 'cover',
       backgroundRepeat: 'no-repeat',
       width: '100vw', // Set the width to the full viewport width
       height: '100vh', // Set the height to the full viewport height
     }}>
          
            <h3 className="text-7xl font-bold text-pink-900 text-left  w-3/4 ">welcome to slotzz</h3>
            <br/>
            <br/>
            <div className="flex justify-start w-1/2">
            <button className="bg-green-500 hover:bg-green-700 text-white 
            font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:text-blue-800   " type='submit' onClick={handleClick}> admin Registration</button>
            </div>
            <br/>
            <p className="inline-block align-baseline font-bold text-sm text-red-500 hover:text-blue-800 text-left  w-1/2 ">
              Already registered user then click login</p><br/>
              <div className="flex justify-start w-1/2">
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 
            rounded focus:outline-none hover:text-red-800  " type='submit'  onClick={handleClicklogin}>login</button>
            </div>
      </div>
    )
  }


export default Landing;