function appendToDisplay(value) {
    document.getElementById("display").value += value;
}

function clearDisplay() {
    document.getElementById("display").value = "";
}

function deleteDigit() {
    let currentDisplay = document.getElementById("display").value;
    document.getElementById("display").value = currentDisplay.slice(0, -1);
}

function calculate() {
    try {
        document.getElementById("display").value = eval(document.getElementById("display").value);
    } catch {
        document.getElementById("display").value = "Error";
    }
}