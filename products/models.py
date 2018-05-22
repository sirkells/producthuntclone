from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    # image field to be uploaded by user for the products section
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body_text = models.TextField()  # summary of the job
    url = models.TextField()
    no_of_votes = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  # func that displays the title as header in admin page
        return self.title

    def summary(self):  # function to summarise the body_text so it displays olnly the first 100 chr
        return self.body_text[:100]

    def date_format(self):  # fumction to format the date to only date without time
        return self.date.strftime('%b %e %Y')
