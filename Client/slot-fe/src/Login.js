import axios from 'axios';
import React, { useState } from 'react';
import { Link,useNavigate } from 'react-router-dom';


const Login = () => {
    
    const [username,setUser]= useState()
    const [password,setPassword]= useState()
    const [showPassword, setShowPassword] = useState(false);
    const navigate =useNavigate()
    const togglePasswordVisibility = () => {
      setShowPassword(!showPassword);
  };


    

    
    
    const handleSubmit=async (e)=>{
        e.preventDefault();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if(!emailRegex.test(username)){
          alert("please enter a valid email address")
          return;
        }
        const passwordRegex=/^(?=.*[a-zA-Z])(?=.*\d).{8,}$/;
        if(!passwordRegex.test(password)){
          alert("password must be 8 charcters long and using alphanumeric password")
          return;
        }
        try {
          const response = await axios.post('http://127.0.0.1:5000/users_rel_routes/user_login', {
            username,
            password,
        });
        console.log(response.data); 
          if (response.ok) {
              const data = await response.json();
              // Do something with the response data if needed
              console.log(data);
              navigate('/');
          } else {
              console.error('Failed to log in');
              // Handle error cases here (display error messages, etc.)
          }
      } catch (error) {
          console.error('wrong credentials:', error);
          alert("credentials are invalid")
          // Handle network errors or exceptions here
      }
      
        
    }
        
    
    
 
  
 
 
  
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-violet-500">
      <h1 className="text-4xl font-bold text-gray-900 ">Login Page</h1>
      <br/>

      <div className="w-full max-w-md">
       
        <form  className="bg-blue-200 shadow-lg rounded px-12 pt-6 pb-8 mb-4" onSubmit={handleSubmit}>
        <div className= "mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
              Username
            </label>
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type='text'
        name='username'
        placeholder='enter email address'
        //className='form-control'
        value={username}
        onChange={(e)=> setUser(e.target.value)}
        
        required
        />
        </div>
        
        <div className="mb-6">
        <div className="form-group">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
              Password
            </label>
        <div style={{ position: 'relative' }}>
            
        
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
        type={showPassword ? 'text' : 'password'} 
        
        name='password'
        placeholder='password' 
      
        value={password}
        onChange={(e)=> setPassword(e.target.value) }
        style={{ paddingRight: '2.5rem' }}
        
                    
       
        
        
        required
                
        />
        <span
                    onClick={togglePasswordVisibility}
                    style={{
                        position: 'absolute',
                        top: '30%',
                        transform: 'translateY(-50%)',
                        right: '4px',
                        cursor: 'pointer',
                    }}
                >
                    {showPassword ? '👁️' : '👁️‍🗨️'}
                </span>
        
        </div>
        </div>
        </div>
        
        <div className="flex items-center justify-between">
        <button  className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type='submit'>Login</button>
        
        <p className="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800">
          Not registered yet? <Link to ='/register' className='text-red-500'>Register Here</Link>
        </p>
        </div>
        <br/>
        
      </form>
      </div>
    </div>
  )
    }

export default Login

