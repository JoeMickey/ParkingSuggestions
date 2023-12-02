class lotModel{
    id:number;
    title:string;
    lat:number;
    lng:number;
    condition:string;
    
    constructor(id:number,title:string,lat:number,lng:number,condition:string){
        this.id = id;
        this.title = title;
        this.lat = lat;
        this.lng = lng;
        this.condition = condition;
        
    }
}
export default lotModel