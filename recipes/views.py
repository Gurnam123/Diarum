"""View for Recipe app go here"""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from . import models
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from .utils import get_random_quote


class RecipeListView(LoginRequiredMixin, ListView):
    """Class-based View for Recipe model (List view)"""
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        # get the currently logged in user
        user = self.request.user
        # return the queryset of recipes for the currently logged in user
        return self.model.objects.filter(author=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quote'] = get_random_quote()
        return context
    
    # def get_queryset(self):
    #     # get the currently logged in user
    #     user = self.request.user

    #     # return the queryset of recipes for the currently logged in user
    #     return self.model.objects.filter(author=user)

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the default context dictionary
    #     context = super().get_context_data(**kwargs)

    #     # Add an additional string context to the context dictionary
    #     context['quote'] = get_random_quote()


def home(request):
    """Function-based view for listing recipes at home page"""
    recipes = models.Recipe.objects.all()
    context = {
    'recipes': recipes
  }
    return render(request, 'recipes/home.html', context)


def about(request):
    """Function based view for about page"""
    return render(request, 'recipes/about.html', {'title': 'about page'})


class RecipeDetailView(DetailView):
    """CLass based view for recipe details page"""
    model = models.Recipe


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """CLass based view for deleting recipe's"""
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


""" class RecipeCreateView(LoginRequiredMixin, CreateView):
 
    model = models.Recipe
    fields = ['title', 'description','image','memories','location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

 """
class RecipeCreateView(LoginRequiredMixin,CreateView):
    model = models.Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """CLass based view for Updating recipe's"""
    model = models.Recipe
    fields = ['title', 'description','image','memories','location']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def search_recipe(request):
    """Function based view for searching recipe's"""
    query = request.GET.get('q','')
    recipes = models.Recipe.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/search.html', context)


def memory(request):
    """Function based view for returnig memories"""
    # Get the current user
    current_user = request.user

    # Filter the Recipe model to include only recipes by the current user and that are marked as private
    recipes = models.Recipe.objects.filter(author=current_user, memories=True)

    # Render the search results page with the filtered recipes
    context = {'recipes': recipes}
    return render(request, 'recipes/memory.html', context)