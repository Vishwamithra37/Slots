import React, { useState } from 'react'
import axios from 'axios'
import { Link,useNavigate} from 'react-router-dom'

const Register= () => {
    const [Fullname,setName]= useState()
    
    const [Email,setEmail]= useState()
    const [Contact_no,setContact] = useState()
    const [Password,setPassword]= useState()
    const [Confirm_password,setConfirmPassword]= useState()
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
      if (!nameRegex.test(Fullname) ){
        alert("fullname should contain only letters" );
        return;
      }
      if(!Fullname ||!Email ||!Password){
        alert("please fill in all fields");
        return;
      }
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if(!emailRegex.test(Email)){
          alert("please enter a valid email address")
          return;
        }
        const phoneNumberRegex = /^\d{10}$/; // 10-digit number regex
          if(!phoneNumberRegex.test(Contact_no)) {
            alert('Please provide a valid contact number');
            return;
            }
        const passwordRegex=/^(?=.*[a-zA-Z])(?=.*\d).{8,}$/;
        if(!passwordRegex.test(Password)){
          alert("password must be 8 charcters long and using alphanumeric password")
          return;
        }
        if (Password !== Confirm_password) {
          alert('Passwords do not match');
          return;
      }
      try {
        const response = await axios.post('http://localhost:5000/users_rel_routes/user_register', {
          Fullname,
          Contact_no,
          Email,
          Password,
          Confirm_password,
        }, {
          headers: {
            'Content-Type': 'application/json',
            'accept': 'application/json',
          },
        });
  
        const data = response.data;
        console.log(data);
        navigate('/login'); // Assuming registration was successful and navigating to login
      } catch (error) {
        console.error('Error:', error);
        if (error.response && error.response.data) {
          console.error('Response Data:', error.response.data);
        }
        alert('There was an error during registration. Please try again.');
      }
    }

    

    return (
      <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-cover bg-center " 
    
     style={{
        backgroundImage: "url('blue.jpg')",
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        width: '100vw', // Set the width to the full viewport width
        height: '100vh', // Set the height to the full viewport height
      }}>
        <div className="flex justify-start w-3/4">
    <div className="flex flex-col items-center justify-center min-h-screen py-2 ">
      <h1 className="text-4xl font-bold text-gray-900">Registration Form</h1>
      <br/>
      <div className="flex justify-start w-3/4"></div>
      <form  className="bg-blue-200 shadow-lg rounded px-12 pt-6 pb-8 mb-4" onSubmit={handleSubmit}>
      <div className="mb-4">
      <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="Fullname">
      Fullname
            </label>
      <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type='text'
        name='Fullname'
        placeholder=' enter Fullname'
       
        value={Fullname}
        onChange={(e)=> setName(e.target.value)}
        required
        />
        </div>
        
        
        
        
        

        <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="Email">
              Username
            </label>
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type='text'
        name='Email'
        placeholder='enter email address'
       
        value={Email}
        onChange={(e)=> setEmail(e.target.value)}
    
        required
        />
        </div>
        <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="Contact_no">
        Contact_no
            </label>
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type='number'
        name='Contact_no'
        placeholder='enter contact number'
       
        value={Contact_no}
        onChange={(e)=> setContact(e.target.value)}
    
        required
        />
        
        
        </div>
        <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="Password">
              Password
            </label>
            <div style={{ position: 'relative' }}>
            
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
        type={showPassword ? 'text' : 'Password'} 
        name='Password'
        placeholder=' enter alphanumeric password'
       
        value={Password}
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
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="Confirm_password">
        Confirm_password
                    </label>
            <div style={{ position: 'relative' }}>
            
        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
        type={showPassword ? 'text' : 'password'} 
        name='Confirm_password'
        placeholder='re enter your password'
       
        value={Confirm_password}
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
    </div>
    </div>
  )
    }


export default Register;


