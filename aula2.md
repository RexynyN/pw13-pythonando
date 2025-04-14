Acesse diretamente pelo Notion

```python
<https://grizzly-amaranthus-f6a.notion.site/Aula-2-1c36cf8ea89f80438f8cc674e1d823ac?pvs=4>
```

## Gráficos

Adicione nas views os cálculos para os gráficos

```python
def mentorados(request):
    if request.method == 'GET':
        navigators = Navigators.objects.filter(user=request.user)
        mentorados = Mentorados.objects.filter(user=request.user)
        
        estagios_flat = [i[1] for i in Mentorados.estagio_choices]
        qtd_estagios = []

        for i, j in Mentorados.estagio_choices:
            qtd_estagios.append(Mentorados.objects.filter(estagio=i).count())

    
        return render(request, 'mentorados.html', {'estagios': Mentorados.estagio_choices, 'navigators': navigators, 'mentorados': mentorados, 'estagios_flat': estagios_flat, 'qtd_estagios': qtd_estagios})
```

Adicione o JavaScript

```python
<script src="<https://cdn.jsdelivr.net/npm/chart.js>"></script>

<script>
  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: {{estagios_flat|safe}},
      datasets: [{
        label: '',
        data: {{qtd_estagios|safe}},
        borderWidth: 1
      }]
    },
    
  });
</script>
```

## Reuniões

Crie uma URL para reuniões

```python
path('reunioes/', views.reunioes, name='reunioes'),
```

Crie a view

```python
def reunioes(request):
    if request.method == 'GET':
        return render(request, 'reunioes.html')
```

Desenvolva o HTML

```python
{% extends "base.html" %}
{% load static %}
{% block 'body' %}
<header class="bg-slate-900">
    <nav class="flex items-center justify-between p-4 lg:px-8" aria-label="Global">
      <div class="flex lg:flex-1">
        <a href="#" class="-m-1.5 p-1.5">
          <span class="sr-only">Your Company</span>
          <img class="h-8 w-auto" src="{% static 'logo.png' %}" alt="">
        </a>
      </div>
      <div class="flex lg:hidden">
        <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700">
          <span class="sr-only">Open main menu</span>
          <svg class="size-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
          </svg>
        </button>
      </div>
      <div class="hidden lg:flex lg:gap-x-12">
        <a href="#" class="text-sm/6 font-semibold text-gray-100">Mentorados</a>
        <a href="#" class="text-sm/6 font-semibold text-gray-100">Tarefas</a>
        <a href="#" class="text-sm/6 font-semibold text-gray-100">Progressos</a>
        <a href="#" class="text-sm/6 font-semibold text-gray-100">Navigators</a>
      </div>
      <div class="hidden lg:flex lg:flex-1 lg:justify-end">
        
      </div>
    </nav>
  </header>
  
  <div class="bg-[#040e1b] min-h-screen">
    <div class="max-w-7xl mx-auto py-8">
        <div class="grid grid-cols-2 gap-12 ">
            <div>
              {% if messages %}
                    {% for message in messages %}
                        <div class="rounded-md {{message.tags}} mt-4">
                            <div class="flex">
                                <div class="ml-3 py-4">
                                    {{message}}

                                </div>

                            </div>
                        </div>
                    {% endfor %}
                {% endif %}
                <form action="{% url 'reunioes' %}" method="POST">{% csrf_token %}
                  <h2 class="mt-4 text-2xl/9 font-bold tracking-tight text-gray-100">Abra um horário</h2>
                  <label for="email" class="block text-sm/6 font-medium text-gray-200">Data</label>
                  <input type="datetime-local" name="data" id="date" required class="block w-full rounded-md bg-white/5 px-3 py-1.5 text-base text-white outline outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6">
                  
                  <button type="submit" class="flex w-full justify-center cursor-pointer rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 mt-4">Abrir horários</button>
                </form>

            </div>
            <div>
              
                
                <ul role="list" class="divide-y divide-gray-800">
                   
                    <li class="flex justify-between gap-x-6 py-5">
                      <div class="flex min-w-0 gap-x-4">
                        <img class="size-12 flex-none rounded-full bg-gray-800" src="#" alt="">
                        <div class="min-w-0 flex-auto">
                          <p class="text-sm/6 font-semibold text-white">Nome</p>
                          <p class="mt-1 truncate text-xs/5 text-gray-400">Descricao</p>
                        </div>
                      </div>
                      <div class="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                        <p class="text-sm/6 text-white">Data</p>
                        <p class="mt-1 text-xs/5 text-gray-400"></p>
                      </div>
                    </li>
                    
                  </ul>
                  
            </div>
        </div>

    </div>
  </div>

{% endblock 'body' %}
```

