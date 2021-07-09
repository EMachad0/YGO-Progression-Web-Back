function hide(element) {
    element.classList.add("hide");
}

function show(element) {
    element.classList.remove("hide");
}

function frontend_filter(list) {
    const name = document.getElementById('filter-name')
    
    let toFilter = list.children;
    toFilter = Array.prototype.slice.call(toFilter, 0);
    toFilter.forEach(function (v) {
        let card = card_values[v.id];
        if (name != null && name.value !== "" && !card['name'].toLowerCase().includes(name.value.toLowerCase())) hide(v);
        else show(v);
    });
}

function frontend_card_list_filter() {
    const list = document.getElementById('card-list');
    frontend_filter(list);
}