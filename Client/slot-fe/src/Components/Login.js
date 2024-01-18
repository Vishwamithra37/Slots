import axios from 'axios';
import React, { useState } from 'react';
import { Link,useNavigate } from 'react-router-dom';


const Login = () => {
    
    const [Email,setUser]= useState()
    const [Password,setPassword]= useState()
    const [showPassword, setShowPassword] = useState(false);
    const navigate =useNavigate()
    const togglePasswordVisibility = () => {
      setShowPassword(!showPassword);
  };


    

    
    
    const handleSubmit=async (e)=>{
        e.preventDefault();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if(!emailRegex.test(Email)){
          alert("please enter a valid email address")
          return;
        }
        const passwordRegex=/^(?=.*[a-zA-Z])(?=.*\d).{8,}$/;
        if(!passwordRegex.test(Password)){
          alert("password must be 8 charcters long and using alphanumeric password")
          return;
        }
        try {
          const response = await axios.post('http://localhost:5000/users_rel_routes/user_login', {
              Email,
              Password,
          });
          const userData = response.data;
          console.log(userData);
          navigate('/Nav');
          // Handle successful login, e.g., redirect to dashboard
      } catch (error) {
          console.error('Error:', error);
          if (error.response && error.response.data) {
              console.error('Response Data:', error.response.data);
          }
          alert('Login failed. Please check your credentials and try again.');
      }
        
    }
        
    
    
 
  
 
 
  
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-cover bg-center " 
    
     style={{
        backgroundImage: "url('tiv.jpg')",
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        width: '100vw', // Set the width to the full viewport width
        height: '100vh', // Set the height to the full viewport height
      }}>
    {/* Rest of your code */}
    <div className="flex justify-start align-left w-2/3">
    
      <h1 className="text-4xl font-bold text-gray-900  text-left w-3/4">Login Page</h1>
      </div>
    
      
      <br/>
      
     

      <div className="flex  justify-start w-3/4">
       
        <form  className="bg-blue-200 shadow-lg rounded px-12 pt-6 pb-8 mb-4 align-left w-3/2"  onSubmit={handleSubmit}>
        <div className= "mb-4 ">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">
        email
            </label>
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type='email'
        name='email'
        placeholder='enter email address'
        //className='form-control'
        value={Email}
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
      
        value={Password}
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

