var isDoggle = false;

async function focusNavTitle() {
    let pageEndPoint = await document.URL.split("/")[3];
    // pageEndPoint = element.innerText.toLowerCase().replace(" ", "")
    console.log(pageEndPoint)

    switch (pageEndPoint) {
        case '':
            homeId.classList.add("active");
            break;
        case 'membership':
            membershipId.classList.add("active");
            break;
        case 'contact':
            contactId.classList.add("active");
            break;
        case 'about':
            aboutId.classList.add("active");
            break;
        case 'history':
            historyId.classList.add("active");
        case 'login':
            loginId.classList.add("active");
            break;
        case 'signup':
            signupId.classList.add("active");
            break;
        default:
            homeId.classList.add("active");
            break;
    }
}

function showNotiMessage(type, message) {
    clearInterval(timeIn);
    notiMessage.style.display = "flex";
    notiMessage.innerHTML =
        `<div class="notiMessage ${type}">
            <p>${message}</p>
            <img class="icon-10" src="static/icon/delete.svg" alt="delete" onclick="deleteNoti(this)">
        </div>` + notiMessage.innerHTML;

    var timeIn = setInterval(() => {
        try {
            for (let i = 0; i < notiMessage.childNodes.length; i++) {
                notiMessage.removeChild(notiMessage.childNodes[i]);
            }
        } catch (ee) {
            console.log(ee);
        }
        clearInterval(timeIn);
    }, 4000);
}

// showNotiMessage();
focusNavTitle();

// for delete notification
function deleteNoti(ee) {
    ee.parentElement.style.display = "none";
}

var timeIn = setInterval(() => {
    try {
        for (let i = 0; i < notiMessage.childNodes.length; i++) {
            notiMessage.removeChild(notiMessage.childNodes[i]);
        }
    } catch (ee) {
        console.log(ee);
    }
    clearInterval(timeIn);
}, 4000);

function showNavBar(e){
    // if(document.body.offsetWidth > 800){
        // return
    // }
    
    let navbar = document.getElementById("navbar");
    let bar = document.getElementById("bar");
    if (navbar.style.display === "flex") {
        navbar.style.display = "none";
        bar.innerHTML = "&#8801;";
    } else {
        navbar.style.display = "flex";
        bar.innerHTML = "&#10007;";
    }
};