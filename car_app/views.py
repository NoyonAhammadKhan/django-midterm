from django.shortcuts import render, redirect
from . import models
from . import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from django.contrib.auth.models import User
# Create your views here.


def home(request):
    cars = models.Car.objects.all()
    # print(f"car--{cars[0].pk}")
    total_car = cars.count()
    brands = models.Brand.objects.all()
    return render(request, 'home.html', {'cars': cars, 'brands': brands, 'total_car': total_car})


def filter_brand(request, id):
    brand = models.Brand.objects.get(pk=id)
    cars = models.Car.objects.filter(brand_name=brand)
    total_car = cars.count()
    brands = models.Brand.objects.all()
    return render(request, 'home.html', {'cars': cars, 'brands': brands, 'total_car': total_car})


# def car_details(request, id):
#     car = models.Car.objects.get(pk=id)
#     if request.method == 'POST':
#         comment_form = forms.CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment_form.save()
#             return redirect('details')
#     else:
#         comment_form = forms.CommentForm()

#     comments = models.Comment.objects.filter(car=car)
#     print(comments)
#     return render(request, 'car_details.html', {'car': car, 'comment_form': comment_form, 'comments': comments})


class CarDetails(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


# class CreatOrder(CreateView):
#     model = models.Order
#     template_name = 'signup.html'
#     success_url = reverse_lazy('login')
#     form_class = SignUpForm
#     success_message = "Your profile was created successfully"

def create_order(request, id):
    car = models.Car.objects.get(pk=id)
    if car.quantity > 0:
        car.quantity = car.quantity-1
        car.save()
        data = {'car': car, 'user': request.user}
        new_order = models.Order()
        new_order.car = car
        new_order.user = request.user
        new_order.save()
    return redirect('home')


def add_car(request):
    car_form = forms.CarForm()
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST, request.FILES)
        car_form.owner = user
        print(car_form)
        if car_form.is_valid():
            form = car_form.save(commit=False)
            # car_form.owner = request.user
            form.owner = user
            form.save()
            return redirect('home')
    else:
        car_form = forms.CarForm()
        return render(request, 'add_car.html', {'car_form': car_form})


def add_brand(request):

    if request.method == 'POST':
        brand_form = forms.BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            return redirect('home')
    else:
        brand_form = forms.BrandForm()
        return render(request, 'add_brand.html', {'form': brand_form})
