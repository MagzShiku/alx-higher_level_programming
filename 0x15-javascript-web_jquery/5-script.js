// Use the jQuery API to select the <div> element with id "add_item"
var addItemDiv = $('#add_item');

// Add a click event listener to the add_item div
addItemDiv.on('click', function() {
  // Use the jQuery API to select the <ul> element with class "my_list"
  var myList = $('ul.my_list');

  // Create a new <li> element
  var newItem = $('<li>Item</li>');

  // Append the new <li> element to the <ul> element
  myList.append(newItem);
});
