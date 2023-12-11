// Use the jQuery API to select the <div> element with id "red_header"
var redHeaderDiv = $('#red_header');

// Add a click event listener to the red_header div
redHeaderDiv.on('click', function() {
  // Use the jQuery API to select the <header> element
  var headerElement = $('header');

  // Add the class "red" to the <header> element
  headerElement.addClass('red');
});
