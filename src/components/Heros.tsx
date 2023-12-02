import React from "react";
import { Link } from "react-router-dom";

export const Heros = () => {

    return (
        <div>
            <div className='d-none d-lg-block'>
                <div className='row g-0 mt-5'>
                    <div className='col-sm-6 col-md-6'>
                        <div className='col-image-left'></div>
                    </div>
                    <div className='col-4 col-md-4 container d-flex justify-content-center align-items-center'>
                        <div className='ml-2'>
                            <h1>Worried about getting a parking ticket?</h1>
                            <p className='lead'>
                                Our team will tell you if they are prone to parking tickets based on the street name and the time, with the help of Google Map API
                            </p>
                            
                            
                        </div>
                    </div>
                </div>
                <div className='row g-0'>
                    <div className='col-4 col-md-4 container d-flex 
                        justify-content-center align-items-center'>
                        <div className='ml-2'>
                            <h1>Brief introduction to our research</h1>
                            <p className='lead'>
                            Our research conclusion would show and explain why there are times and places where more parking tickets can be found, so that we can provide some tips for parking when it’s almost impossible to park in the parking lot. 
                            </p>
                        </div>
                    </div>
                    <div className='col-sm-6 col-md-6'>
                        <div className='col-image-right'></div>
                    </div>
                </div>
            </div>
        </div>
    );
}