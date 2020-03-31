// django.jQuery(document).ready(function() {
//   console.log("ready!");
//   django.jQuery("#id_name").change(function() {
//     alert("Handler for #id_name was called.");
//   });
// });

window.onload = function() {
  document.getElementById("searchbar").placeholder = "Enter name";

  document
    .getElementById("searchbar")
    .addEventListener("input", function(event) {
      var x = event.inputType;
      console.log(x);
    });
};
