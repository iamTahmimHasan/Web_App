$(document).ready(function(){

	// Maritial Status
	$("#sel1").click(function(){
		var boardingpoint = $("#sel1").val()
		 // 	var e = document.getElementById("sel1");
			// var strUser = e.options[e.selectedIndex].text;
			if (boardingpoint == "Married") {
				$("#disabled1").removeAttr('disabled');
				$("#disabled2").removeAttr('disabled');
			}else{
				$("#disabled1").attr('disabled', true);
				$("#disabled2").attr('disabled', true);

			}
		});
	// Input Field required
	var submit_button = document.getElementById("submit_button");
	submit_button.addEventListener("click", function(e) {
		var required = document.querySelectorAll("input[required]");

		required.forEach(function(element) {
			if(element.value.trim() == "") {
				element.style.borderColor  = "red";
				Swal.fire({
					icon: "info"
				})
			} else {
				element.style.borderColor  = "white";
			}
		});
	});

	// Select Field required
// 	var submit_button = document.getElementById("submit_button");

// 	submit_button.addEventListener("click", function(e) {
// 		var required = document.querySelector('#inputState').required = true;

// 		required.forEach(function(element) {
// 			if(element.value.trim() == "") {
// 				element.style.borderColor  = "red";
// 			} else {
// 				element.style.borderColor  = "white";
// 			}
// 		});
// 	});

	

	
// 	function yesnoCheck(that) {
// 		if (that.value == "Add") {
//  // alert("check");
//  document.getElementById("ifYes").style.display = "block";
// } else {
// 	document.getElementById("ifYes").style.display = "none";
// }
// }


});