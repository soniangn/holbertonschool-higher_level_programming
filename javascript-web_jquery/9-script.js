$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  const hello = data.hello;   
  $('DIV#hello').text(hello);
})