$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
})});

$(document).ready(function () {
  $('DIV#remove_item').click(function () {
    $('.my_list li').last().remove();
})});

$(document).ready(function () {
  $('DIV#clear_list').click(function () {
    $('.my_list li').remove();
})});
