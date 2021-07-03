function do_sort(key, ord, list) {
    let toSort = list.children;
    toSort = Array.prototype.slice.call(toSort, 0);

    toSort.sort(function (a, b) {
        let va = card_values[a.id][key];
        let vb = card_values[b.id][key];
        if (va == null && vb == null) return -1;
        if (va == null) return 1;
        if (vb == null) return -1;
        return (ord === "asc" ? 1 : -1) * (va <= vb ? -1 : 1);
    });

    list.innerHTML = "";
    for (let i = 0, l = toSort.length; i < l; i++) {
        list.appendChild(toSort[i]);
    }
}