from django.views.generic import TemplateView

from map.models import Trash
from map.tsp import tsp


class PointView(TemplateView):
    template_name = 'map/point.html'

    def post(self, request):
        data = dict(request.POST)
        trash = zip(data.get('lat'), data.get('lng'), data.get('type'), data.get('remark'))
        trash = [Trash(lat=t[0], lng=t[1], type=t[2], remark=t[3]) for t in trash]
        Trash.objects.bulk_create(trash)
        return self.render_to_response({})

class TspView(TemplateView):
    template_name = 'map/tsp.html'

    def post(self, request):
        data = request.POST
        points = [[float(data.get('clat')), float(data.get('clng'))]]
        kwargs = {}
        kwargs.update({'type': ttype} if (ttype := data.get('type')) else {})
        kwargs.update({'crated_at__gte': start} if (start := data.get('start')) else {})
        kwargs.update({'crated_at__lte': end} if (end := data.get('end')) else {})
        trash = Trash.objects.filter(**kwargs).order_by('id').reverse()[:9].values()
        points += map(lambda t: [t.get('lat'), t.get('lng')], trash)
        res = tsp.process(points)
        points = list(map(lambda r: points[r], res))
        remarks = ['現在地'] + list(map(lambda r: trash[r - 1].get('remark'), res[1:-1]))
        return self.render_to_response({'points': points, 'markers': zip(points, remarks)})
