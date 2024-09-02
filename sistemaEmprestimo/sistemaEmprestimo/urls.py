from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionario/', include('funcionario.urls')),
    path('conta/', include('conta.urls')),
    path('conta/', include('django.contrib.auth.urls')),
    path('emprestimo/', include('emprestimo.urls')),
    path('equipamento/', include('equipamento.urls')),
    path('itemEmprestimo/', include('itemEmprestimo.urls'))
]
