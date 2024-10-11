from .models import Tarefa
from .forms import TarefaForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Listar tarefas
class ListaTarefa(ListView):
    model = Tarefa
    template_name = 'lista.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
        queryset = super().get_queryset()  # Obtém o queryset padrão
        search_query = self.request.GET.get('search', '')  # Captura o valor da pesquisa

        if search_query:
            queryset = queryset.filter(nome_tarefa__icontains=search_query)  # Filtra as tarefas

        return queryset  # Retorna o queryset filtrado

# Nova Tarefa 
class NovaTarefa(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'nova.html'
    success_url = '/lista'

# Atualizar Tarefas
class AtualizarTarefa(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'atualizar.html'
    success_url = '/lista'

# Apagar tarefas
class DeletarTarefa(DeleteView):
    model = Tarefa
    template_name = 'deletar.html'
    success_url = '/lista'
