let password = document.getElementById('passw');
let rePassword = document.getElementById('re-passw');
let wPass = document.getElementById('smt-btn');

function checkPassword() {
    if (password.value === rePassword.value && rePassword.value != "") {
        rePassword.style.boxShadow = "0 0 20px green";
        wPass.style.visibility = 'visible';
        smtBtn.disabled = false;

    } else {
        // wPass.innerText = "Incorrect Password";
        wPass.style.visibility = 'hidden';
        rePassword.style.boxShadow = "0 0 20px red";
        smtBtn.disabled = true;
    }

}