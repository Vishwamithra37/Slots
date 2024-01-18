import React from 'react';
import { Link } from 'react-router-dom';


const Navbar = () => {
  return (
    <nav className="bg-gray-800 p-4">
      <div className="flex items-center justify-between">
        {/* Replace 'logo.png' with the correct path to your logo image */}
        <Link to="/">
          <img src="./new1.png" alt="Logo" className="h-8" width="50" height="200"/> 
          {/* Adjust 'h-8' class to set the height of your logo */}
        </Link>
        <div className='flex items-center justify-center'>
          <Link to="/Home" className="text-white mr-4">Home</Link>
          <Link to="/about" className="text-white mr-4">About</Link>
          <Link to="/history" className="text-white">History</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
