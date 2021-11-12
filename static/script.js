window.onload = () =>{
    console.log($(".error").html())
    if ($(".error").html().includes("<p>No errors</p>"))
    {
        console.log("hide")
        $(".error").css("display", "none")
    }
    else{
        $(".error").css("display", "visible")
    }
}



function AnimeList(){
    titleName = $(".anime-list-text-field").val()
    $.ajax(`/getAnimeList?titleName=${titleName}`,
        {        
            success: function (listOfAnime) {
                $("datalist").html("")
                titles = $.parseJSON(listOfAnime)
                for (title in titles)
                {
                    // <option value="Hunter X Hunter">Hunter X Hunter</option>
                    option = `<option value=\"${titles[title]}\">${titles[title]}</option>`
                    // adding option string into data list
                    $("datalist").append(option)
                    console.log(titles[title])
                }
            }
        }
    );
}

setInterval(AnimeList, 1000)