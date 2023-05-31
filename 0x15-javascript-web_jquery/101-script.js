$(function () {
  $('div#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(() => {
    $('UL.my_list li:last-child').remove();
  });
  $('div#clear_list').click(() => {
    $('UL.my_list > li').remove();
  });
});
