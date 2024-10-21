from django.core.management.base import BaseCommand
from django.utils import timezone
from ...models import Blog

class Command(BaseCommand):
    help = "Check and publish scheduled blog posts"

    def handle(self, *args, **options):
        now = timezone.now()
        scheduled_posts = Blog.objects.filter(status='draft', published__lte=now)

        for post in scheduled_posts:
            post.status = 'published'
            post.save()
            self.stdout.write(f"Published post: {post.title}")  
            
        self.stdout.write("List of scheduled posts: " + str(scheduled_posts))