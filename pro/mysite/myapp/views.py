from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import Itemform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
from django.shortcuts import get_object_or_404
from django.utils import timezone

#################################################
##              CLASS-BASED VIEWS              ##
#################################################

## START OF INDEX VIEW
class IndexClassView(ListView):
    model               = Item
    template_name       = 'myapp/index.html'
    context_object_name = 'item_list'
## END OF INDEX VIEW

logger = logging.getLogger(__name__)
#@cache_page(60 * 15)
@vary_on_headers('User-Agent')
def index(request):
    logger.info("fetching all items from database")
    logger.info(f"User [{timezone.now().isoformat()}]{request.user} requested item list from {request.META.get('REMOTE_ADDR')}")
    item_list = Item.objects.all().order_by('id')
    logger.debug(f"Found {item_list.count()} items in the database")
    paginator = Paginator(item_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'myapp/index.html', context)

## START OF DETAIL VIEW

def detail(request,id):
    logger.info(f"fetching item {id} from database")
    try:
        item = get_object_or_404(Item, pk=id)
        logger.debug(f"Found item {item.item_name} (${item.item_price})")
    except Exception as e:
        logger.error(f"Error fetching item %s: %s", id, str(e))
        raise
    
    return render(request, 'myapp/detail.html', {'item': item} )
# class FoodDetail(DetailView):  
#     model               = Item
#     template_name       = 'myapp/detail.html'
#     context_object_name = 'item'
## END OF DETAIL VIEW

## START OF CREATE VIEW
def create_item(request):
    if request.method == 'POST':
        form = Itemform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    else:
        form = Itemform()
    return render(request, 'myapp/item_form.html', {'form': form})
# class CreateItem(LoginRequiredMixin, CreateView):
#     model               = Item
#     fields              = ['item_name', 'item_description', 'item_price', 'item_image']

#     def form_valid(self, form):
#         form.instance.user_name = self.request.user
#         return super().form_valid(form)
## END OF CREATE VIEW

## START OF UPDATE VIEW
class UpdateItem(UpdateView):
    model                   = Item
    fields                  = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name_suffix    = "_update_form"
    
    def get_queryset(self):
        return Item.objects.filter(user_name=self.request.user)
## END OF UPDATE VIEW

## START OF DELETE VIEW
# class DeleteItem(DeleteView):
#     model               = Item
#     success_url         = reverse_lazy('myapp:index')
## END OF DELETE VIEW

#################################################
##              FUNCTION-BASED VIEWS           ##
#################################################
## WITHOUT OPTIMIZATION
def get_objects(request):
    for item in Item.objects.all():
        print(item.item_name)

## WITH OPTIMIZATION
def get_objects_optimized(request):
    items = Item.objects.only('item_name')
    for item in items:
        print(item.item_name)

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('myapp:index')

    return render(request, 'myapp/item_confirm_delete.html')