import React, { useState } from 'react'
import axios from 'axios'
import { Link,useNavigate} from 'react-router-dom'

const Register= () => {
    const [fname,setName]= useState()
    const [lname,setLastName]= useState()
    const [username,setUser]= useState()
    const [contact,setContact] = useState()
    const [password,setPassword]= useState()
    const [confirmpassword,setConfirmPassword]= useState()
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);
    const navigate =useNavigate()
    const togglePasswordVisibility = () => {
      setShowPassword(!showPassword);
  };
  const toggleConfirmPasswordVisibility = () => {
    setShowConfirmPassword(!showConfirmPassword);
};
    
    const handleSubmit=async(e)=>{
      e.preventDefault()

      const nameRegex = /^[a-zA-z]+$/;
      if (!nameRegex.test(fname) || !nameRegex.test(lname)){
        alert("firstname and lastname should contain only letters" );
        return;
      }
      if(!fname ||!lname ||!username ||!password){
        alert("please fill in all fields");
        return;
      }
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if(!emailRegex.test(username)){
          alert("please enter a valid email address")
          return;
        }
        const phoneNumberRegex = /^\d{10}$/; // 10-digit number regex
          if(!phoneNumberRegex.test(contact)) {
            alert('Please provide a valid contact number');
            return;
            }
        const passwordRegex=/^(?=.*[a-zA-Z])(?=.*\d).{8,}$/;
        if(!passwordRegex.test(password)){
          alert("password must be 8 charcters long and using alphanumeric password")
          return;
        }
        if (password !== confirmpassword) {
          alert('Passwords do not match');
          return;
      }
      try {
        const response = await axios.post('http://127.0.0.1:5000/users_rel_routes/user_register', {
          fname,
          lname,
          contact,
          username,
          password,
          confirmpassword
      });
      console.log(response.data); 
        if (response.ok) {
            const data = await response.json();
            // Do something with the response data if needed
            console.log(data);
            navigate('/login');
        } else {
            console.error('Failed to log in');
            // Handle error cases here (display error messages, etc.)
        }
    } catch (error) {
        console.error('wrong credentials:', error);
        alert("credentials are invalid")
        // Handle network errors or exceptions here
    }
    

        //navigate("/login")
    }

    

    return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-violet-500">
      <h1 className="text-4xl font-bold text-gray-900">Registration Form</h1>
      <br/>
      <form  className="bg-blue-200 shadow-lg rounded px-12 pt-6 pb-8 mb-4" onSubmit={handleSubmit}>
      <div className="mb-4">
      <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="firstname">
              firstname
            </label>
      <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type='text'
        name='firstName'
        placeholder='firstName'
       
        value={fname}
        onChange={(e)=> setName(e.target.value)}
        required
        />
        </div>
        
        <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="lastname">
              lastName
            </label>
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type='text'
        name='lastName'
        placeholder='lastName'
        
        value={lname}
        onChange={(e)=> setLastName(e.target.value)}
        
        
        />
        </div>
        

        <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
              Username
            </label>
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type='text'
        name='username'
        placeholder='enter email address'
       
        value={username}
        onChange={(e)=> setUser(e.target.value)}
    
        required
        />
        </div>
        <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="contact">
              Contact number
            </label>
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type='number'
        name='contact'
        placeholder='enter contact number'
       
        value={contact}
        onChange={(e)=> setContact(e.target.value)}
    
        required
        />
        
        
        </div>
        <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
              password
            </label>
            <div style={{ position: 'relative' }}>
            
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
        type={showPassword ? 'text' : 'password'} 
        name='password'
        placeholder='password'
       
        value={password}
        onChange={(e)=> setPassword(e.target.value)}
        
        
                    
       
        required
        />
        <span
                    onClick={togglePasswordVisibility}
                    className="absolute top-1/3 transform -translate-y-1/2 right-3 cursor-pointer"

                    
                    
                >
                    {showPassword ? '👁️' : '👁️‍🗨️'}
                </span>
        
        </div>
        
        </div>
        <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="confirmpassword">
             Confirm password
            </label>
            <div style={{ position: 'relative' }}>
            
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
        type={showPassword ? 'text' : 'password'} 
        name='confirmpassword'
        placeholder='confirmpassword'
       
        value={confirmpassword}
        onChange={(e)=> setConfirmPassword(e.target.value)}
        style={{ paddingRight: '2.5rem' }}
        
                    
       
        required
        />
        <span
                    onClick={toggleConfirmPasswordVisibility}
                    className="absolute top-1/3 transform -translate-y-1/2 right-3 cursor-pointer"
                    
                >
                    {showPassword ? '👁️' : '👁️‍🗨️'}
                </span>
        
        </div>
        
        </div>
        
        
        <div className="flex items-center justify-between">
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type='submit'>Register</button>
        <p className="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800">
            Already registered? <Link to="/login"  className='text-red-500'>Login Here</Link>
        </p>
        </div>
        <br/>
      </form>
    </div>
  )
    }


export default Register;


