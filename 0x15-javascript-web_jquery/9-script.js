// Use the jQuery API to select the <div> element with id "hello"
var helloDiv = $('#hello');

// Make an AJAX request to fetch the translation from the URL
$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  method: 'GET',
  success: function(response) {
    // Extract the translation from the response
    var translation = response.hello;

    // Update the text of the <div> element with the translation
    helloDiv.text(translation);
  },
  error: function() {
    // Handle any errors that occur during the AJAX request
    helloDiv.text('Error fetching translation');
  }
});
