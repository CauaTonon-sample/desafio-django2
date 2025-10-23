import requests
from django.core.management.base import BaseCommand
from posts.models import Post

API_URL = "https://jsonplaceholder.typicode.com/posts"

class Command(BaseCommand):
    help = "Busca e armazena posts da API JSONPlaceholder"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Iniciando a busca de posts na API..."))

        try:
            # 1. Faz a requisição HTTP (o "pedido")
            response = requests.get(API_URL)
            
            # Se o pedido falhar (ex: erro 404, 500), ele vai gerar um erro aqui
            response.raise_for_status() 

            # 2. Converte a resposta em JSON
            posts_data = response.json()

            # 3. Processa e armazena os dados
            count_created = 0
            for post_data in posts_data:
                # Usamos get_or_create para evitar duplicatas.
                # Ele tenta buscar um Post com o external_id.
                # Se encontrar, não faz nada.
                # Se NÃO encontrar, ele cria um novo.
                _, created = Post.objects.get_or_create(
                    external_id=post_data['id'],
                    defaults={
                        'user_id': post_data['userId'],
                        'title': post_data['title'],
                        'body': post_data['body'],
                    }
                )
                if created:
                    count_created += 1

            # 4. Feedback final
            self.stdout.write(self.style.SUCCESS(
                f"Processo concluído! {count_created} novos posts foram criados."
            ))
            if count_created == 0:
                self.stdout.write(self.style.SUCCESS("Nenhum post novo encontrado."))

        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Erro ao buscar dados da API: {e}"))