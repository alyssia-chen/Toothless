from django.views import generic
from django.urls import reverse_lazy
from .models import ClassAvails
from notes.models import Notes

class IndexView(generic.ListView):
    template_name = 'classavails/index.html'
    context_object_name = 'notes_list'
    def get_queryset(self):
        """Return all the Notes."""
        return Notes.objects.all()

class SearchView(generic.ListView):
    template_name = 'classavails/search.html'
    context_object_name = 'classavails_list'
    def get_queryset(self):
        """Return the all the class availabilities."""
        return ClassAvails.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'classavails/create.html'
    model = Notes
    fields = ['note']
    success_url = reverse_lazy('classavails:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'classavails/update.html'
    model = Notes
    fields = ['note']
    success_url = reverse_lazy('classavails:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'classavails/delete.html' # override default of greetings/greeting_confirm_delete.html
    model = Notes
    success_url = reverse_lazy('classavails:index')
    