from .models import Categories

def categories_processor(request):
  categories = Categories.objects.all()
  return {"available_categories": categories}