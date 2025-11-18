from django.db import models

class ContactMessage(models.Model):
    name = models.CharField("الاسم", max_length=100)
    email = models.EmailField("البريد الإلكتروني")
    phone = models.CharField("رقم الجوال", max_length=20)
    subject = models.CharField("الموضوع", max_length=200)
    message = models.TextField("التفاصيل", blank=True)
    attachment = models.FileField("المرفقات", upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField("تاريخ الإرسال", auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.subject}"
