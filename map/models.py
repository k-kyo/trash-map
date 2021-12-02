from django.db import models


class Trash(models.Model):
    lat = models.FloatField(verbose_name="緯度")
    lng = models.FloatField(verbose_name="経度")
    type = models.CharField(verbose_name="種類", max_length=10, blank=True)
    remark = models.CharField(verbose_name="備考", max_length=30, blank=True)
    crated_at = models.DateField(verbose_name="作成日時", auto_now_add=True)
