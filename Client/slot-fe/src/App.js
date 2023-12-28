
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from './Login'
import Home from './Home'
import Register from './Register'





import {BrowserRouter,Routes,Route} from 'react-router-dom'

function App() {
  
  return (
    <BrowserRouter>
    <Routes>
    <Route path='/' element={<Home />}></Route>
      
    <Route path='/login' element={<Login />}></Route>
    <Route path='/register' element={<Register />}></Route>
      
      
      
    </Routes>
    </BrowserRouter>
    
  )
  
    
}

export default App;
