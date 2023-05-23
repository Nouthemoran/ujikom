from django.db import models

# Create your models here.
class MyModel(models.Model):
    kdjual = models.CharField(primary_key=True, max_length=4)
    kdbrg = models.CharField(max_length=4)
    nmbrg = models.CharField(max_length=100)
    tgltrans = models.DateTimeField(auto_now_add=False)
    jumbrg = models.IntegerField()
    hargabrg = models.FloatField()
    totalbyr = models.FloatField()
    
    def save(self, *args, **kwargs):
        if not self.kdjual:
            last_kdjual = MyModel.objects.order_by('-kdjual').first()
            if last_kdjual:
                last_kdjual_number = int(last_kdjual.kdjual[1:])
                new_kdjual_number = last_kdjual_number + 1
                self.kdjual = 'J' + str(new_kdjual_number).zfill(3)
            else:
                self.kdjual = 'J001'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nmbrg
