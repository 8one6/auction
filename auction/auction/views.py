from django.views.generic import TemplateView

class HomeView(TemplateView):
    def get_context_data(self, **kwargs):
        context = {}
        return context
    
    template_name = 'home.html'