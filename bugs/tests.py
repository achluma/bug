from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Bug
from .views import home, register_bug, bug_list

# Create your tests here.
class BugModelTestCase(TestCase):
    def setUp(self):
        # Create a sample Bug instance
        self.bug = Bug.objects.create(
            description="Test Bug",
            bug_type="ERROR",
            report_date=timezone.now(),
            status="TO_DO"
        )
        self.bug2 = Bug.objects.create(
            description="Test Bug 2",
            bug_type="Feature Request",
            report_date=timezone.now(),
            status="IN_PROGRESS"
        )
        

    def test_bug_creation(self):
        self.assertEqual(self.bug.description, "Test Bug")
        self.assertEqual(self.bug.bug_type, "ERROR")
        self.assertTrue(self.bug.report_date)
        self.assertEqual(self.bug.status, "TO_DO")

    def test_bug_str_method(self):
        self.assertEqual(str(self.bug), "Test Bug")

    def test_bug_default_status(self):
        new_bug = Bug.objects.create(
            description="Another Bug",
            bug_type="Feature Request",
            report_date=timezone.now()
        )
        self.assertEqual(new_bug.status, "TO_DO")
        
    def test_bug_type_choices(self):
        bug_types = [choice[0] for choice in Bug._meta.get_field('bug_type').choices]
        self.assertIn("Error", bug_types)
        self.assertIn("Feature Request", bug_types)
        self.assertIn("Enhancement", bug_types)

    def test_bug_status_choices(self):
        status_choices = [choice[0] for choice in Bug._meta.get_field('status').choices]
        self.assertIn("TO_DO", status_choices)
        self.assertIn("IN_PROGRESS", status_choices)
        self.assertIn("DONE", status_choices)
        
    def test_bug_report_date_future(self):
        future_date = timezone.now() + timezone.timedelta(days=1)
        future_bug = Bug.objects.create(
            description="Future Bug",
            bug_type="ERROR",
            report_date=future_date,
            status="TO_DO"
        )
        self.assertGreater(future_bug.report_date, timezone.now())

    def test_bug_report_date_past(self):
        past_date = timezone.now() - timezone.timedelta(days=7)
        past_bug = Bug.objects.create(
            description="Past Bug",
            bug_type="ERROR",
            report_date=past_date,
            status="TO_DO"
        )
        self.assertLess(past_bug.report_date, timezone.now())
        
class BugViewTestCase(TestCase):
    def setUp(self):
        # Create a sample Bug instance for testing
        self.bug = Bug.objects.create(
            description="Test Bug",
            bug_type="ERROR",
            report_date=timezone.now(),
            status="TO_DO"
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to My Bug Tracking App")

    def test_register_bug_view(self):
        response = self.client.get(reverse('register_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register a Bug")

    def test_bug_list_view(self):
        response = self.client.get(reverse('bug_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Recent Bugs")
        self.assertQuerysetEqual(response.context['bugs'], [repr(self.bug)])