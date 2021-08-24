from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from .models import Topic
from .forms import TopicForm,GoodTopicForm,BadTopicForm


from users.models import CustomUser



class BbsView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        users   = CustomUser.objects.all()

        topics  = Topic.objects.all()
        context = { "topics":topics,
                    "users":users,
                }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        copied              = request.POST.copy()
        copied["user"]      = request.user.id

        form    = TopicForm(copied)
        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")

        return redirect("bbs:index")

index   = BbsView.as_view()


class BbsGoodView(LoginRequiredMixin,View):

    def post(self, request, pk, *args, **kwargs):

        copied              = request.POST.copy()
        copied["user"]      = request.user.id
        copied["target"]    = pk

        form    = GoodTopicForm(copied)
        if form.is_valid():
            print("バリデーションOK")
            form.save()

        return redirect("bbs:index")

good    = BbsGoodView.as_view()

class BbsBadView(LoginRequiredMixin,View):

    def post(self, request, pk, *args, **kwargs):

        copied              = request.POST.copy()
        copied["user"]      = request.user.id
        copied["target"]    = pk

        form    = BadTopicForm(copied)
        if form.is_valid():
            print("バリデーションOK")
            form.save()

        return redirect("bbs:index")

bad     = BbsBadView.as_view()
