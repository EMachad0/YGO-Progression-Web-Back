const deck = {"main": [], "extra": [], "side": []};
const extra_deck_types = ["Fusion Monster"];


function add_card(source, card_id, card, zone) {
    let deck_id = zone.id;
    if (deck_id === "card_list" || source === deck_id) return;
    if (zone.childElementCount >= (deck_id === "main" ? 60 : 15)) return;

    if (deck_id === "extra") {
        if (!extra_deck_types.includes(card_values[card_id]['type'])) return;
    } else if (deck_id === "main" || deck_id === "side"){
        if (extra_deck_types.includes(card_values[card_id]['type'])) return;
    }
    
    let inDeck = get_amount_in_deck(source, card_id, deck_id);
    let limit = 3;
    if (ban_list.hasOwnProperty(card_values[card_id]['name'])) limit = ban_list[card_values[card_id]['name']];
    if (card_values[card_id]['quantity'] === inDeck || inDeck === limit) return;
    
    const newDiv = document.createElement('div');
    newDiv.classList.add("col-card", "m-0", "p-1");
    newDiv.id = card_id;
    const cln = card.cloneNode(true);
    cln.id = deck_id + "_" + card_id;
    newDiv.appendChild(cln);

    zone.appendChild(newDiv);
    deck[deck_id].push(card_id);
    frontend_sort("level", "des", zone);
}

function remove_card(source, card_id, card) {
    if (source === "card-list") return;
    deck[source].splice(deck[source].indexOf(card_id), 1);
    card.parentElement.remove();
}


function get_amount_in_deck(source, card_id, deck_id) {
    let inDeck = 0;
    if (deck_id === "extra") inDeck += deck['extra'].filter(x => x === card_id).length;
    else if (deck_id === "side" || deck_id === "main") {
        inDeck += deck['side'].filter(x => x === card_id).length;
        inDeck += deck['main'].filter(x => x === card_id).length;
    }
    if (source !== "card-list") inDeck--;
    return inDeck;
}

function get_deck_text() {
    let text = "";
    Object.entries(deck).forEach(([key, cards]) => {
        text += (key === "side"? '!':'#') + key + '\n';
        cards.forEach(c => text += c + '\n');
        text += '\n';
    });
    console.log(text);
    return text
}