function openNav() {
	document.getElelmentById("mySidebar").style.width = "250px";
	document.getElementById("content").style.marginLeft = "250px";
}

function closeNav() {
	document.getElelmentById("mySidebar").style.width = "0";
	document.getElementById("content").style.marginLeft = "0";
}