var nome ="Menino da sombra lá ";
var cargo ="Monarca das sombras"
var nomehtml = document.getElementById("nome-no-html");
var cargohtml = document.getElementById("cargo-no-html");
var texto1 = document.getElementById("texto-1");
var texto2 = document.getElementById("texto-2");

function colocarnomenohtml(nome) {
    nomehtml.innerHTML = nome;
 
}
function colocarcargonohtml(cargo) {
    cargohtml.innerHTML=cargo;

    
}

function logarnome(){
    console.log(nome);   
}

function clicknoprojetos(){
    console.log("Clicou em Site Topzeira");
    texto2.style.display = "block";
    texto1.style.display ="none";
}

function clicknosobre() {
    console.log("Clicou no botão sobre");
    texto1.style.display ="block";
    texto2.style.display = "none";
    
}
colocarnomenohtml(nome);
colocarcargonohtml(cargo);  