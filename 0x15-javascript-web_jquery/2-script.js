// Use the jQuery API to select the <div> element with id red_header
var redHeaderDiv = $('#red_header');

// Add a click event listener to the red_header div
redHeaderDiv.on('click', function() {
  // Use the jQuery API to select the <header> element
  var headerElement = $('header');

  // Update the text color of the <header> element to red
  headerElement.css('color', '#FF0000');
});
