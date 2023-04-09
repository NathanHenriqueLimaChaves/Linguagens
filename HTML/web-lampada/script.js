let btn_liga = document.querySelector('#on-off');
let lampada = document.querySelector('#lamp');

btn_liga.addEventListener('click',function(){
    // console.log("oiiii")
    if(lampada.src.match("lampada-on")){
        lampada.src="lampada-off.gif";
    }else{
        lampada.src="lampada-on.gif";
    }
});
