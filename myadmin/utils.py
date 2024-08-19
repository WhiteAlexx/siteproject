from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from orders.models import Order


def q_search(query):

    if query.isdigit() and len(query) <= 5:
        return Order.objects.filter(id=int(query))

    vector = SearchVector("user", "status")
    query = SearchQuery(query)

    return (
        Order.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
