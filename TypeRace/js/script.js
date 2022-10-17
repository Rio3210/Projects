const typing_text=document.querySelector(".typing-text p"),
inputField=document.querySelector(".wrapper .input-field"),
mistakeTag=document.querySelector(".mistake span"),
wpmTag=document.querySelector(".wpm span"),
cpmTag=document.querySelector(".cpm span"),
tryAgainBtn=document.querySelector("button")
timeTag=document.querySelector(".time span b");

let timer,
maxTime=60,
timeLeft =maxTime,
charIndx =mistakes=isTyping=0;

function randomParagraph(){
    let randIndex=Math.floor(Math.random()* paragraphs.length);
    typing_text.innerHTML="";
    paragraphs[randIndex].split("").forEach(span =>{
        let spanTag=`<span>${span}</span>`;
        typing_text.innerHTML+=spanTag;
    });
    typing_text.querySelectorAll("span")[0].classList.add("active")
    document.addEventListener("keydown", () => inputField.focus());
    typing_text.addEventListener("click", () => inputField.focus());
}

function initTyping(){
    const characters =typing_text.querySelectorAll("span");
    let typedchar =inputField.value.split("")[charIndx];

    if(charIndx < characters.length && timeLeft >0){
        if(!isTyping){
            timer=setInterval(initTimer,1000);
            isTyping=true;
        }
        
        if (typedchar == null){
            charIndx-=1;
            if (characters[charIndx].classList.contains("incorrect")){
                mistakes-=1;
            }
            characters[charIndx].classList.remove("correct","incorrect");
        }
        else{
            if(characters[charIndx].innerText===typedchar){
                characters[charIndx].classList.add("correct");
                
            }
            else{
                mistakes++;
                characters[charIndx].classList.add("incorrect");
                
            }
            charIndx+=1;
        }
         
        characters.forEach(span =>span.classList.remove("active")); // helps to switch the underline effect from letter to letter 
        characters[charIndx].classList.add("active")
    
        let wpm =Math.round((((charIndx - mistakes) /5) /(maxTime-timeLeft))*60)   //the number of words is calculated by dividing the number of characters typed by 5. The number of "words" is then divided by the total elapsed time (in minutes).
        qpm=wpm <0 || !wpm || wpm === Infinity ? 0 : wpm;
        mistakeTag.innerText=mistakes;
        wpmTag.innerText=wpm;
        cpmTag.innerText=charIndx-mistakes;
    }
    else{
        clearInterval(timer);
    }
}
function  initTimer(){
    if(timeLeft >0){
        timeLeft-=1;
        timeTag.innerText=timeLeft;
    }
    else{
        inputField.value="";
        clearInterval(timer);
    }
}
function resetGame(){
    randomParagraph();
    inputField.value="";
    clearInterval(timer);
    timeLeft =maxTime;
    charIndx =mistakes=isTyping=0;
    timeTag.innerText=timeLeft;
    mistakeTag.innerText=mistakes;
    wpmTag.innerText=0;
    cpmTag.innerText=0;



}
randomParagraph()
inputField.addEventListener("input",initTyping);
tryAgainBtn.addEventListener("click",resetGame)