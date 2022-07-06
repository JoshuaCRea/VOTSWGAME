var townIds = ["#townA", "#townB", "#townD", "#townC"];
var currentTownIndex = 0;

$(".move-button").click(function () {
    if (currentTownIndex == 4) {
        currentTownIndex = 0
    }
    var currentTownId = townIds[currentTownIndex];
    currentTownIndex++;
    $(".town").css('background-color', '#ffffff');
    $(currentTownId).css('background-color', '#f8cf95');
})