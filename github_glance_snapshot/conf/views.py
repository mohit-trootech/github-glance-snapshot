from django.views.generic import DetailView
from utils.constants import Templates
from utils.models import models

User = models.USER


class TestTemplate(DetailView):
    template_name = Templates.BASE_TEMPLATE
    model = User


test_template = TestTemplate.as_view()
