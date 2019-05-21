from django.db import models
from django.utils import timezone


class Document(models.Model):
    """Class for document fields"""

    file = models.FileField(upload_to='documents/')
    time = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now, blank=True)
    end_date = models.DateTimeField()

    @property
    def get_time_end(self):
        """Calculate the expiration date of the file"""

        if self.create_date:
            end = self.create_date + timezone.timedelta(seconds=self.time)
            return end

    def save(self, *args, **kwargs):
        """Custom save method"""

        self.end_date = self.get_time_end
        super(Document, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Custom delete method"""

        self.file.delete()
        super().delete(*args, **kwargs)
