$(".anime-list-text-field").keyup(function(){
    console.log("keypress function")
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
    )
})