from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import RegistroForm, LoginForm, CategoriaForm, SubcategoriaForm, ProductoForm
from django.contrib import messages
from .models import Categoria, Subcategoria, Producto

# Create your views here.

def index(request):
    return render(request, 'base.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido.')
            return redirect('menu_principal') # Nombre de la URL para el menú principal
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.sucess(request, 'Inicio de sesión exitoso. Bienvenido.')
            return redirect('menu_principal') # Nombre de la URL para el menú principal
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def menu_principal(request):
    return render(request, 'menu_principal.html')

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria_list.html', {'categorias': categorias})

# Vista para crear Categoría
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categoria_form.html', {'form': form})

# Vista para editar Categoría
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria_edit.html', {'form': form})

# Vista para eliminar Categoría
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'categoria_delete.html', {'categoria': categoria})

# Vista para listar Subcategorías
def lista_subcategorias(request):
    subcategorias = Subcategoria.objects.all()
    return render(request, 'subcategoria_list.html', {'subcategorias': subcategorias})

# Vista para crear Subcategoría
def crear_subcategoria(request):
    if request.method == 'POST':
        form = SubcategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_subcategorias')
    else:
        form = SubcategoriaForm()
    return render(request, 'subcategoria_form.html', {'form': form})

# Vista para editar Subcategoría
def editar_subcategoria(request, pk):
    subcategoria = get_object_or_404(Subcategoria, pk=pk)
    if request.method == 'POST':
        form = SubcategoriaForm(request.POST, instance=subcategoria)
        if form.is_valid():
            form.save()
            return redirect('lista_subcategorias')
    else:
        form = SubcategoriaForm(instance=subcategoria)
    return render(request, 'subcategoria_edit.html', {'form': form})

# Vista para eliminar Subcategoría
def eliminar_subcategoria(request, pk):
    subcategoria = get_object_or_404(Subcategoria, pk=pk)
    if request.method == 'POST':
        subcategoria.delete()
        return redirect('lista_subcategorias')
    return render(request, 'subcategoria_delete.html', {'subcategoria': subcategoria})

# Vista para listar Productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos})

# Vista para crear Producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

# Vista para editar Producto
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_edit.html', {'form': form})

# Vista para eliminar Producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'producto_delete.html', {'producto': producto})

# Vista para listar Subcategorías con la cantidad de Productos asociados
def subcategorias_con_productos(request):
    subcategorias = Subcategoria.objects.all()
    return render(request, 'subcategoria_list_with_count.html', {'subcategorias': subcategorias})