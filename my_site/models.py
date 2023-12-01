# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DbArticles(models.Model):
    title = models.CharField(max_length=50)
    full_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'db_articles'


class DbClients(models.Model):
    surnameclient = models.TextField(db_column='surnameClient')  # Field name made lowercase.
    nameclient = models.TextField(db_column='nameClient')  # Field name made lowercase.
    fathernameclient = models.TextField(db_column='fatherNameClient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'db_clients'


class DbDeposites(models.Model):
    depositecode = models.IntegerField(db_column='depositeCode')  # Field name made lowercase.
    mindepositeperiod = models.IntegerField(db_column='minDepositePeriod')  # Field name made lowercase.
    mindepositevalue = models.IntegerField(db_column='minDepositeValue')  # Field name made lowercase.
    currencycode = models.CharField(db_column='currencyCode', max_length=6)  # Field name made lowercase.
    interestrate = models.IntegerField(db_column='interestRate')  # Field name made lowercase.
    depositename = models.CharField(db_column='depositeName', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'db_deposites'


class DbDepositsregistration(models.Model):
    surnameclient = models.TextField(db_column='surnameClient')  # Field name made lowercase.
    nameclient = models.TextField(db_column='nameClient')  # Field name made lowercase.
    fathernameclient = models.TextField(db_column='fatherNameClient')  # Field name made lowercase.
    depositecode = models.IntegerField(db_column='depositeCode')  # Field name made lowercase.
    depositedatestart = models.DateField(db_column='depositeDateStart')  # Field name made lowercase.
    depositedateend = models.DateField(db_column='depositeDateEnd')  # Field name made lowercase.
    depositesum = models.IntegerField(db_column='depositeSum')  # Field name made lowercase.
    depositestatus = models.CharField(db_column='depositeStatus', max_length=20)  # Field name made lowercase.
    surnamepersons = models.TextField(db_column='surnamePersons')  # Field name made lowercase.
    namepersons = models.TextField(db_column='namePersons')  # Field name made lowercase.
    fathernamepersons = models.TextField(db_column='fatherNamePersons')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'db_depositsregistration'


class DbExchangerates(models.Model):
    ratesname = models.CharField(db_column='ratesName', max_length=40)  # Field name made lowercase.
    exchangerate = models.FloatField(db_column='exchangeRate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'db_exchangerates'


class DbPersons(models.Model):
    surnamepersons = models.TextField(db_column='surnamePersons')  # Field name made lowercase.
    namepersons = models.TextField(db_column='namePersons')  # Field name made lowercase.
    fathernamepersons = models.TextField(db_column='fatherNamePersons')  # Field name made lowercase.
    jobtitlepersons = models.TextField(db_column='jobTitlePersons')  # Field name made lowercase.
    salarypersons = models.PositiveBigIntegerField(db_column='salaryPersons')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'db_persons'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
