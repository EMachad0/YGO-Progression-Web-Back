update_card_list()

function update_card_list() {
    let url = "/collection/?&guild=" + get_guild() + "&user=" + get_user() + "&limit=30"
    try {
        window.axios.get(url).then(function (response) {
            console.log(response.data);
            
        })
    } catch (error) {
        console.error(error);
    }
}