
function card_list_sort() {
    const sort_param = document.getElementById('sort-param');
    const key = sort_param.options[sort_param.selectedIndex].text;
    const sort_order = document.getElementById('sort-order');
    const ord = sort_order.options[sort_order.selectedIndex].text;
    const list = document.getElementById('card-list');
    if (key === "any") return;
    do_sort(key, ord, list);
}


function card_list_filter() {
    const list = document.getElementById('card-list');
    do_filter(list);
}

function deck_download() {
    download("YGO-Prog-deck.ydk", get_deck_text());
}

function display_update(id) {
    const display = document.getElementById('display');
    id = id.split("_")[1];
    display.src = "https://storage.googleapis.com/ygoprodeck.com/pics/" + id + ".jpg";
}