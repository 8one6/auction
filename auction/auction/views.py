from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
from auction.forms import WhoAmIForm

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        if not self.request.session.get('has_session'):
            self.request.session['has_sesion'] = True
            self.request.session.save()
        context = {}
        return context
    


class WhoAmIView(FormView):
    form_class = WhoAmIForm
    template_name = 'whoami.html'
    
    def get_success_url(self):
        return reverse('auction_home')
    
    def form_valid(self, form):
        self.request.session['name'] = form.cleaned_data['name']
        self.request.session.save()
        return super(FormView, self).form_valid(form)    