

window.onload = function() {
  document.getElementById("searchbar").placeholder = "Enter name";

  document
    .getElementById("searchbar")
    .addEventListener("input", function(event) {
      var x = event.returnValue;
      console.log(this.value);
    });
};
