$(document).ready(function() {
  $('[id^=detail-]').hide();

    $('.list-group-item').each(function(e){
      console.log('.list-group-item')
       $input = $(this)
       $target = $input.find('input')
      if(!$target) {
        $target = $input.find('select')
      }
      console.log($target.val())
      if($target.val()) {
        $target = $input.find('.panel-item')
        $target.show()
        $target.attr('display','block')
      }
    })

    $('.toggle').click(function() {
        $input = $( this );
        $target = $('#'+$input.attr('data-toggle'));
        $target.slideToggle();
    });
});
