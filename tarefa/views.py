from .models import Tarefa
from .forms import TarefaForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView


class ListaTarefa(ListView):
    model = Tarefa
    template_name = 'lista.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
        queryset = super().get_queryset()  
        search_query = self.request.GET.get('search', '')  

        if search_query:
            queryset = queryset.filter(nome_tarefa__icontains=search_query)  

        return queryset  


class NovaTarefa(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'nova.html'
    success_url = '/lista'


class AtualizarTarefa(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'atualizar.html'
    success_url = '/lista'


class DeletarTarefa(DeleteView):
    model = Tarefa
    template_name = 'deletar.html'
    success_url = '/lista'
