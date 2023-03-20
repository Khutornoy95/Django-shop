from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    image_validator = FileExtensionValidator(
        allowed_extensions=['png', 'jpg', 'gif'],
        message='Расширение не поддерживается. Разрешённые расширения .jpg .gif .png'
    )

    def validate_image_size(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Максимальный размер файла %sMB" % str(megabyte_limit), code='invalid')

    fullName = models.CharField(max_length=200, verbose_name='Полное имя')
    email = models.EmailField(unique=True, verbose_name='Email')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name='Аватар',
                               validators=[validate_image_size, image_validator])
    phoneNumberRegex = RegexValidator(regex=r"^\d{10}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=10, unique=True, verbose_name='Телефон')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
