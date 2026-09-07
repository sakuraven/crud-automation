const addProductToTable = (event) => {
    event.preventDefault();

    const code = document.getElementById("code").value;
    const brand = document.getElementById("brand").value;
    const type = document.getElementById("type").value;
    const category = document.getElementById("category").value;
    const unitPrice = document.getElementById("unitPrice").value;
    const cost = document.getElementById("cost").value;
    const extra = document.getElementById("extra").value;

    const table = document.getElementById("productTable");

    const row = table.insertRow(-1);
    row.insertCell(0).innerHTML = code;
    row.insertCell(1).innerHTML = brand;
    row.insertCell(2).innerHTML = type;
    row.insertCell(3).innerHTML = category;
    row.insertCell(4).innerHTML = unitPrice;
    row.insertCell(5).innerHTML = cost;
    row.insertCell(6).innerHTML = extra;

    document.getElementById("code").value = "";
    document.getElementById("brand").value = "";
    document.getElementById("type").value = "";
    document.getElementById("category").value = "";
    document.getElementById("unitPrice").value = "";
    document.getElementById("cost").value = "";
    document.getElementById("extra").value = "";
}

const clearTable = () => {
    const table = document.getElementById("productTable");
    const qtRows = table.rows.length;
    for(let i = qtRows-1; i > 0; i--) {
        table.deleteRow(i);
    }
}
