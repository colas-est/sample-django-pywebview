from django.shortcuts import render

from django.views.generic import FormView, View
from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        label='Recherche',
        required=False,
        max_length=254
    )
    principal_organ = forms.ChoiceField(
        label='Organe principal',
        required=False,
        choices=(
            (None, 'Selectionner'),
            ('reglementary', 'Contrôle réglementaire'),
            ('tambour', 'Tambour sêcheur'),
            ('predoseur', 'Prédoseurs'),
            ('bandes', 'Bandes transporteuses'),
            ('tour', 'Tour')
        ),
        widget=forms.Select(attrs={'class': 'selectpicker'})
    )


class DoneInterventionForm(forms.Form):
    date = forms.CharField(
        label='Date de réalisation',
        widget=forms.TextInput(attrs={'class': 'datepicker'})
    )
    remark = forms.CharField(
        label='Remarque',
        widget=forms.Textarea
    )


class ListIntervention(FormView):
    template_name='list_intervention.html'
    form_class = SearchForm
    success_url = '/interventions/'


class DoneIntervention(FormView):
    template_name='done_intervention.html'
    form_class = DoneInterventionForm
    success_url = '/interventions/'


class LifeReport(View):
    template_name='life_report.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
