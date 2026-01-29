from joins.models import Join

class ReferMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ref_id = request.GET.get('ref')
        try:
            obj = Join.objects.get(ref_id=ref_id)
        except Join.DoesNotExist:
            obj = None
        if obj:
            request.session['join_id_ref'] = obj.id

        response = self.get_response(request)

        return response
