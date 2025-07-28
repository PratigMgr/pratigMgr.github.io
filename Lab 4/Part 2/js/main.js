const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */
const images = ["pic1.jpg", "pic2.jpg", "pic3.jpg", "pic4.jpg", "pic5.jpg"];

/* Declaring the alternative text for each image file */
const alts = {
    "pic1.jpg": "A picture of a baby's eye",
    "pic2.jpg": "A random unique picture of rock",
    "pic3.jpg": "A picture of jasmine flower",
    "pic4.jpg": "A picture of Egyptian Sculpture",
    "pic5.jpg": "A picture of a beautiful butterfly.",

    
};

/* Looping through images */
for(let i = 0 ; i < images.length; i++) {
    // Create a new <img> element for each thumbnail
    const newImage = document.createElement('img');
    // Set the image source (path to the image file)
    newImage.setAttribute('src', "./images/" + images[i]);
   // Set the alt text (for accessibility) from the `alts` object
    newImage.setAttribute('alt', alts[images[i]]);
    // Append the thumbnail to the thumbBar container
    thumbBar.appendChild(newImage);
    // Add click event to update the main displayed image when thumbnail is clicked
    newImage.addEventListener('click', function(f){
        displayedImage.setAttribute('src', this.src);
        displayedImage.setAttribute('alt', this.alt);
});
}
/* Wiring up the Darken/Lighten button */
    // If button says "Darken", switch to light mode
btn.addEventListener('click', function(){
    if(btn.textContent == "Darken"){
    btn.setAttribute('class','light');
    btn.textContent = 'Lighten';
    overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
  } else {
        // Otherwise, switch back to dark mode
    btn.setAttribute('class','dark');
    btn.textContent = 'Darken';
    overlay.style.backgroundColor = 'rgba(0,0,0,0)';
    }
})
