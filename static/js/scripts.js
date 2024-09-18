/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.fade-in');
  
    function handleScroll() {
      const windowHeight = window.innerHeight;
  
      elements.forEach(element => {
        const rect = element.getBoundingClientRect();
        if (rect.top < windowHeight - 100) { // Ajuste o valor conforme necessário
          element.classList.add('visible');
        }
      });
    }
  
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Verifica inicialmente
  });