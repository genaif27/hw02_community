from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# from django import forms  # Импортируем модуль forms, из него возьмём класс ModelForm
# from .models import New_User  # Импортируем модель, чтобы связать с ней форму

User = get_user_model()
# создадим новый класс для формы регистрации
# сделаем его наследником встроеного класса UserCreationForm)

class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем с какой моделью будет рабоать эта форма
        model = User

        # Здесь перечислим поля модели, которые должны отображаться в веб-форме;
        fields = ('first_name', 'last_name', 'username', 'email') 
