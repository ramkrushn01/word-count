
async function focusNavTitle(){
    let  pageEndPoint = await document.URL.split("/")[3];
    let aList = await document.getElementsByTagName('a');

    for (let i = 0; i < aList.length; i++) {
        let element = aList[i];
        if(pageEndPoint === ""){
            document.getElementById("home").classList.add("active");
            break;
        }else if(pageEndPoint == element.innerText.toLowerCase().replace(" ","")){
            element.classList.add('active');
            break;
        }else if(pageEndPoint == "contact"){
            contact.classList.add('active');
        }
    }
}

focusNavTitle();

// for delete notification 
function deleteNoti(ee){
    ee.parentElement.style.display = "none";
}

var timeIn = setInterval(() => {
    try{
        notiMessage.style.display = "none";
    }catch(ee){
        console.log(ee);
    }
    clearInterval(timeIn);
}, 4000);