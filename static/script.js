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



