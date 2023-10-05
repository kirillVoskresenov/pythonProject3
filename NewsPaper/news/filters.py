import django_filters
from django import forms
from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):

    date = django_filters.DateFilter(
        field_name='article_date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        lookup_expr='gte',
        label='Date (beginning with)'
    )

    type = django_filters.ChoiceFilter(
        field_name='post_type',
        choices=Post.Types,
        label='Category'
    )


    class Meta:
        model = Post
        fields = {
           'author': ['exact'],
           'title': ['icontains']
       }