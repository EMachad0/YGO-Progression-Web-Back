const drop_zones = ["main", "extra", "side", "card-list"]

function onDragOver(event) {
    event.preventDefault();

}
function onDragStart(event) {
    event.dataTransfer.setData('text/plain', event.target.id);
    console.log("dragging " + event.target.id)
}

function onDrop(event) {
    event.preventDefault();
    const data = event.dataTransfer.getData('text');
    const split = data.split("_");
    const source = split[0];
    const id = split[1];
    
    let dropzone = event.target;
    while (!drop_zones.includes(dropzone.id)) dropzone = dropzone.parentNode;
    if (!drop_zones.includes(dropzone.id)) return;
    
    console.log(data, dropzone.id)
    
    if (!card_values.hasOwnProperty(id)) return;
    
    const elem = document.getElementById(data);
    add_card(source, id, elem, dropzone);
    remove_card(source, id, elem);

    event.dataTransfer.clearData();
}