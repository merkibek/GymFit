from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe


class Client(models.Model):
    PASS_TYPES = (
        ('FD', 'Full day'),     # Unlimited
        ('DY', 'Daily'),        # To 17:00
        ('EV', 'Evening')       # From 17:00
    )
    SUB_STATUSES = (
        ('AC', 'Active'),
        ('CN', 'Canceled')
    )
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    card_id = models.CharField(max_length=8, null=True, blank=True, verbose_name='Card ID', unique=True)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=11)
    pass_type = models.CharField(max_length=2, choices=PASS_TYPES)
    sub_months = models.IntegerField(default=1)
    sub_initiated = models.DateField(default=timezone.now)
    sub_terminated = models.DateField(default=timezone.now)
    sub_status = models.CharField(max_length=2, choices=SUB_STATUSES)
    image = models.ImageField(verbose_name='Picture', default='noimage.jpg', upload_to='images')

    def image_tag(self):
        return mark_safe('<img src="/media/{}" width="150" height="150" />'.format(self.image))

    image_tag.short_description = 'Image'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Attendance(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    date_attended = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendance Records'

    def clean(self):
        d = datetime.now()
        if self.client.sub_status == 'CN':
            raise ValidationError('Client\'s subscription has expired!')
        if self.client.pass_type == 'DY' and d.hour >= 16:
            raise ValidationError('Client has "Daily" pass, time out!')
        if self.client.pass_type == 'EV' and d.hour < 17:
            raise ValidationError('Client has "Evening" pass. Time hasn\'t come yet')


class Team(models.Model):
    team_name = models.CharField(max_length=30)
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    client = models.ManyToManyField('Client', verbose_name='Members')
    info = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, verbose_name='Meeting date')

    def __str__(self):
        return self.team_name


class Instructor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=11)
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(verbose_name='Picture', upload_to='images', default='noimage.jpg')

    def image_tag(self):
        return mark_safe('<img src="/media/{}" width="300" height="400" />'.format(self.image))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Applications(models.Model):
    IS_PROCESSED = {
        ('T', 'Processed'),
        ('F', 'Not Processed'),
        ('W', 'Waiting for client')
    }
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default='None')
    phone = models.CharField(max_length=30, default='None')
    message = models.TextField()
    processed = models.CharField(max_length=1, choices=IS_PROCESSED, default='F')

    class Meta:
        verbose_name = 'Applications'
        verbose_name_plural = 'Applications'