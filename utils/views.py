from django.core.paginator import Paginator, InvalidPage, EmptyPage

def paginate(request, queryset, per_page=25):
    paginator = Paginator(queryset, per_page)

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        results = paginator.page(page)
    except (EmptyPage, InvalidPage):
        results = paginator.page(paginator.num_pages)

    return results
