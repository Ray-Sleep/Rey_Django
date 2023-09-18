let switchCtn = document.querySelector('#switch-cnt');
let switchC1 = document.querySelector("#switch-c1");
let switchC2 = document.querySelector("#switch-c2");
let switchCircle = document.querySelectorAll(".switch-circle");
let switchBth = document.querySelectorAll(".switch-btn");
let aContainer = document.querySelector("#a-container");
let bContainer = document.querySelector("#b-container");
let allButtons =  document.querySelectorAll(".submit");

let getButtons = (e) => e.preventDefault()
let changeForm = (e) => {
    //修改类名
    switchCtn.classList.add('is-gx');
    setTimeout(function (){
        switchCtn.classList.remove("is-gx");
    },1500)
    switchCtn.classList.toggle("is-txr");
    switchCircle[0].classList.toggle("is-txr");
    switchCircle[1].classList.toggle("is-txr");

    switchC1.classList.toggle("is-hidden");
    switchC2.classList.toggle("is-hidden");
    aContainer.classList.toggle("is-txl");
    bContainer.classList.toggle("is-txl");
    bContainer.classList.toggle("is-z");
}

// 点击切换
let shell = (e) => {
    for (var i=0 ;i < allButtons.length;i++)
        allButtons[i].addEventListener("click",getButtons);
    for (var i=0 ; i< switchBth.length;i++)
        switchBth[i].addEventListener('click',changeForm);
}
window.addEventListener('load',shell);