from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Post.
    
    Ele 'traduz' os dados do modelo Post para JSON, garantindo que
    apenas os campos definidos em 'fields' sejam expostos na API.
    """
    class Meta:
        model = Post
        # Define quais campos do seu modelo 'Post' devem ser 
        # incluídos na resposta JSON da API.
        fields = ['id', 'user_id', 'external_id', 'title', 'body']