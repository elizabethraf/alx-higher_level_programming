<script src='https://code.jquery.com/jquery-3.6.0.min.js'></script>
<script>
$(document).ready(() => {
  $('#btn_translate').click(() => {
    let language_code = $('#language_code').val();
    const api_url = 'https://www.fourtonfish.com/hellosalut/hello/';
    $.get(`${api_url}${language_code}`, (data) => {
      $('#hello').html(data.hello);
      });
    });
});
</script>
