from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy


# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    # モデルの指定をする。どのモデルを使うのか？どのデータベースのテーブルのデータを扱うかの指定
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    # field... formの中にどのデータをブラウザで入力させるのかを指定する（今回は以下の４つを表示する）
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
