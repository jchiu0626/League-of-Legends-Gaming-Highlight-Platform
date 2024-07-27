$(document).ready(function(){
    $("#discussion").on("click", "p", function(event){
        var clickedParagraph = $(this);
        clickedParagraph.css("color", "red");
        clickedParagraph.css("font-size", "200%");
        setTimeout(function(){
            clickedParagraph.css("color", "");
            clickedParagraph.css("font-size", "100%");
        }, 2000);
    });
    $('#search').on('submit', function(e) {
        e.preventDefault();
        var search = $(this).find('input[name="search"]').val();
        if(search === "Pentakill") {
            $(this).find('input[name="search"]').val('')
            window.location.href = 'search_results.html';
        } else {
            $(this).find('input[name="search"]').val('')
            window.location.href = 'search_not_found.html';
        }
    });
    $('#submit-comment').click(function(e) {
        var comment = $('#comment-text').val();
        var storyId = $(this).data('story-id');
        if(comment) {
            $.ajax({
                url: $('#comment-form').attr('action'),
                type: 'POST',
                data: {
                    'comment': comment,
                    'story_id': storyId,
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                dataType: 'json',
                success: function(data) {
                    $('#discussion > p').append('<br>' + data.comment);
                    $('#comment-text').val('');
                },
            });
        }
    });
});

function confirmDelete() {
    return confirm("Are you sure you want to delete this outplay?");
}
