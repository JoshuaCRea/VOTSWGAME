var townIds = ["#townA", "#townB", "#townD", "#townC"];
var currentTownIndex = 0;
var currentTownId = townIds[currentTownIndex];
$(currentTownId).css('background-color', '#f8cf95');


$("#moveCcwButton").click(function () {
    console.log(`current town index is: ${currentTownIndex}`);
    currentTownIndex--;
    if (currentTownIndex == -1) {
        currentTownIndex = 3
    }
    var currentTownId = townIds[currentTownIndex];
    console.log(`current town index is: ${currentTownIndex}`);
    $(".town").css('background-color', '#ffffff');
    $(currentTownId).css('background-color', '#f8cf95');
})

$("#moveCwButton").click(function () {
    console.log("I just clicked the move CW button");
    currentTownIndex++;
    console.log(`current town index is: ${currentTownIndex}`);
    if (currentTownIndex == 4) {
        currentTownIndex = 0
    }
    var currentTownId = townIds[currentTownIndex];
    console.log(`current town index is: ${currentTownIndex}`);
    $(".town").css('background-color', '#ffffff');
    $(currentTownId).css('background-color', '#f8cf95');
})