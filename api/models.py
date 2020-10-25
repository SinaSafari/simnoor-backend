from django.db import models


class News(models.Model):
    en_title = models.CharField(max_length=255)
    fa_title = models.CharField(max_length=255)
    en_body_text = models.TextField()
    fa_body_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.en_title


class Product(models.Model):
    en_title = models.CharField(max_length=255)
    fa_title = models.CharField(max_length=255)
    en_description = models.TextField()
    fa_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.en_title


class Contact(models.Model):
    sender_name = models.CharField(max_length=255)
    sender_email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_responsed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
