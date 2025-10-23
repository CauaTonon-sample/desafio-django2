from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importa a ViewSet 
from posts.views import PostViewSet

# O router é quem cria magicamente as URLs para nós (ex: /posts/ e /posts/1/)
router = DefaultRouter()

# Dizemos: "Ei, roteador, use a PostViewSet para a URL 'posts'"
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Qualquer URL que comece com 'api/'
    # deve ser gerenciada pelo nosso 'router'."
    path('api/', include(router.urls)),
]
