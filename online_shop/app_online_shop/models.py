from django.db import models

# Create your models here.

# создаем класс с описанием структуры будущей таблицы

class OnlineShop(models.Model):
    # создаем заголовок
    title = models.CharField('Заголовок', max_length=128)
    # создаем описание объявления
    description = models.TextField('Описание')
    # создаем цену объявления
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    # создаем возможность торговаться
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')
    # создаем дату размещения объявления
    created_time = models.DateTimeField(auto_now_add=True)
    # создаем дату обновления объявления
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "advertisements"
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

# from app_online_shop.models import OnlineShop
# OnlineShop.objects.all()