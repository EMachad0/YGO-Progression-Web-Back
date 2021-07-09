function deck_download() {
    download("YGO-Prog-deck.ydk", get_deck_text());
}

function display_update(id) {
    const display = document.getElementById('display');
    id = id.split("_")[1];
    display.src = "https://storage.googleapis.com/ygoprodeck.com/pics/" + id + ".jpg";
}