from django.apps import apps
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        dictverbose = {}
        for app in apps.get_app_configs():  # Fix: changed 'app' to 'apps'
            if 'site-packages' not in app.path:
                dictverbose[app.label] = app.verbose_name  # Fix: changed 'verbose_nbame' to 'verbose_name'
        
        context['verbose_dict'] = dictverbose
        return context
