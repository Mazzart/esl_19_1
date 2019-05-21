from django.core.management.base import BaseCommand
from django.utils import timezone

from uploader.models import Document


class Command(BaseCommand):
    """Custom command class to clean database"""

    help = "Deletes documents for which lifetime has expired"

    def handle(self, *args, **options):
        """Clear the database of expired files"""

        now = timezone.now()
        Document.objects.filter(end_date__lt=now).delete()
