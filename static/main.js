moreButtonInnerHTML = "More"

$(".m_more_button_inactive").click(function() { 
    if ($(this).html() == "Close")
    {
        $(this).parent().children(".user_comment").html("")
        $(".user_comment").html("")
        $(this).parent().children(".user_comment").css("height", "0px")
        $(this).parent().children(".user_comment").css("padding", "0px")
        $(this).parent().children(".user_comment_inactive").removeClass(".user_comment")
        $(this).html("More")
        moreButtonInnerHTML = "More"
        return 1
    }
    $(this).parent().children(".user_comment_inactive").addClass("user_comment")
    $(this).parent().children(".user_comment").css("height", "calc(389px*0.6)").css("padding", "15px")
    $(this).parent().children(".user_comment").html("This title is good as hell ")
    $(this).html("Close")
    moreButtonInnerHTML = "Close"
    
});

$(".border").mouseover(function(){
    $(this).css("padding", "2px")
    $(this).children(".tile").children(".m_more_button_inactive").addClass(".m_more_button")
    if (typeof  $(this).children(".tile").children(".m_more_button").html() === "undefined")
    {
        $(this).children(".tile").children(".m_more_button_inactive").html(moreButtonInnerHTML)
        $(this).children(".tile").children(".m_more_button_inactive").css("height", "40px")
    }
})

$(".border").mouseleave(function(){
    $(this).css("padding", "0px")
    $(this).children(".tile").children(".m_more_button_inactive").removeClass(".m_more_button").html("")
    $(this).children(".tile").children(".m_more_button_inactive").css("height", "0px")
})