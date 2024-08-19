from orders.models import Order

class AdminMixin:

    def get_order(self, order_id=None):
        # if request.user.is_authenticated:
        #     query_kwargs = {'user': request.user}
        # else:
        #     query_kwargs = {'session_key': request.session.session_key}

        # if order_id:
        #     query_kwargs['id'] = order_id

        return Order.objects.filter(id=order_id)
