from django.contrib import admin
from .models import Vendas, Vendedor, Produto

admin.site.register(Vendas)
admin.site.register(Vendedor)
admin.site.register(Produto)