/**
 * Created by Sevenn on 02/08/14.
 */

$(document).ready(function()
{
    setupRotator();
});
function setupRotator()
{
    if($('.quotes').length > 1)
    {
        $('.quotes').fadeOut(0);
        $('.quotes:first').addClass('current').fadeIn(0);
        setInterval('textRotate()', 5000);
    }
}
function textRotate()
{
    var current = $('.blockquotes > .current');
    if(current.next().length == 0)
    {
        current.removeClass('current').fadeOut(1500);
        $('.quotes:first').addClass('current').fadeIn(1500);
    }
    else
    {
        current.removeClass('current').fadeOut(1500);
        current.next().addClass('current').fadeIn(1500);
    }
}
