$(function () {
  function getHello () {
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
  }
  $('input#btn_translate').click(() => {
    getHello();
  });
  $('input#language_code').keypress((e) => {
    if (e.which === 13) {
      getHello();
    }
  });
});
