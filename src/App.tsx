import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Footer } from './components/Footer';
import { Navbar } from './components/Navbar';
import { HomePage } from './components/HomePage';
import { LocationInput } from './components/LocationInput';
import { MapComponent } from './components/MapComponent';
import lotModel from './model/lotModel';
function App() {
  return (
    <Router>
    <div className='d-flex flex-column min-vh-100'>
      
      <Navbar />
      <div className='flex-grow-1'>
        <Routes>
          <Route path='' element={<HomePage />} />
          <Route path='/home' element={<HomePage />} />
          <Route path='/search' element={<LocationInput />} />
        </Routes>
      </div>
      <Footer />
    </div>
    </Router>
  );
}

export default App;
