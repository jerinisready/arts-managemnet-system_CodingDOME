from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from event.models import Registration

User = get_user_model()


@method_decorator(login_required, 'dispatch')
class ScoreboardListView(ListView):
    model = User
    template_name = 'event/scoreboard.html'

    def get_queryset(self):
        return User.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        cxt = super(ScoreboardListView, self).get_context_data(object_list=object_list, **kwargs)
        cxt['scoreboard'] = {}
        for regn in Registration.objects.all().filter(point__gt=0):
            if regn.user not in cxt['scoreboard'].keys():
                cxt['scoreboard'][regn.user] = regn.point
            else:
                cxt['scoreboard'][regn.user] = cxt['scoreboard'][regn.user] + regn.point
        cxt['scoreboard'] = list( cxt['scoreboard'].items() )
        cxt['scoreboard'].sort(key=lambda item: item[1], reverse=True)
        return cxt

