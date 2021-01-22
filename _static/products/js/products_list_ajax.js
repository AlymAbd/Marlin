function get_ajax(group_id, price_from, price_to){
    $.ajax({
        url : '/products/products_list_ajax/',
        dataType : 'JSON',
        type : 'GET',
        data : {
            id_group : group_id,
            from_price : price_from,
            to_price : price_to
        },
        success :
        function(data){
            console.log(data);
            alert(data);
        }
    });
}

function test_ajax(){
    let group_id = 2;
    let price_from = 3;
    let price_to = 6;
    get_ajax(group_id, price_from, price_to);
}

