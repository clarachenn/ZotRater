//javascript for ratings.html
const urlParams = new URLSearchParams(window.location.search);
var data = urlParams.get('data');
//const container = document.getElementById('ratingContainer');

function displayClassItems() {
    const container = document.getElementById('info');
    const values = data.split(',');

    // Construct the desired array format
    const transformedArray = [
        parseFloat(values[0]), // First value as a number
        values[1], // Second value as a string
        [values[2] + ", " + values[3], values[4] + ", " + values[5]], // Third and fourth values as an array
        [parseFloat(values[6]), parseFloat(values[7])], // Fifth and sixth values as an array
        [parseFloat(values[8]), parseFloat(values[9])], // Seventh and eighth values as an array
        [parseFloat(values[10]), parseFloat(values[11])], // Ninth and tenth values as an array
        [parseFloat(values[12]), parseFloat(values[13])], // Eleventh and twelfth values as an array
        [parseFloat(values[14]), parseFloat(values[15])], // Thirteenth and fourteenth values as an array
        values.slice(16, 20), // Fifteenth to eighteenth values as an array
        values.slice(20) // Remaining values as an array
      ];

    // Log the transformed array
    console.log(transformedArray);
    data = transformedArray;
    console.log(data.length);
    //container.innerHTML = '';
    for (let i = 0; i < data.length; i++) {
        if (i === 0) {
          const rating = data[i];
          
          const ratingElement = document.createElement('p');
          ratingElement.textContent = `Overall Rating: ${rating}`;
          console.log(ratingElement.textContent);
          container.appendChild(ratingElement);
        } else if (i === 1) {
          const response = data[i];
          const responseElement = document.createElement('p');
          responseElement.textContent = `Response: ${response}`;
          container.appendChild(responseElement);
        } else if (i === 2) {
          const profNames = data[i];
          const profNamesElement = document.createElement('div');
          profNamesElement.classList.add('side-by-side');
          
          for (let j = 0; j < profNames.length; j++) {
            const profNameElement = document.createElement('p');
            profNameElement.textContent = `Professor Name: ${profNames[j]}`;
            profNamesElement.appendChild(profNameElement);
          }
          
          container.appendChild(profNamesElement);
        } else if (i === 8 || i === 9) {
            console.log(data[i]);
            const profWords = data[i];
            const profWordsElement = document.createElement('div');
            profWordsElement.classList.add('side-by-side');
            console.log(getRatingLabel.length);
            profWordsElement.textContent = `${getRatingLabel(8)}: ${JSON.stringify(data[i])}`;
            container.appendChild(profWordsElement);
        }
        
        else {
            console.log(i);
            console.log(data[i]);
          const ratings = data[i];
          const ratingsElement = document.createElement('div');
          ratingsElement.classList.add('side-by-side');
          
          for (let j = 0; j < ratings.length; j++) {
            const ratingElement = document.createElement('p');
            ratingElement.textContent = `${getRatingLabel(i)}: ${ratings[j]}`;
            ratingsElement.appendChild(ratingElement);
          }
          
          container.appendChild(ratingsElement);
        }
      }
      
      function getRatingLabel(index) {
        const ratingLabels = ['Course Ratings', 'Course GPA', 'Pass Rate', 'Professor Rating', 'Professor Difficulty','Professor Keywords'];
        return ratingLabels[index - 3   ];
      }
      
    }

document.addEventListener('DOMContentLoaded', function () {
    displayClassItems();
});