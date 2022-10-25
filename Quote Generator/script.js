const quoteText=document.querySelector(".quote"),
authorName=document.querySelector(".author"),
readme=document.querySelector(".speech"),
btngenerate=document.querySelector(".generateQuote");


function generate(){
    fetch("https://api.quotable.io/random").then(res =>res.json()).then(result =>{
        
        quoteText.innerText=result.content;
        authorName.innerText=result.author;
    });
}
readme.addEventListener("click",() =>{
    let utterance=new SpeechSynthesisUtterance(`${quoteText.innerText} by ${authorName.innerText}`)
    speechSynthesis.speak(utterance);
})

btngenerate.addEventListener("click",generate);

