async function focusNavTitle() {
    let pageEndPoint = await document.URL.split("/")[3];
    let aList = await document.getElementsByTagName("a");

    for (let i = 0; i < aList.length; i++) {
        let element = aList[i];
        if (pageEndPoint === "") {
            document.getElementById("home").classList.add("active");
            break;
        } else if (
            pageEndPoint == element.innerText.toLowerCase().replace(" ", "")
        ) {
            element.classList.add("active");
            break;
        } else if (pageEndPoint == "contact") {
            contact.classList.add("active");
        }
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
