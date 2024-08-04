// Когда html документ готов (прорисован)
$(document).ready(function () {
    // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
    var successMessage = $("#jq-notification");

    // Ловим собыитие клика по кнопке добавить в корзину
    $(document).on("click", ".add-to-cart", function (e) {

        // Блокируем его базовое действие
        e.preventDefault();

        // Берем элемент счетчика в значке корзины и берем оттуда значение
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseFloat(goodsInCartCount.text() || 0);
        var cartCount = parseFloat(goodsInCartCount.text() || 0);

        // Получаем id товара из атрибута data-product-id
        var product_id = $(this).data("product-id");
        var count_mid = parseFloat($(this).data("count-mid"));
        var count_low = parseFloat($(this).data("count-low"));
        var count_res = parseFloat($(this).data("count-res"));
        // Из атрибута href берем ссылку на контроллер django
        var add_to_cart_url = $(this).attr("href");

        if (count_res > 0) {
            $(this).addClass("disabled");
        }

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                count_res: count_res,
                count_res: count_res,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // // Сообщение
                // successMessage.html(data.message);
                // successMessage.fadeIn(400);
                // // Через 7сек убираем сообщение
                // setTimeout(function () {
                //     successMessage.fadeOut(400);
                // }, 7000);

                // Увеличиваем количество товаров в корзине (отрисовка в шаблоне)
                if (count_mid > 0) {
                    cartCount += count_mid;
                } else if (count_low > 0) {
                    cartCount += count_low;
                } else if (count_res > 0) {
                    cartCount += count_res;
                } else if (count_res > 0) {
                    cartCount += count_res;
                } else {
                    cartCount++;}
                // goodsInCartCount.text(cartCount);
                goodsInCartCount.addClass("bg-danger");

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

                $('#exampleModal').appendTo('body');
                $('#exampleModal').modal('show');
            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });

    });


    // Ловим собыитие клика по кнопке удалить товар из корзины
    $(document).on("click", ".remove-from-cart", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Берем элемент счетчика в значке корзины и берем оттуда значение
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseFloat(goodsInCartCount.text() || 0);

        // Получаем id корзины из атрибута data-cart-id
        var cart_id = $(this).data("cart-id");
        // Из атрибута href берем ссылку на контроллер django
        var remove_from_cart = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({

            type: "POST",
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // // Сообщение
                // successMessage.html(data.message);
                // successMessage.fadeIn(400);
                // // Через 7сек убираем сообщение
                // setTimeout(function () {
                //     successMessage.fadeOut(400);
                // }, 7000);

                // Уменьшаем количество товаров в корзине (отрисовка)
                cartCount -= data.quantity;
                // goodsInCartCount.text(cartCount);
                if (data.clss === 0) {
                    goodsInCartCount.removeClass("bg-danger");
                }

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });


    // Теперь + - количества товара 
    // Обработчик события для уменьшения значения
    $(document).on("click", ".decrement", function () {
        // Берем ссылку на контроллер django из атрибута data-cart-change-url
        var url = $(this).data("cart-change-url");
        // Берем id корзины из атрибута data-cart-id
        var cartID = $(this).data("cart-id");
        // Ищем ближайшеий input с количеством 
        var $input = $(this).closest('.input-group').find('.number');
        // Берем значение количества товара
        var currentValue = parseFloat($input.val());
        // Если количества больше одного, то только тогда делаем -1
        if (currentValue > 1) {
            $input.val(currentValue - 1);
            // Запускаем функцию определенную ниже
            // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
            updateCart(cartID, currentValue - 1, -1, url);
        }
    });

    // Обработчик события для увеличения значения
    $(document).on("click", ".increment", function () {
        // Берем ссылку на контроллер django из атрибута data-cart-change-url
        var url = $(this).data("cart-change-url");
        // Берем id корзины из атрибута data-cart-id
        var cartID = $(this).data("cart-id");
        // Ищем ближайшеий input с количеством 
        var $input = $(this).closest('.input-group').find('.number');
        // Берем значение количества товара
        var currentValue = parseFloat($input.val());

        $input.val(currentValue + 1);

        // Запускаем функцию определенную ниже
        // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
        updateCart(cartID, currentValue + 1, 1, url);
    });

    $(document).on("change", ".number", function () {
        var change = parseFloat($(this).val());
        var cartID = $(this).data("cart-id");
        var url = $(this).data("cart-change-url");
        alert("Выбрано " + change + " ед.");
        updateCart(cartID, change, change, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                //  // Сообщение
                // successMessage.html(data.message);
                // successMessage.fadeIn(400);
                //  // Через 7сек убираем сообщение
                // setTimeout(function () {
                //      successMessage.fadeOut(400);
                // }, 7000);

                // Изменяем количество товаров в корзине
                var goodsInCartCount = $("#goods-in-cart-count");
                var cartCount = parseFloat(goodsInCartCount.text() || 0);
                cartCount += change;
                // goodsInCartCount.text(cartCount);

                // Меняем содержимое корзины
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    }

    // Берем из разметки элемент по id - оповещения от django
    var notification = $('#notification');
    // И через 7 сек. убираем
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }

    // При клике по значку корзины открываем всплывающее(модальное) окно
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Собыите клик по кнопке закрыть окна корзины
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Обработчик события радиокнопки выбора способа доставки
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });


    $(document).on("click", ".select_buy", function () {
        // Берем ссылку на контроллер django из атрибута data-cart-select-url
        var url = $(this).data("cart-select-url");
        // Берем id корзины из атрибута data-cart-id
        var cartID = $(this).data("cart-id");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({

            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
                },
            success: function (data) {

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
                
            },
        });
    });

    // При клике по оплате открываем всплывающее(модальное) окно
    // $('#modalButton_1').click(function () {
    $(document).on("click", ".modalButton_1", function () {
        // Берем ссылку на контроллер django из атрибута data-order-payment-url
        var url = $(this).data("order-payment-url");
        // Берем id корзины из атрибута data-order-id
        var orderID = $(this).data("order-id");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({

            type: "POST",
            url: url,
            data: {
                order_id: orderID,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
                },
            success: function (data) {

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var paymentContainer = $("#payment-container");
                paymentContainer.html(data.payment_html);
                
            },
        });

        $('#exampleModal_1').appendTo('body');

        $('#exampleModal_1').modal('show');
    });

    // Собыите клик по кнопке закрыть окна корзины
    $('#exampleModal_1 .btn-close').click(function () {
        $('#exampleModal_1').modal('hide');
    });

});
