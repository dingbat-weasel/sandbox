const parts = window.location.pathname.split('/').filter(Boolean);
document.querySelector('h1').textContent = parts.at(-2);
