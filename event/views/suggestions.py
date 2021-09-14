from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from event.forms import SuggestionBoxForm, BlogForm
from event.models import SuggestionBox


@method_decorator(login_required, 'dispatch')
class SuggestionListView(ListView):
    model = SuggestionBox

    def get_queryset(self):
        return SuggestionBox.objects.filter(user=self.request.user).select_related('event')


@method_decorator(login_required, 'dispatch')
class SuggestionCreateView(CreateView):
    model = SuggestionBox
    # fields = ['category', 'description', 'event']
    form_class = SuggestionBoxForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SuggestionCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.object.category == 'Suggestions':
            msg = "Thank you for your Valuable Feedback!"
            messages.success(self.request, msg)
        else:
            msg = "We have Received your Complaint! We Will look into it and will get back to you soon!"
            messages.info(self.request, msg)
        return reverse('suggestion-box-list')


@method_decorator(login_required, 'dispatch')
class SuggestionUpdateView(UpdateView):
    model = SuggestionBox
    fields = ['description', 'event']

    def get_success_url(self):
        msg = f"Your {self.object.category} has been updated!"
        messages.success(self.request, msg)
        return reverse('suggestion-box-list')


@method_decorator(login_required, 'dispatch')
class SuggestionDeleteView(DeleteView):
    model = SuggestionBox

    def get_success_url(self):
        msg = f"Your {self.object.category} has been Deleted!"
        messages.error(self.request, msg)
        return reverse('suggestion-box-list')


def form_handler(request):
    # title, content, event
    if request.method == 'POST':
        form = SuggestionBoxForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, "Successfully created Suggestion Box entry")
            return redirect('/')
    else:
        form = SuggestionBoxForm()
    context = {
        "form": form
    }
    return render(request, 'index.html', context)


def form_handler2(request):

    # title, content, event
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, )
        if form.is_valid():
            messages.success(request, "Successfully created a Blog entry")
            return redirect('/')
    else:
        form = BlogForm()
    context = {
        "form": form
    }
    return render(request, 'index.html', context)


class SomeFormView(FormView):
    form_class = BlogForm
    template_name = 'index.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        messages.success(self.request, "Successfully created a Blog entry form blog class!")
        return super(SomeFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('form-class')


class SomeCreateFormView(CreateView):
    form_class = SuggestionBoxForm





