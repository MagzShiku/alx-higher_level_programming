// Use the jQuery API to select the <div> element with id "toggle_header"
var toggleHeaderDiv = $('#toggle_header');

// Add a click event listener to the toggle_header div
toggleHeaderDiv.on('click', function() {
  // Use the jQuery API to select the <header> element
  var headerElement = $('header');

  // Toggle the class "red" and "green" on the <header> element
  headerElement.toggleClass('red green');
});
