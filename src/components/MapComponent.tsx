import React, { useRef, useEffect } from 'react';
import lotModel from '../model/lotModel';

export const MapComponent: React.FC<{lots:lotModel[]}> = (props) => {
    const mapRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (mapRef.current) {
            const map = new window.google.maps.Map(mapRef.current, {
                center: { lat: props.lots[0].lat, lng: props.lots[0].lng },
                zoom: 10,
            });
            props.lots.forEach(lot => {
                const marker = new window.google.maps.Marker({
                    position: { lat: lot.lat, lng: lot.lng },
                    map: map
                });

                const infoWindow = new window.google.maps.InfoWindow({
                    content: `<div><strong>${lot.condition}</strong><p>${lot.title}</p></div>` // 替换为您想要显示的信息
                });

                marker.addListener('click', () => {
                    infoWindow.open(map, marker);
                });
            });
        }
    }, [[props.lots]]);

    return (<div ref={mapRef} style={{ height: '550px', width: '100%' }} />);
};