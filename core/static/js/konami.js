jQuery(function(){
    var KonamiKeys = [];
    function Konami(e){
        KonamiKeys.push(e.keyCode);
        if (KonamiKeys.toString().indexOf("38,38,40,40,37,39,37,39,66,65") >= 0) {
            jQuery(this).unbind('keydown', Konami);
            kExec();
        }
    }
    jQuery(document).keydown(Konami);
});
function kExec(){
    document.getElementById('WhenIm').innerHTML = '<section><article class="text-center"><object type="text/html" data="http://www.youtube.com/embed/Awmu0-8aXSQ?autoplay=1" class="konami-video"></object></article></section>';
}
