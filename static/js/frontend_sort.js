function frontend_sort(key, ord, list) {
    let toSort = list.children;
    toSort = Array.prototype.slice.call(toSort, 0);

    toSort.sort(function (a, b) {
        let va = card_values[a.id][key];
        let vb = card_values[b.id][key];
        if (va === vb) return (card_values[a.id]['name'] <= card_values[b.id]['name'] ? -1 : 1);
        if (va == null) return 1;
        if (vb == null) return -1;
        return (ord === "asc" ? 1 : -1) * (va <= vb ? -1 : 1);
    });

    list.innerHTML = "";
    for (let i = 0, l = toSort.length; i < l; i++) {
        list.appendChild(toSort[i]);
    }
}

function frontend_card_list_sort() {
    const sort_param = document.getElementById('sort-param');
    const key = sort_param.options[sort_param.selectedIndex].text;
    const sort_order = document.getElementById('sort-order');
    const ord = sort_order.options[sort_order.selectedIndex].text;
    const list = document.getElementById('card-list');
    if (key === "any") return;
    frontend_sort(key, ord, list);
}