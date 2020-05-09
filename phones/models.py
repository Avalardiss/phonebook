from django.db import models

class Abonent(models.Model):
    id = models.AutoField('ID', auto_created=True, primary_key=True)
    rank = models.CharField('Воинское звание', max_length=50)
    name = models.CharField('Фамилия, Имя, Отчество', max_length=100)
    phone = models.CharField('Рабочий телефон', max_length=10)
    IP_phone = models.CharField('IP телефон', max_length=10)

    class Meta:
        verbose_name = 'Абонент'
        verbose_name_plural = 'Абоненты'
    def __str__(self):
        return self.id
    def __str__(self):
        return self.rank
    def __str__(self):
        return self.name
    def __str__(self):
        return self.phone
    def __str__(self):
        return self.IP_phone
        
def get_absolute_url(self):
        return reverse("a:detail", kwargs={'a_id': self.a_id})