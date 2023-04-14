var imgElement = document.querySelector("img");

function khalidFunction() {
  alert("Thanks for Changing My color");
}

function turnOff(element) {
  element.innerText = "OFF";
}

function hideMonkey(element) {
  element.remove();
}

function over(element) {
  element.style.height = "5em";
}

function out(element) {
  element.style.height = "1em";
}

function changeOthers() {
  var target = document.querySelector("#khalid");

  target.style.backgroundColor = "red";
  setTimeout(khalidFunction, 5000);
}

function changeOthers2() {
  var target = document.querySelector("#khalid");

  target.style.backgroundColor = "yellow";
}

function changeSize() {
  imgElement.style.height = "3em";
  imgElement.style.width = "3em";
}

function imageChanger() {
  imgElement.src = "cat.jpg";
}


function chooseLunch(element) {
var target  = document.querySelector("h3");
target.innerText = "Thanks for selecting: "+element.value;
}


function setname(element){
var target  = document.querySelector("h3");
target.innerText = element.value;
}