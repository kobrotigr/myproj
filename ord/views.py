from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OrdItem
from django.views.generic import CreateView
from .forms import OrdForm
from django.urls import reverse
from basket.models import BasketItem
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from django.template.loader import render_to_string

# Create your views here.


class OrdCreate(LoginRequiredMixin, CreateView):
    model = OrdItem
    template_name = "ord/ord_list.html"
    form_class = OrdForm

    def get_success_url(self):
        return reverse('shop_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save(True)
        basket_list = BasketItem.objects.filter(user=self.request.user)
        for item in basket_list:
            form.instance.ord_list.add(item.book)
        form.save(True)
        d = {'ord': form.instance}
        plaintext = get_template('ord/email.txt')
        htmly = get_template('ord/email.html')
        html_content = htmly.render(d)
        text_content = plaintext.render(d)
        msg = EmailMultiAlternatives('Order', text_content, 'shop@gmail.com', ['admin@gmail.com'])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        # send_mail("Order", text_cont, 'shop@gmail.com', ['admin@gmail.com'], fail_silently=False)
        BasketItem.objects.filter(user=self.request.user).delete()

        return super(OrdCreate, self).form_valid(form)
