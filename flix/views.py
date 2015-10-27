# Django
from django.views.generic import TemplateView

# Local
from flix.account.models import ViewEvent

class HomepageView(TemplateView):
    template_name = 'homepage.html'

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['view_event'] = ViewEvent.objects.get(pk=1)
        return context
