from django.views.generic import TemplateView

from news.models import News


class HomePageView(TemplateView):
    template_name = "mainpage/mainpage.html"

    def get_context_data(self, **kwargs):
        news = News.objects.prefetch_related("images").all()\
            .order_by("date_published")
        return {"news": news}
