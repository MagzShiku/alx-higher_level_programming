// Use the jQuery API to select the <div> element with id "update_header"
var updateHeaderDiv = $('#update_header');

// Add a click event listener to the update_header div
updateHeaderDiv.on('click', function() {
  // Use the jQuery API to select the <header> element
  var headerElement = $('header');

  // Update the text of the <header> element
  headerElement.text('New Header!!!');
});
