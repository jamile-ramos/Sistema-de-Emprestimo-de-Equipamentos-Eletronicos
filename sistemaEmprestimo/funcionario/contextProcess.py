from django.contrib.auth.models import Group

def user_group_context(request):
    user = request.user
    isAdmin = user.groups.filter(name='Admin').exists()
    isFuncionario = user.groups.filter(name='Funcionarios').exists()
    return {
        'isAdmin': isAdmin,
        'isDuncionario': isFuncionario,
    }