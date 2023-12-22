from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operation, Money
from .forms import OperationForm

@login_required
def index(request):
    """
        Функция для страницы с анализом бюджета

        money_user - бюджет пользователя
        operations - операции пользователя
    """

    # Получаем бюджет пользователя
    money_user, _ = Money.objects.get_or_create(user=request.user)

    # Получаем операции пользователя
    operations = Operation.objects.filter(user=request.user).order_by('-date')

    context = {
        'operations': operations,
        'money_user': money_user,
    }

    return render(request, 'finance/index.html', context)

@login_required
def operation_create(request):
    """
        Функция для страницы с созданием операции

        money_user - бюджет пользователя
        form - форма операции
    """

    # Получаем бюджет пользователя
    money_user = Money.objects.get(user=request.user)

    # Обрабатываем форму
    form = OperationForm(request.POST, files=request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            # Добавляем доход или расход к общему бюджету
            money_user.amount += int(post.amount)
            money_user.save()

            form.save()

            return redirect('finance:index')

        return render(request, 'finance/create_operation.html', {'form': form})

    context = {
        'form': form,
    }

    return render(request, 'finance/create_operation.html', context)
