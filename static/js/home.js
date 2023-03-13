var mainText = document.getElementById("mainText");
var withOutSpace = document.getElementById("withOutSpace");
var totalCharIs = 0;
var changeMainTextImg = false;
var changeMainTextCase = false;

// for getting old text

if (!mainText.value) {
    mainText.value = localStorage.getItem("mainText");
}

async function getRequest(url) {
    let req = await fetch(url);
    let res = await req.json();
    return res;
}

function getWithoutSpace(str) {
    var ans = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            ans += 1;
        }
    }
    return ans;
}

function getParagraph(str){
    if(str == '')return 0;
    
    str = str.split('\n');
    res = 0
    for(let i=0;i<str.length;i++){
        if(str[i] != ''){
            res+=1;
        }
    }

    return res
}



// for title case
function toTitleCase(str) {
    str = str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
    for (let i = 1; i < str.length; i++) {
        if (str[i - 1] === " ") {
            str =
                str.slice(0, i) +
                str.charAt(i).toUpperCase() +
                str.slice(i + 1).toLowerCase();
        }
    }
    return str;
}

// for sentence case
function toSentenceCase(str) {
    str = str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
    for (let i = 1; i < str.length - 2; i++) {
        if (str[i] === " " && str[i - 1] === ".") {
            str =
                str.slice(0, i) +
                str.charAt(i + 1).toUpperCase() +
                str.slice(i + 2).toLowerCase();
        }
    }
    return str;
}

// for clear the main text area
function clearMainText() {
    mainText.value = "";
    typeStart(0);
    localStorage.setItem("mainText", mainText.value);
}

// for coping the main text
function copyToClip() {
    navigator.clipboard.writeText(mainText.value);
    cpText.src = "/static/icon/copy-done.svg";
    changeMainTextImg = true;
}

// for setCase of the mainText
function setCase(ee) {
    let text = mainText.value;
    let currentCase = ee.value;
    changeMainTextCase = true;
    switch (currentCase) {
        case "sc":
            mainText.value = toSentenceCase(text);
            break;

        case "tc":
            mainText.value = toTitleCase(text);
            break;

        case "uc":
            mainText.value = text.toUpperCase();
            break;

        case "lc":
            mainText.value = text.toLowerCase();
            break;
    }
    localStorage.setItem("mainText", mainText.value);
}

// change the word char
function typeStart(event) {
    if (event.keyCode !== 32) {
        totalWord.innerText = mainText.value.replace(/\s+/g,' ').trim().split(" ").length;
    }
    if (mainText.value.length === 0) {
        totalWord.innerText = 0;
    }

    // totalWord.innerText = getTotalWord(mainText.value)
    totalCharIs = mainText.value.length;
    totalChar.innerText = totalCharIs;
    withOutSpace.innerText = getWithoutSpace(mainText.value);
    Panragraph.innerText = getParagraph(mainText.value);

    // for social
    googleId.innerText = 300 - totalCharIs;
    twitterId.innerText = 280 - totalCharIs;
    facebookId.innerText = 250 - totalCharIs;
    if (changeMainTextImg) {
        cpText.src = "/static/icon/copy.svg";
        changeMainTextImg = false;
    }

    if (changeMainTextCase) {
        sCase.value = "Case";
        changeMainTextCase = false;
    }

    localStorage.setItem("mainText", mainText.value);
}

// for download text
async function downloadFile(ee) {
    let res = await getRequest(`/savefile?download-file=true`);
    if (res.success) {
        let a = document.createElement("a");
        document.body.appendChild(a);
        a.style = "display:none";

        let fromBlob = new Blob([mainText.value], { type: "text/plain" });
        let downUrl = window.URL.createObjectURL(fromBlob);
        a.href = downUrl;
        a.download = "wordCount.txt";
        a.click();
        window.URL.revokeObjectURL(downUrl);
    } else {
        showNotiMessage("error", res.reason);
    }
}

// for text file upload
async function uploadFile(ee) {
    let res = await getRequest(`/savefile?upload-file=true`);
    if (res.success) {
        let inp = document.createElement("input");
        inp.type = "file";
        inp.accept = "text/plain";
        inp.style = "display:none";
        inp.onchange = () => {
            file = inp.files[0];
            if (file) {
                let reader = new FileReader();
                reader.readAsText(file, "UTF-8");
                reader.onload = (evt) => {
                    mainText.value = evt.target.result;
                    typeStart(0);
                };
            }
        };
        inp.click();
    } else {
        showNotiMessage("error", res.reason);
    }
}

// for file save

async function saveFile(ee) {
    let req = await fetch("/savefile", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            fileData: mainText.value,
            fileNumber: parseInt(fileNumber.value),
        }),
    });
    let res = await req.json();
    if (res.success) {
        showNotiMessage("success", res.reason + ' File number: ' + res.file_number);
        fileNumber.value = res.file_number;
    } else {
        showNotiMessage("error", res.reason);
    }
}

async function newFile(ee) {
    res = await getRequest(
        `/savefile?new-file=true&&current-file=${parseInt(fileNumber.value)}`
    );
    if (res.success) {
        showNotiMessage("success", res.reason);
        fileNumber.value = res.fileNumber;
    } else {
        showNotiMessage("error", res.reason);
    }
}

typeStart(0);