Crie as models para armazenar as reuniões e os horários

```python
class DisponibilidadeHorarios(models.Model):
    data_inicial = models.DateTimeField(null=True, blank=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    agendado = models.BooleanField(default=False)

    @property
    def data_final(self):
        return self.data_inicial + timedelta(minutes=50)
    
class Reuniao(models.Model):
    tag_choices = (
        ('G', 'Gestão'),
        ('M', 'Marketing'),
        ('RH', 'Gestão de pessoas'),
        ('I', 'Impostos')
    )

    data = models.ForeignKey(DisponibilidadeHorarios, on_delete=models.CASCADE)
    mentorado = models.ForeignKey(Mentorados, on_delete=models.CASCADE)
    tag = models.CharField(max_length=2, choices=tag_choices)
    descricao = models.TextField()
```

Execute as migrações!

Processe os dados para abertura de um horário

```python
def reunioes(request):
    if request.method == 'GET':
        return render(request, 'reunioes.html')
    else:
        data = request.POST.get('data')

        data = datetime.strptime(data, '%Y-%m-%dT%H:%M')

        disponibilidade = DisponibilidadeHorarios.objects.filter(
            data_inicial__gte=(data - timedelta(minutes=50)),
            data_inicial__lte=(data + timedelta(minutes=50))
        )

        if disponibilidades.exists():
            messages.add_message(request, constants.ERROR, 'Você já possui uma reunião em aberto.')
            return redirect('reunioes')

        disponibilidade = DisponibilidadeHorarios(
            data_inicial=data,
            mentor=request.user

        )
        disponibilidade.save()

        messages.add_message(request, constants.SUCCESS, 'Horário disponibilizado com sucesso.')
        return redirect('reunioes')
```

## Token mentorado

Para os mentorados acessarem determinadas páginas vamos usar um token de login

Primeiro adicione uma nova coluna na models Mentorado

```python
token = models.CharField(max_length=16, null=True, blank=True)
```

Agora use o método save para gerar um token aleatório

```python
def save(self, *args, **kwargs):
    if not self.token: 
        self.token = self.gerar_token_unico()
    super().save(*args, **kwargs)

def gerar_token_unico(self):
    while True:
        token = secrets.token_urlsafe(8)  
        if not Mentorados.objects.filter(token=token).exists():
            return token
```

Crie a URL para o mentorado se autenticar

```python
path('auth/', views.auth, name="auth_mentorado"),
```

Adicione a view

```python
def auth(request):
    if request.method == 'GET':
        return render(request, 'auth_mentorado.html')
```

Crie o auth_mentorado.html

```python
{% extends "base.html" %}

{% block 'body' %}
    <div class="bg-gray-900 flex items-center justify-center h-screen">
        <div class="bg-gray-800 p-8 rounded-lg shadow-lg text-center w-96">
            <form action="{% url 'auth_mentorado' %}" method="POST"> {% csrf_token %}
                
                <h2 class="text-2xl font-bold text-gray-200 mb-4">Acessar conteúdo</h2>
                {% if messages %}
                    {% for message in messages %}
                        <div class="rounded-md {{message.tags}} mt-4">
                            <div class="flex">
                                <div class="ml-3 py-4">
                                    {{message}}

                                </div>

                            </div>
                        </div>
                    {% endfor %}
                {% endif %}
                <label class="text-gray-400 block text-left mb-1">Token de acesso</label>
                <input type="text" name="token" class="w-full p-3 rounded-md bg-gray-300 text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Digite seu token">

                <button class="w-full mt-4 bg-indigo-600 text-white font-semibold p-3 rounded-md hover:bg-indigo-700 transition cursor-pointer">Acessar</button>
            </form>
        </div>
    </div>
{% endblock 'body' %}

```

Processe os dados no back-end

```python
def auth(request):
    if request.method == 'GET':
        return render(request, 'auth_mentorado.html')
    else:
        token = request.POST.get('token')

        if not Mentorados.objects.filter(token=token).exists():
            messages.add_message(request, constants.ERROR, 'Token inválido')
            return redirect('auth_mentorado')
        
        response = redirect('escolher_dia')
        response.set_cookie('auth_token', token, max_age=3600)
        return response
```

## Marcar reunião

Crie uma URL para página que o mentorado irá escolher um dia em aberto

```python
path('escolher_dia/', views.escolher_dia, name='escolher_dia'),
```

