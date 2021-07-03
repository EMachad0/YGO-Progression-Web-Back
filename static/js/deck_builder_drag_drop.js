const drop_zones = ["main", "extra", "side", "card-list"]

function onDragOver(event) {
    event.preventDefault();

}
function onDragStart(event) {
    event.dataTransfer.setData('text/plain', event.target.id);
    console.log("dragging " + event.target.id)

}

function onDrop(event) {
    const data = event.dataTransfer.getData('text');
    const split = data.split("_");
    const source = split[0];
    const id = split[1];
    
    let dropzone = event.target;
    let deck_id = dropzone.id;
    while (!drop_zones.includes(deck_id)) {
        dropzone = dropzone.parentNode;
        deck_id = dropzone.id;
    }
    
    console.log(data, deck_id)
    
    if (!drop_zones.includes(deck_id)) return;
    
    if (!card_values.hasOwnProperty(id)) return;
    if (source === deck_id) return;
    if (deck_id !== "card-list" && dropzone.childElementCount > (deck_id === "main" ? 60 : 15)) return;

    if (deck_id === "extra") {
        if (!extra_deck_types.includes(card_values[id]['type'])) return;
    } else if (deck_id === "main" || deck_id === "side"){
        if (extra_deck_types.includes(card_values[id]['type'])) return;
    }
    
    let inDeck = 0;
    if (deck_id === "extra") inDeck += deck['extra'].filter(x => x === id).length;
    else if (deck_id === "side" || deck_id === "main") {
        inDeck += deck['side'].filter(x => x === id).length;
        inDeck += deck['main'].filter(x => x === id).length;
    }
    if (source !== "card-list") inDeck--;
    if (card_values[id]['quantity'] <= inDeck) return;

    const elem = document.getElementById(data);

    if (deck_id !== "card-list") {
        const newDiv = document.createElement('div');
        newDiv.classList.add("col-card", "m-0", "p-1");
        const cln = elem.cloneNode(true);
        cln.id = deck_id + "_" + id;
        newDiv.appendChild(cln);
    
        dropzone.appendChild(newDiv);
        deck[deck_id].push(id);
    }
    
    if (source !== "card-list") {
        deck[source].splice(deck[source].indexOf(id), 1);
        elem.parentElement.remove();
    }

    event.dataTransfer.clearData();
}