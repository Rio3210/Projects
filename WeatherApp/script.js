const wrapper=document.querySelector(".wrapper"),
inputPart=wrapper.querySelector(".input-part"),
infoTxt=inputPart.querySelector(".info-text"),
inputField=inputPart.querySelector("input"),
getBtn=inputPart.querySelector("button"),
Icon=wrapper.querySelector(".weather-show img"),
backArrow=wrapper.querySelector("header i");

let api;

let apikey= "YourAPI here";
inputField.addEventListener( "keyup", e =>{
    if (e.key == "Enter" && inputField.value!=""){
        requestApi(inputField.value);
    }
});

getBtn.addEventListener("click",() =>{
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(OnSuccess,onError);
    }else{
        alert("Your browser does not support Geolocation api:(")
    }
});

function OnSuccess(position){
    
    const{latitude,longtude}=position.coords;
    api=`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longtude}&units=metric&appid=2ed2367df21f178ed5e1451ce9beedf2`
    fetchData()
}
function onError(error){
    infoTxt.innerText=error.message;
    infoTxt.classList.add("error")
}

function fetchData(){
    infoTxt.innerText="Getting Weather details"
    infoTxt.classList.add("loading")
    fetch(api).then(response =>response.json()).then(result => weatherDetails(result));
}
function requestApi(city){
    api="https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + apikey;
    fetchData()
}
function weatherDetails(info){
    infoTxt.classList.replace("loading","error")
    if(info.cod=="404"){
        infoTxt.innerText=`${inputField.value} is not a valid city name.`
        
    }else{
        const city =info.name;
        const country = info.sys.country;
        const {description, id}= info.weather[0];
        const {feels_like, humidity, temp} = info.main;

        
        wrapper.querySelector(".temprature .number").innerText = Math.floor(temp);
        wrapper.querySelector(".weather").innerText = description;
        wrapper.querySelector(".location span"). innerText = `${city}, ${country}`;
        wrapper.querySelector(".temprature .numb-2").innerText = Math.floor(feels_like);
        wrapper.querySelector(".humidity span"). innerText = `${humidity}%`;

        if (id==800){
            Icon.src="Weather Icons/clear.svg"
        }else if (id>=200 && id<=232){
            Icon.src="Weather Icons/storm.svg"
        }else if (id>=600 && id<=622){
            Icon.src="Weather Icons/snow.svg"
        }else if (id>=701 && id<=781){
            Icon.src="Weather Icons/haze.svg"
        }else if (id>=801 && id<=804){
            Icon.src="Weather Icons/cloud.svg"
        }else if ((id>=300 && id<=321) ||(id>=500 && id<=531)){
            Icon.src="Weather Icons/rain.svg"
        }

        infoTxt.classList.remove("loading","error")
        wrapper.classList.add("active");
    }
    
}
backArrow.addEventListener("click",() => {
    wrapper.classList.remove("active");
    inputField.value="";
});
