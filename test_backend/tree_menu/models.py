from django.db import models


class TopMenuItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent__isnull=True)


class NestedMenuItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent__isnull=False)


class MenuItem(models.Model):
    """
    Базовый класс, характеризует отдельные пункты меню
    """
    title = models.CharField(max_length=100, verbose_name='Название')
    url = models.CharField(max_length=2000, verbose_name='Ссылка (URL или тэг Named URL)')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, verbose_name='Меню')
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.CASCADE, verbose_name='Родительский элемент')

    def __str__(self):
        return f'Меню: {self.menu} -- Элемент: {self.title}'

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class Menu(models.Model):
    """
    Отдельный объект меню со всеми вложениями
    """
    title = models.CharField(max_length=150, verbose_name='Название')

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
        return f'{self.menu} -- {self.title}'

    class Meta:
        verbose_name = 'Корневой пункт меню'
        verbose_name_plural = 'Корневые пункты меню'


class NestedMenuItem(MenuItem):
    """
    Вложенные пункты меню, у который обязательно есть родитель
    """
    objects = NestedMenuItemManager()

    def __str__(self):
        return f'{self.menu} -- {self.title}'

    class Meta:
        verbose_name = 'Вложенный пункт меню'
        verbose_name_plural = 'Вложенные пункты меню'
