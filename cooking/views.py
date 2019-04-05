from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
import json

from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_GET, require_POST
from django.views.generic import ListView, \
    TemplateView, \
    DetailView, \
    CreateView, FormView

from cooking.forms import RecipeForm, RegistrationForm
from cooking.models import Recipe, User


# Create your views here.
from social_cooking.settings import PAGE_SIZE


class FeedView(ListView):
    template_name = 'recipe_list.html'
    queryset = Recipe.objects.all()
    paginate_by = PAGE_SIZE
    url_name = 'feed'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['url_feed'] = reverse(self.url_name)
        return context


class UserFeedView(FeedView, LoginRequiredMixin):
    url_name = 'user.feed'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class RecipeView(DetailView):
    template_name = 'recipe.html'
    queryset = Recipe.objects.all()


class CreateRecipeView(CreateView):
    template_name = 'create_recipe.html'
    form_class = RecipeForm
    model = Recipe

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class RegisterView(FormView):
    template_name = 'registration/signup.html'
    form_class = RegistrationForm
    model = User
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        form.save()
        user = authenticate(
            request=self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)
        return super().form_valid(form)
