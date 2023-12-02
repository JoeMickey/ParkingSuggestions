import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; 
import { MapComponent } from './MapComponent';
import lotModel from '../model/lotModel';

export const LocationInput = () => {
  const [name, setName] = useState('');
  const [street, setStreet] = useState('');
  const [map, setMap] = useState(false)
  const [lots,setLots] = useState<lotModel[]>([new lotModel(1,"San Diego civil theatre ",  32.6157,-117.0611,"Low Risk"),new lotModel(2,"San Diego civil theatre",  32.7167,-117.1622,"High Risk")])
  const [httpError, setHttpError] = useState(null);

  
  const handleSubmit = (event:any) => {
    event.preventDefault();
    /*
    const fetchBooks = async () => {
      const url: string = "http://localhost:8080/api/lots";

      const response = await fetch(url);

      if (!response.ok) {
          throw new Error('Something went wrong!');
      }

      const responseJson = await response.json();

      const responseData = responseJson._embedded.lots;

      const returnLot: lotModel = responseData;

      setLot(returnLot);
  };
  fetchBooks().catch((error: any) => {
      setHttpError(error.message);
  })*/
    setMap(true)
  };

  return (
    map == false? <div className="container mt-3">
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="longitude" className="form-label">Street Name</label>
          <input 
            type="text" 
            className="form-control" 
            id="longitude" 
            value={name} 
            onChange={e => setName(e.target.value)} 
          />
        </div>
        <button type="submit" onClick = {handleSubmit} className="btn btn-primary">Submit</button>
      </form>
    </div> : <MapComponent lots = {lots} />
  );
};
