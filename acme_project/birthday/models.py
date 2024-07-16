from django.db import models
from django.urls import reverse

from .validators import real_age
from users.models import CustomUser


class Birthday(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=20
    )
    last_name = models.CharField(
        'Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=20
    )
    birthday = models.DateField(
        'Дата рождения',
        validators=(real_age,)
    )
    image = models.ImageField(
        'Фото',
        blank=True,
        upload_to='birthdays_images'
    )
    author = models.ForeignKey(
        CustomUser,
        verbose_name='Автор записи',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = 'день рождения'
        verbose_name_plural = 'Дни рождения'
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Уникальный запрос для пользователя'
            ),
        )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("birthday:detail", kwargs={"pk": self.pk})


class Congratulation(models.Model):
    text = models.TextField(
        'Поздравление'
    )
    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        verbose_name='день рождения',
        related_name='congratulations'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания поздраления'
    )

    class Meta:
        ordering = ('created_at',)
