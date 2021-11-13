moreButtonInnerHTML = "More"

$(".m_more_button_inactive").click(function() { 
    if ($(this).html() == "Close")
    {
        $(".user_comment").html("")
        $(".user_comment").css("height", "0px")
        $(".user_comment").css("padding", "0px")
        $(".user_comment_inactive").removeClass(".user_comment")
        $(this).html("More")
        moreButtonInnerHTML = "More"
        return 1
    }
    $(".user_comment_inactive").addClass("user_comment")
    $(".user_comment").css("height", "calc(389px*0.6)").css("padding", "15px")
    $(".user_comment").html("This title is good as hell ")
    $(this).html("Close")
    moreButtonInnerHTML = "Close"
    
});

$(".border").mouseover(function(){
    $(this).css("padding", "2px")
    $(".m_more_button_inactive").addClass(".m_more_button")
    if (typeof $(".m_more_button").html() === "undefined")
    {
        $(".m_more_button_inactive").html(moreButtonInnerHTML)
        $(".m_more_button_inactive").css("height", "40px")
    }
})

$(".border").mouseleave(function(){
    $(this).css("padding", "0px")
    $(".m_more_button_inactive").removeClass(".m_more_button").html("")
    $(".m_more_button_inactive").css("height", "0px")
})