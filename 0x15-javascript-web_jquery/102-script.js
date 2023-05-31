$(function () {
  $('input#btn_translate').click(() => {
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/',
      data: {
        lang: $('input#language_code').val()
      },
      crossDomain: true,
      success: function (data) {
        $('div#hello').text(data.hello);
      }
    });
  });
});
