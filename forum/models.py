from django.db import models



# parent model
class forum(models.Model):
    name = models.CharField(max_length=200, default="anonymous")
    email = models.CharField(max_length=200, null=True)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.topic)


# child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE, default=None)
    discuss = models.CharField(max_length=1000, default=None)

    def __str__(self):
        return str(self.forum)