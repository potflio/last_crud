from django.db import models
class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    
    class Meta:  
        db_table = "student"
# try:
#     import pymysql
#     pymysql.install_as_MySQLdb()
# except:
#     pass
