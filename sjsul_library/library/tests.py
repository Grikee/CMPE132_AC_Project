from django.test import TestCase
from django.urls import reverse

class DashboardAccessTestCase(TestCase):
    def test_member_dashboard_access(self):
        # Test member dashboard URL
        response = self.client.get(reverse('member_dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_librarian_dashboard_access(self):
        # Test librarian dashboard URL
        response = self.client.get(reverse('librarian_dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard_access(self):
        # Test admin dashboard URL
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)
