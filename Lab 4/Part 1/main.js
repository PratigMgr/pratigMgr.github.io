const customName = document.getElementById('customname');
const randomize = document.querySelector('.randomize');
const story = document.querySelector('.story');

// Function to get random item from an array
function randomValueFromArray(array){
  const random = Math.floor(Math.random()*array.length);
  return array[random];
}

// Template story and arrays for replacement values
let storyText = "It was 94 fahrenheit outside, so :insertx: went for a walk. When they got to :inserty:, they stared in horror for a few moments, then :insertz:. Bob saw the whole thing, but was not surprised — :insertx: weighs 300 pounds, and it was a hot day.";
const insertX = ["Willy the Goblin", "Big Daddy", "Father Christmas"];
const insertY = ["the soup kitchen", "Disneyland", "the White House"];
const insertZ = ["spontaneously combusted", "melted into a puddle on the sidewalk", "turned into a slug and crawled away"];

// Add click event listener to randomize button
randomize.addEventListener('click', result);


function result() {

    let newStory = storyText;
      // Get random values for each placeholder
    var xItem = randomValueFromArray(insertX);
    var yItem = randomValueFromArray(insertY);
    var zItem = randomValueFromArray(insertZ);

       // Replace placeholders with random values
    newStory = newStory.replaceAll(":insertx:", xItem);
    newStory = newStory.replaceAll(":inserty:", yItem);
    newStory = newStory.replaceAll(":insertz:", zItem);

  // Replace name if custom name is provided
  if(customName.value !== '') {
    const name = customName.value;
    newStory = newStory.replaceAll(xItem, name);

  }

  // Convert to UK units if UK checkbox is checked
  if(document.getElementById("uk").checked) {
    const weight = Math.round(300/14) + ' stone';
    const temperature =  Math.round( (5/9) * (94 - 32)) + ' centigrade';
    newStory = newStory.replaceAll('94 fahrenheit', temperature);
    newStory = newStory.replaceAll('300 pounds', weight);

  }
  // Display the generated story
  story.textContent = newStory;
  story.style.visibility = 'visible';
}

