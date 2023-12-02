import React from 'react';

type ParkingLotProps = {
    name: string;
    location: string;
    spaces: number;
};

const ParkingLot: React.FC<ParkingLotProps> = ({ name, location, spaces }) => {
    return (
        <div className="card my-2">
            <div className="card-body">
                <h5 className="card-title">{name}</h5>
                <h6 className="card-subtitle mb-2 text-muted">Location: {location}</h6>
                <p className="card-text">Spaces available: {spaces}</p>
            </div>
        </div>
    );
};

export default ParkingLot;