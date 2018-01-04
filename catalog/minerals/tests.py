from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Mineral


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Abelsonite",
            category="Organic")

    def test_index_view(self):
        resp = self.client.get(reverse('minerals:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.mineral.category)
        self.assertContains(resp, "Organic")
