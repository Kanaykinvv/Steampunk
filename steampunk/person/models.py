from django.db import models

# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length=50, default='NoName', verbose_name='Имя персонажа')
    cash = models.FloatField(default=0.0, verbose_name='Количество денежных средств')
    experience = models.IntegerField(default=0, verbose_name='Количество текущего опыта')
    level = models.IntegerField(default=1, verbose_name='Текущий уровень')
    dice_min = models.IntegerField(default=1, verbose_name='Текущий кубик (min)')
    dice_max = models.IntegerField(default=4, verbose_name='Текущий кубик (max)')
    bounty = models.IntegerField(default=0, verbose_name='Текущие очки развития')

    strength_bonus = models.IntegerField(default=0, verbose_name='Сила (бонус)')
    strength_add = models.IntegerField(default=0, verbose_name='Сила (улучшение)')

    agility_bonus = models.IntegerField(default=0, verbose_name='Ловкость (бонус)')
    agility_add = models.IntegerField(default=0, verbose_name='Ловкость (улучшение)')

    intellect_bonus = models.IntegerField(default=0, verbose_name='Интеллект (бонус)')
    intellect_add = models.IntegerField(default=0, verbose_name='Интеллект (улучшение)')

    initiative_bonus = models.IntegerField(default=0, verbose_name='Инициатива (бонус)')
    initiative_add = models.IntegerField(default=0, verbose_name='Инициатива (улучшение)')

    health_current = models.IntegerField(default=0, verbose_name='Здоровье (текущее)')
    health_bonus = models.IntegerField(default=0, verbose_name='Здоровье (бонус)')
    health_add = models.IntegerField(default=0, verbose_name='Здоровье (улучшение)')

    energy_current = models.IntegerField(default=0, verbose_name='Энергия (текущее)')
    energy_bonus = models.IntegerField(default=0, verbose_name='Энергия (бонус)')
    energy_add = models.IntegerField(default=0, verbose_name='Энергия (улучшение)')

    persistence_bonus = models.IntegerField(default=0, verbose_name='Стойкость (бонус)')
    persistence_add = models.IntegerField(default=0, verbose_name='Стойкость (улучшение)')

    reaction_bonus = models.IntegerField(default=0, verbose_name='Реакция (бонус)')
    reaction_add = models.IntegerField(default=0, verbose_name='Реакция (улучшение)')

    consciousness_bonus = models.IntegerField(default=0, verbose_name='Сознание (бонус)')
    consciousness_add = models.IntegerField(default=0, verbose_name='Сознание (улучшение)')

    burden_current = models.IntegerField(default=0, verbose_name='Ноша (текущая)')
    burden_bonus = models.IntegerField(default=0, verbose_name='Ноша (бонус)')
    burden_add = models.IntegerField(default=0, verbose_name='Ноша (улучшение)')

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'