Crie uma função que valida o token do mentorado em [auth.py](http://auth.py)

```python
from .models import Mentorados

def valida_token(token):
    return Mentorados.objects.filter(token=token).first()
```

Crie a view

```python
def escolher_dia(request):
    if not valida_token(request.COOKIES.get('auth_token')):
        return redirect('auth_mentorado')
    if request.method == 'GET':
        disponibilidades = DisponibilidadeHorarios.objects.filter(
            data_inicial__gte=datetime.now(),
            agendado=False
        ).values_list('data_inicial', flat=True)
        horarios = []
        for i in disponibilidades:
            horarios.append(i.date().strftime('%d-%m-%Y'))

        return render(request, 'escolher_dia.html', {'horarios': list(set(horarios))})

```

Construa o HTML

```python
{% extends "base.html" %}
{% load static %}
{% block 'body' %}
  <div class="bg-[#040e1b] min-h-screen">
    <div class="max-w-7xl mx-auto py-8">
        <h2 class="mt-4 text-2xl/9 font-bold tracking-tight text-gray-100">Escolha o dia para reunião</h2>
        {% if messages %}
            {% for message in messages %}
                <div class="rounded-md {{message.tags}} mt-4">
                    <div class="flex">
                        <div class="ml-3 py-4">
                            {{message}}

                        </div>

                    </div>
                </div>
            {% endfor %}
        {% endif %}
        <ul role="list" class="mt-3 grid grid-cols-1 gap-5 sm:grid-cols-2 sm:gap-6 lg:grid-cols-4">
            {% for horario in horarios %}         
                <li class="col-span-1 flex rounded-md shadow-sm">
                   
                        <div class="flex px-4 shrink-0 items-center justify-center rounded-l-md bg-pink-600 text-sm font-medium text-white">Março</div>
                        <div class="flex flex-1 items-center justify-between truncate rounded-r-md border-b border-r border-t border-gray-200 bg-white">
                            <div class="flex-1 truncate px-4 py-2 text-sm">
                            <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Quinta-feira</a>
                            <p class="text-gray-500">{{horario}}</p>
                            </div>
                        </div>
                    
                </li>    
            {% endfor %}
            
        </ul>
    </div>
  </div>

  
{% endblock 'body' %}
```

Crie a URL onde o mentorado irá de fato agendar a reunião

```python
path('agendar_reuniao/', views.agendar_reuniao, name='agendar_reuniao'),
```

Agora a view

```python
def agendar_reuniao(request):
    if not valida_token(request.COOKIES.get('auth_token')):
        return redirect('auth_mentorado')
    if request.method == 'GET':
        data = request.GET.get("data")
        data = datetime.strptime(data, '%d-%m-%Y')
        horarios = DisponibilidadeHorarios.objects.filter(
            data_inicial__gte=data,
            data_inicial__lt=data + timedelta(days=1),
            agendado=False
        )
        return render(request, 'agendar_reuniao.html', {'horarios': horarios, 'tags': Reuniao.tag_choices})
```

E o HTML

```python
{% extends "base.html" %}
{% load static %}
{% block 'body' %}
  <div class="bg-[#040e1b] min-h-screen">
    <div class="max-w-5xl mx-auto py-8">
      <form action="{% url 'agendar_reuniao' %}" method="POST">{% csrf_token %}
        <h2 class="mt-4 text-2xl/9 font-bold tracking-tight text-gray-100">Agende sua reunião</h2>
        <label for="email" class="block mt-4 text-sm/6 font-medium text-gray-200">Horário</label>
        <select name="horario" id="" class="block  w-full rounded-md bg-white/5 px-3 py-2.5 text-base text-white outline outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6">
          
          {% for horario in horarios %}
            <option value="{{horario.id}}" class="text-slate-900">{{horario.data_inicial.time}} às {{horario.data_final.time}}</option>
          {% endfor %}

        </select>

        <label for="email" class="block mt-4 text-sm/6 font-medium text-gray-200">Tag</label>
        <select name="tag" id="" class="block  w-full rounded-md bg-white/5 px-3 py-2.5 text-base text-white outline outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6">
          
          {% for tag in tags %}
            <option value="{{tag.0}}" class="text-slate-900">{{tag.1}}</option>
          {% endfor %}
              
          
        </select>

        <label for="email" class="block mt-4 text-sm/6 font-medium text-gray-200">Descrição</label>
        <textarea name="descricao" class="block w-full rounded-md bg-white/5 px-4 py-2 text-base text-white outline outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"></textarea>
        <button type="submit" class="flex mt-4 w-full justify-center cursor-pointer rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Agendar</button>
      </form>   
    </div>
  </div>

  
{% endblock 'body' %}
```

Em escolher_dia.html redirecione para a página criada

```python
{% url 'agendar_reuniao' %}?data={{horario}}
```