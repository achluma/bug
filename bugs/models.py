from django.db import models

# Create your models here.
class Bug(models.Model):
    # Field for textual description of the bug
    description = models.TextField()

    # Field for the type of the bug (e.g., error, new feature, etc.)
    bug_type = models.CharField(
        max_length=100,
        choices=[
            ('ERROR', 'Error'),
            ('NEW_FEATURE', 'New Feature'),
            ('OTHER', 'Other'),
        ],
        )

    # Field for the date in which the bug is being registered
    report_date = models.DateField()

    # Field for the status of resolution of the bug
    status = models.CharField(
        max_length=50,
        choices=[
            ('TO_DO', 'To Do'),
            ('IN_PROGRESS', 'In Progress'),
            ('DONE', 'Done'),
        ],
        default='TO_DO'  # Default status is set to 'To Do'
    )

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-report_date']  # Order bugs by report date in descending order
