// Use the jQuery API to select the <ul> element with id "list_movies"
var listMoviesUl = $('#list_movies');

// Make an AJAX request to fetch the movie data from the URL
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function(response) {
    // Extract the movie results from the response
    var movies = response.results;

    // Iterate over each movie and add its title to the list
    movies.forEach(function(movie) {
      // Create a new <li> element with the movie title
      var listItem = $('<li>').text(movie.title);

      // Append the <li> element to the <ul> element
      listMoviesUl.append(listItem);
    });
  },
  error: function() {
    // Handle any errors that occur during the AJAX request
    listMoviesUl.append('<li>Error fetching movie data</li>');
  }
});
