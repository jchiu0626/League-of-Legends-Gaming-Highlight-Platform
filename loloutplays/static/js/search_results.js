$(document).ready(function(){
    var search = new URLSearchParams(window.location.search).get('search');
    if (search === "Pentakill") {
        $('#content').show();
        $('#search-not-found').hide();
    }
    else {
        $('#content').hide();
        $('#search-not-found').show();
    }
});
