from django.db import models

class PrivacyPolicy(models.Model):
    text = models.TextField(default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.text

    class Meta:
        verbose_name = 'Політика конфіденційності'
        verbose_name_plural = 'Політики конфіденційності'