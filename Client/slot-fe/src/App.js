import React from 'react';

import {BrowserRouter,Routes,Route} from 'react-router-dom'

import Land from './Components/Landing';
import Navbar from './Components/Navbar';
import Home from './Components/Home';
import History from './Components/History';

import About from './Components/About';


import Login from './Components/Login';
import Register from './Components/Register';



const App = () => {
  return (
    <BrowserRouter>
    <Routes>
      

      <Route path='/' element={<Land />}></Route>
      <Route path='/about' element={<About />}></Route>
      <Route path='/Home' element={<Home />}></Route>
      <Route path='/history' element={<History/>}></Route>
      <Route path='/Nav' element={<Navbar />}></Route>
      
      
      <Route path="/login" element={<Login />}></Route>
      <Route path="/register" element={<Register />}></Route>
      
      
        
      
    </Routes>
    </BrowserRouter>
    
      
     
      
    
  );
};

export default App;
