from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Post

class HomePage(ListView):
    template_name = "homepage.html"
    model = Post
    paginate_by = 10
    ordering = ['pubdate']

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter().order_by("-pubdate")[
            :10
        ]
        return context


def authentication(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          # or any other success page
          return HttpResponse("Logged in")
    return render(request, 'registration/login.html', {'form': form})
