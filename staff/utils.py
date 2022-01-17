from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse

class ObjectListMixin:
    model = None
    template = None

    def get(self, request):
        objects = self.model.objects.all()
        return render(request, self.template, context={'objects': objects})


class ObjectDetailMixin:
    model = None
    template = None
    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    model = None
    model_form = None
    template = None
    redirect_template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_position = bound_form.save()
            objects = self.model.objects.all()
            return render(request, self.redirect_template, context={'objects': objects})
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
     model = None
     model_form = None
     template = None

     def get(self, request, slug):
         obj = self.model.objects.get(slug__iexact=slug)
         bound_form = self.model_form(instance=obj)
         return render(request, self.template, context={self.model.__name__.lower(): bound_form})

     def post(self, request, slug):
         obj = self.model.objects.get(slug__iexact=slug)
         bound_form = self.model_form(request.POST, instance=obj)
         if bound_form.is_valid():
             obj_update = bound_form.save()
             return redirect(obj_update)
         return render(request, self.template, context={self.model.__name__lower(): obj, 'form': bound_form})


class ObjectsDeleteMixin:
    model = None
    template = None
    link = None
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.link))