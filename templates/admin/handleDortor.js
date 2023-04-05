

const rows = document.querySelectorAll('.row-doctor');

console.log(rows)

rows.forEach(row => {
    row.addEventListener('click', () => {
        // Truy xuất thông tin về dòng được nhấp vào
        alert("halo");
    });
});

// function bindingData(this) {
//     alert("he")
// }