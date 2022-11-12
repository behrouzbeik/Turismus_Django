import django_filters
from .models import *
from django import forms

class ResidenceFilter(django_filters.FilterSet):
    
    _SCORE={
        ('Descending','Descending'),
        ('Ascending','Ascending'),
    }

    graid_star = django_filters.MultipleChoiceFilter(choices=Residence.GSTAR, widget = forms.CheckboxSelectMultiple, field_name='graid_star',lookup_expr='exact')
    city = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all(),widget = forms.CheckboxSelectMultiple)
    buyscore = django_filters.ChoiceFilter(choices = _SCORE, method='buyscore_filter')
    userscore = django_filters.ChoiceFilter(choices = _SCORE, method='userscore_filter')
    type = django_filters.MultipleChoiceFilter(choices=Residence.RESIDENCE_TYPE, widget = forms.CheckboxSelectMultiple, field_name='type',lookup_expr='exact')

    def buyscore_filter(self,queryset,name,value):
        data = 'buyscore' if value == 'Ascending' else '-buyscore'
        return queryset.order_by(data)
    
    def userscore_filter(self,queryset,name,value):
        data = 'userscore' if value == 'Ascending' else '-userscore'
        return queryset.order_by(data)
    

# class CategoriesCounter():


class TransportFilter(django_filters.FilterSet):
    
    _SCORE={
        ('Descending','Descending'),
        ('Ascending','Ascending'),
    }

    graid_star = django_filters.MultipleChoiceFilter(choices=Residence.GSTAR, widget = forms.CheckboxSelectMultiple, field_name='graid_star',lookup_expr='exact')
    city = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all(),widget = forms.CheckboxSelectMultiple)
    buyscore = django_filters.ChoiceFilter(choices = _SCORE, method='buyscore_filter')
    userscore = django_filters.ChoiceFilter(choices = _SCORE, method='userscore_filter')
    type = django_filters.MultipleChoiceFilter(choices=Residence.RESIDENCE_TYPE, widget = forms.CheckboxSelectMultiple, field_name='type',lookup_expr='exact')

    def buyscore_filter(self,queryset,name,value):
        data = 'buyscore' if value == 'Ascending' else '-buyscore'
        return queryset.order_by(data)
    
    def userscore_filter(self,queryset,name,value):
        data = 'userscore' if value == 'Ascending' else '-userscore'
        return queryset.order_by(data)