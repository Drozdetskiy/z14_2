from django.conf.urls import url
from django.urls import path

from cooking.views import FeedView, UserFeedView, RecipeView, \
    CreateRecipeView, RegisterView

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('my-feed', UserFeedView.as_view(), name='user.feed'),
    path('recipe/<int:pk>/', RecipeView.as_view(), name='recipe'),
    path('create', CreateRecipeView.as_view(), name='create'),
    path('auth/register', RegisterView.as_view(), name='register')
    # url('^other-uri/\d+', view_with_params, name='other-name')
]
