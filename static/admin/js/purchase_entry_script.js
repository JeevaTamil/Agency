window.onload = function() {
  console.log("ready");
  setTotalId();

  // var temp_list = document.getElementById("suppliers-data").textContent;

  var temp_supplier = document.getElementById("suppliers-data").textContent;
  var json_supplier = JSON.parse(temp_supplier);

  this.console.log(json_supplier);
  var suppliers = JSON.parse(json_supplier);

  var bill_no = document.getElementById("id_bill_no");
  var disc_value = document.getElementById("id_d_value");
  var disc_percent = document.getElementById("id_d_percent");
  var good_value = document.getElementById("id_goods_val");
  var supplier_name = this.document.getElementById("id_supplier");
  var supplier__name = this.document.getElementById(
    "select2-id_supplier-container"
  );

  var config = { attributes: true, childList: true };

  function toggle_hide(elem) {
    console.log("console output " + elem.style.visibility);
    if (elem.style.display != "block") {
      console.log("it is hidden");
      elem.style.display = "block";
    } else {
      elem.style.display = "none";
    }
  }

  function display_all() {
    var i_gst = document.getElementsByClassName("fieldBox field-i_gst");
    var s_gst = document.getElementsByClassName("fieldBox field-s_gst");
    var c_gst = document.getElementsByClassName("fieldBox field-c_gst");
    for (j = 0; j < s_gst.length; j++) {
      s_gst[j].style.display = "block";
      c_gst[j].style.display = "block";
      i_gst[j].style.display = "block";
    }
  }

  var callback = function(mutationsList) {
    for (var mutation of mutationsList) {
      if (mutation.type == "childList") {
        var selected_supplier = supplier__name.innerHTML;
        var i_gst = document.getElementsByClassName("fieldBox field-i_gst");
        var s_gst = document.getElementsByClassName("fieldBox field-s_gst");
        var c_gst = document.getElementsByClassName("fieldBox field-c_gst");
        for (i = 0; i < suppliers.length; i++) {
          if (suppliers[i].fields.name == selected_supplier) {
            display_all();
            document.getElementById("supplier_city").innerHTML =
              suppliers[i].fields.city;

            if (suppliers[i].fields.state != 1) {
              console.log("i value -> " + i);
              for (j = 0; j < s_gst.length; j++) {
                toggle_hide(s_gst[j]);
              }
              for (j = 0; j < c_gst.length; j++) {
                toggle_hide(c_gst[j]);
              }
            } else {
              for (j = 0; j < i_gst.length; j++) {
                toggle_hide(i_gst[j]);
              }
            }
          }
        }
      }
      break;
    }
  };

  var observer = new MutationObserver(callback);

  observer.observe(supplier__name, config);

  supplier_name.addEventListener("load", function() {
    var name = supplier_name.innerHTML;
  });

  bill_no.addEventListener("input", function(event) {
    var x = event.returnValue;
  });

  good_value.addEventListener("input", function(event) {
    setTotal();
  });

  disc_value.addEventListener("input", function() {
    if (event.value != "") {
      setTotal();
    }
  });

  disc_percent.addEventListener("input", function() {
    if (event.value != "") {
      setTotal();
    }
  });

  function setTotalId() {
    var readonly_fields = document.getElementsByClassName("readonly");
    for (i = 0; i < readonly_fields.length; i++) {
      if (readonly_fields[i].innerHTML == "0") {
        readonly_fields[i].setAttribute("id", "total_val");
      } else if (readonly_fields[i].innerHTML == "-") {
        readonly_fields[i].setAttribute("id", "supplier_city");
      } else if (readonly_fields[i].innerHTML == "GST") {
        readonly_fields[i].setAttribute("id", "tax_type");
      } else if (readonly_fields[i].innerHTML == "c_tax") {
        readonly_fields[i].setAttribute("id", "c_tax");
      } else if (readonly_fields[i].innerHTML == "s_tax") {
        readonly_fields[i].setAttribute("id", "s_tax");
      } else if (readonly_fields[i].innerHTML == "i_tax") {
        readonly_fields[i].setAttribute("id", "i_tax");
      }
    }
  }

  function setTotal() {
    var total = document.getElementById("total_val");
    console.log("set total");
    var val = discounted_val() + tax_value();
    total.innerHTML = parseInt(val);
  }

  function discounted_val() {
    var disc_value = document.getElementById("id_d_value");
    var disc_percent = document.getElementById("id_d_percent");
    var good_value = document.getElementById("id_goods_val");

    return calculate_price(
      good_value.value,
      disc_percent.value,
      disc_value.value
    );
  }

  function tax_value() {
    var val = discounted_val();

    tax = (val * 5) / 100;
    console.log("tax - " + tax);
    document.getElementById("i_tax").innerHTML = tax;
    document.getElementById("c_tax").innerHTML = tax / 2;
    document.getElementById("s_tax").innerHTML = tax / 2;

    // for (i = 0; i < suppliers.length; i++) {
    //   console.log("supplier state" + suppliers[i].fields.state);
    //   if (suppliers[i].fields.state != 1) {
    //     document.getElementById("i_tax").innerHTML = tax;
    //   } else {
    //     document.getElementById("c_tax").innerHTML = tax / 2;
    //     document.getElementById("s_tax").innerHTML = tax / 2;
    //   }
    // }
    // document.getElementById("tax_value").innerHTML = tax;

    return tax;
  }

  function calculate_price(good_value, discount_percent, discount_value) {
    if (discount_value != "") {
      return parseInt(good_value) - parseInt(discount_value);
    }

    if (discount_percent != "") {
      return (
        parseInt(good_value) -
        (parseInt(good_value) * parseInt(discount_percent)) / 100
      );
    }

    return parseInt(good_value);
  }
};
