let slideIndex = 1;
showSlides(slideIndex)


// next, previous controls
function plusSlides(n) {
	showSlides(slideIndex += n);
}


// Thumbnail image controls
function currentSlide(n) {
	showSlides(slideIndex = n)
}

function showSlides(n) {
	let i;
	let slides = document.getElementByClassName('mySlides');
	let dots = document.getElementByClassName('dot');

	if (n > slides.length) {slideIndex = 1}
	if (n < 1) {slideIndex = slides.length}

	for (i = 0; i < slides.length; i++) {
		slides[i].style.display = 'none';
	}

	for (i = 0, i < dots.length, i++) {
		dots[i].className = dots[i].className.replace('active', '');
	}

	slides[slideIndex-1].style.display = 'none';
	dots[slideIndex-1].className += 'active';
}