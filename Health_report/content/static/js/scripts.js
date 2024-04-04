/*!
    * Start Bootstrap - SB Admin v7.0.7 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2023 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

let inputElem = document.querySelectorAll('input');
function showLoading(){
    let check = true;
    inputElem.forEach(element => {
        if (!element.value) {
            check = false;
        }
    });
    
    if (check) {
        document.getElementById('loading').style.display = 'flex';
    }    
}

function showLoading2(){
    let check = false;
    let count = 0;
    inputElem.forEach(element => {
        if (element.checked) {
            check = true;
            count += 1;
        }
    });
    if (count < 2) {
        alert('請選擇一份以上的報告進行分析！')
        event.preventDefault();
        return;
    }
    if (count > 3) {
        alert('最多只能選 3 份報告！')
        event.preventDefault();
        return;
    }  
    if (check) {
        document.getElementById('loading').style.display = 'flex';
    }  
}