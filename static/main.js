moreButtonInnerHTML = "More"

const MAX_LEN = 17




function MakeTile(titleName, rating, genres, imageURL, desciption = "")
{
    function ShortText(text)
    {
        if (text.length > MAX_LEN)
        {
            text = text.slice(0, MAX_LEN) + "..."
        } 

        return text
    }

    let layout = "<div class=\"border\"><div class=\"tile\"><div class=\"user_comment_data\">" + desciption  +"</div><div class=\"photo-and-description\"><div class=\"m_image\" style = \" background-image: url(\'" + imageURL + "\');\"></div><div class=\"short-description\"><h1>" + ShortText(titleName) + "</h1><p>Rating:" +  "☆".repeat(rating) + "</p><p>Genres: " + ShortText(genres) + "</p></div>    </div><div class=\"user_comment_inactive\"></div><div class=\"m_more_button_inactive\"></div></div></div>"

    return layout
}

// load user's watched titles
$.ajax({
    type: "POST",
    url: "/getTitles",
    data: {mode: "watched"},
    dataType: "json",
    success: function (response) {
        response.forEach(title => 
        $(".watched").append(MakeTile(title["titleName"], title["rating"], title["tags"], title["img"], title["description"]))
        )
    }
});

// load user's unwatched titles
$.ajax({
    type: "POST",
    url: "/getTitles",
    data: {mode: "unwatched"},
    dataType: "json",
    success: function (response) {
        response.forEach(title => 
        $(".unwatched").append(MakeTile(title["titleName"], title["rating"], title["tags"], title["img"]))
        )
        $(".unwatched")
    }
});






$(".add-tile-button").click(function () {
    // if add anime window is on screen than this part runs
    if ($(".big_black_squire_active").hasClass("big_black_squire_active"))
    {
        $(".big_black_squire_active").addClass("big_black_squire")
        $(".big_black_squire_active").removeClass("big_black_squire_active")
        $(".add_title_window").css("top", "100%")
        $(".add_title_window").css("display", "none")
    } 
    else
    {
        $(".big_black_squire").addClass("big_black_squire_active")      
        $(".big_black_squire").removeClass("big_black_squire")
        $(".add_title_window").css("display", "flex")
        $(".add_title_window").css("top", "25%")

    }
    // show add anime window
});

// $(".m_main_content").on("mouseover", ".border",
$(".m_main_content").on("click", ".m_more_button_inactive", function() { 
    if ($(this).html() == "Close")
    {
        $(this).parent().children(".user_comment").html("")
        $(".user_comment").html("")
        $(this).parent().children(".user_comment").css("height", "0px").css("padding", "0px")
        $(this).parent().children(".user_comment_inactive").removeClass(".user_comment")
        $(this).html("More")
        moreButtonInnerHTML = "More"
        return 1
    }
    $(this).parent().children(".user_comment_inactive").addClass("user_comment")
    $(this).parent().children(".user_comment").css("height", "calc(389px*0.6)").css("padding", "15px")
    let userComment = $(this).parent().children(".user_comment_data").html()
    $(this).parent().children(".user_comment").html(userComment)
    $(this).html("Close")
    moreButtonInnerHTML = "Close"
    
});

$(".m_main_content").on("mouseover", ".border", function(){
    $(this).css("padding", "2px")
    $(this).children(".tile").children(".m_more_button_inactive").addClass(".m_more_button")
    if (typeof  $(this).children(".tile").children(".m_more_button").html() === "undefined")
    {
        $(this).children(".tile").children(".m_more_button_inactive").html(moreButtonInnerHTML)
        $(this).children(".tile").children(".m_more_button_inactive").css("height", "40px")
    }
})

$(".m_main_content").on("mouseleave", ".border", function(){
    $(this).css("padding", "0px")
    $(this).children(".tile").children(".m_more_button_inactive").removeClass(".m_more_button").html("").css("height", "0px")
})

// function to load images 

$(".anime-list-text-field").keyup(function(){
    titleName = $(".anime-list-text-field").val()
    $.ajax(`/getAnimeList?titleName=${titleName}`,
        {        
            success: function (listOfAnime) {
                $("datalist").html("")
                titles = $.parseJSON(listOfAnime)
                for (title in titles)
                {
                    option = `<option value=\"${titles[title]}\">${titles[title]}</option>`
                    $("datalist").append(option)
                }
            }
        }
    )
})

// hide description field if user clicked on unseen radio button
$("input[value=unwatched").click(function () { 
    $("input[name=description").removeClass("m_btn")
    $("input[name=description").removeClass("show")
    $("input[name=description").addClass("hide")
    $("input[name=description").addClass("m_btn")
});

// show description field if user clicked on watched radio button
$("input[value=watched]").click(function () { 
    $("input[name=description").removeClass("m_btn")
    $("input[name=description").removeClass("hide")
    $("input[name=description").addClass("show")
    $("input[name=description").addClass("m_btn")
});

