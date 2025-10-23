from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Este ViewSet fornece automaticamente as ações 'list' (listar) 
    e 'retrieve' (detalhar) para os Posts.
    
    Como estamos usando ReadOnlyModelViewSet, a API será 
    "somente leitura" (não permitirá criar ou deletar por enquanto).
    """
    
    # 1. A consulta: Pega todos os objetos Post do banco de dados.
    queryset = Post.objects.all().order_by('id')
    
    # 2. O tradutor: Diz ao DRF para usar o PostSerializer.
    serializer_class = PostSerializer
    
    # 3. Diz que qualquer um pode acessar esta API (ler).
    permission_classes = [permissions.AllowAny]
