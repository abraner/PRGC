from django.db import models

class MemberInfo(models.Model):
    memberid = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    firstname = models.CharField(max_length=45, verbose_name="First Name:")
    lastname = models.CharField(max_length=45, verbose_name="Last Name:")
    handicap = models.IntegerField(null=True, default=None, blank=True, verbose_name="Handicap")
    username = models.CharField(max_length=45, verbose_name="User Name:")
    password = models.CharField(max_length=45, blank=True, verbose_name="Password")
    securitylevel = models.IntegerField(null=True, default=None, blank=True, verbose_name="Security Level")

