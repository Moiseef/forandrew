// Articl varios
document.addEventListener('DOMContentLoaded' , ()=>{
let myArt = document.querySelectorAll('#textartmy');
function changeClass(){
 myArt.filter((item, index) => {
    if (`${index}` >= 1) {
        myArt.classList.add('order-md-2');      
    }
 })  
}
changeClass();
})
//myArt.forEach(e => e.classList.add('order-md-2'));
//myArt[1].classList.add('order-md-2');