// Use the jQuery API to select the <div> element with id "character"
var characterDiv = $('#character');

// Make an AJAX request to fetch the character data from the URL
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  success: function(response) {
    // Extract the character name from the response
    var characterName = response.name;

    // Update the text of the <div> element with the character name
    characterDiv.text(characterName);
  },
  error: function() {
    // Handle any errors that occur during the AJAX request
    characterDiv.text('Error fetching character data');
  }
});
