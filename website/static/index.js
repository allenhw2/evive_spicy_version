function deleteOrder(orderId) {
    fetch('/delete-order', {
        method: "POST",
        body: JSON.stringify({ orderId: orderId })
    }).then((_res) => {
        window.location.href = "/";
    })
}