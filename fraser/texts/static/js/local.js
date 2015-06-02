function slug(Text)
{
    return Text
        .toLowerCase()
        .replace(/ /g,'-')
        .replace(/[^\w-]+/g,'')
        ;
}
$(document).ready(function(){
    $('.ngram-hover').hover(function(){
      $('.'+slug(this.innerHTML)).addClass('active');
      }, function(){
      $('.'+slug(this.innerHTML)).removeClass('active');
    });
});
