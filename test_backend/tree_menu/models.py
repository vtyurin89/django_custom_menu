from django.db import models


class TopMenuItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent__isnull=True)


class MenuItem(models.Model):
    """
    Класс характеризует отдельные пункты меню
    """
    title = models.CharField(max_length=100, verbose_name='Название')
    url = models.URLField(max_length=2000, verbose_name='Ссылка')
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.CASCADE, verbose_name='Родительский элемент')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class Menu(models.Model):
    """
    Отдельный объект меню со всеми вложениями
    """
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class TopMenuItem(MenuItem):
    """
    Корневые пункты меню, с которых начинается создание меню
    """
    objects = TopMenuItemManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Верхний пункт меню'
        verbose_name_plural = 'Верхние пункты меню'
