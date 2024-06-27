from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('pattern_count/', views.pattern_count_view, name='pattern_count_view'),
    path('frequent_words_with_mismatches/', views.frequent_words_with_mismatches_view, name='frequent_words_with_mismatches_view'),
    path('gibbs_sampler', views.gibbs_sampler_view, name = 'gibbs_sampler_view'),
    path('de_bruijn_graph/', views.de_bruijn_graph_view, name='de_bruijn_graph_view'),
]