function right_click(event) {
    event.preventDefault();
    const data = event.target.id;
    const split = data.split("_");
    const source = split[0];
    const card_id = split[1];

    console.log(source, card_id);
    
    let deck_id;
    if (source === "card-list") {
        if (extra_deck_types.includes(card_values[card_id]['type'])) deck_id = "extra";
        else deck_id = "main";
    } else deck_id = "card-list";
    
    const dropzone = document.getElementById(deck_id);
    const elem = document.getElementById(data);
    add_card(source, card_id, elem, dropzone);
    remove_card(source, card_id, elem);
}