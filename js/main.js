//Everything here is for testing purposes. There will need to be ways to call from db and also save card position to db. As well as ways to edit cards

$(document).ready(function () {
  //generates the notecards on page load - this will likely call from a db in the future
  for (let index = 1; index < 4; index++) {
    $('#slot3').append("<div class='notecard' value = "+index+" id=card"+index+
    " draggable='true' ondragstart='dragCardStart(event)'onClick='checkSlot(event)'>test card "+index+"</div>");
  }
});

function allowCardDrop(ev) {
  ev.preventDefault(); // default is not to allow drop
}

//When you start dragging a card this function activates with the event of dragStart. It grabs the targets id of the card being dragged
function dragCardStart(ev) {
  ev.dataTransfer.setData("text/plain", ev.target.id);
}


function dropCard(ev) {
  ev.preventDefault(); // default is not to allow drop
  let cardId = ev.dataTransfer.getData("text/plain");
  let sourceCardSlot = document.getElementById(cardId);


  // ev.target.id here is the id of target Object of the drop
  let targetElement = document.getElementById(ev.target.id)
  let targetParentElement = targetElement.parentElement;
  
  //Checks to see if there is an card in the slot. If there is, it will replace it with the new one.
    if (targetElement.className === sourceCardSlot.className) {
      //Removes the current card and replaces it with the new one
      targetParentElement.removeChild(targetElement);
      targetParentElement.appendChild(sourceCardSlot);
    } else {
      // Append to the list
      targetElement.appendChild(sourceCardSlot);
    }
}
