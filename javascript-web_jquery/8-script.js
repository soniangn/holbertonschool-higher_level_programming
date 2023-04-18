$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (result of data.results) {
    const movie = $('<li></li>').text(result.title);
    $('UL#list_movies').append(movie);
  }
});
