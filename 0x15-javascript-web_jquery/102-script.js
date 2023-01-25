<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function() {
  $('#btn_translate'.click(function() {
    var language_code = $('#language_code').val();
    var api_url = 'https://www.fourtonfish.com/hellosalut/hello/';
    $.get(api_url + language_code, function(data) {
      $("#hello").html(data.hello);
      });
    });
});
</script>
