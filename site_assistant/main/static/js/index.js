// var slideIndex = 1;
var modal;
var logoutLink;
var mybutton;
window.onload = function() {
// showSlides(slideIndex);

modal = document.getElementById('id01');
//Get the button:
mybutton = document.getElementById("myBtn");
logoutLink = document.getElementById("login");
  logoutLink.addEventListener("click", function(event) {
    modal.style.display = "block";
    event.preventDefault();

  });

  var scrollHeight = Math.max(
    document.body.scrollHeight, document.documentElement.scrollHeight,
    document.body.offsetHeight, document.documentElement.offsetHeight,
    document.body.clientHeight, document.documentElement.clientHeight
  );
  
  $("#root").css({height:scrollHeight})

  const params = {
    amount: 500,
    size: {
      min: 1,
      max: 5,
      giant: 9
    },
    duration: {
      min: 3,
      max: 20,
    }
  }
  const randomBetween = (a, b) => {
    return (a + (Math.random() * (b - a)));
  }
  
  for (let i = 0; i < params.amount; i++) {
    let star = $("<div></div>");
    let size = Math.round(Math.random() * 10) === 0 ? params.size.giant : randomBetween(params.size.min, params.size.max);
    star.css({
      "width": size + "px",
      "height": size + "px",
      "left": randomBetween(0, 100) + "%",
      "top": randomBetween(0, 100) + "%",
      "box-shadow": "0 0 " + size + "px " + size / 2 + "px #fcffdf",
      "animation-duration": randomBetween(params.duration.min, params.duration.max) + "s"
    });
  
    $("#root").append(star);
  }
}
// Next/previous controls
// function plusSlides(n) {
//   showSlides(slideIndex += n);
// }

// // Thumbnail image controls
// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

// function showSlides(n) {
//   var i;
//   var slides = document.getElementsByClassName("mySlides");
//   var dots = document.getElementsByClassName("dot");
//   if (n > slides.length) {slideIndex = 1}
//   if (n < 1) {slideIndex = slides.length}
//   for (i = 0; i < slides.length; i++) {
//       slides[i].style.display = "none";
//   }
//   for (i = 0; i < dots.length; i++) {
//       dots[i].className = dots[i].className.replace(" active", "");
//   }
//   slides[slideIndex-1].style.display = "block";
//   dots[slideIndex-1].className += " active";
// }



// Get the modal


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}



// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


