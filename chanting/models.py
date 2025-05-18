from django.db import models

class praying(models.Model): # praying table
    title = models.CharField(max_length=50) # ชื่อบทสวด
    content = models.CharField(max_length=2000) # เนื้อบทสวด

class prayingset(models.Model):
    title = models.CharField(max_length=50) # ชื่อบทสวด
    set = models.ManyToManyField(praying)
