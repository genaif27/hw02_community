from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится

class SignUp(CreateView):  # Создаём свой класс, наследуем его от CreateView
    # C какой формой будет работать этот view-класс
    form_class = CreationForm    

    # Какой шаблон применить для отображения веб-формы
    template_name = 'users/signup.html'  

    # Куда переадресовать пользователя после того, как он отправит форму
    success_url = reverse_lazy('posts:index')