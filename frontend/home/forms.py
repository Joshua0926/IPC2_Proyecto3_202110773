from django import forms

class config_form(forms.Form):
    config_file = forms.CharField()

class consume_form(forms.Form):
    consumo_file = forms.CharField()

class crearRecurso_form(forms.Form):
    nombre_recurso = forms.CharField(label='nombre_recurso', max_length=20)
    abreviatura = forms.CharField(label='abreviatura', max_length=20)
    metrica = forms.CharField(label='metrica', max_length=20)
    tipo = forms.CharField(label='tipo', max_length=20)
    costo = forms.CharField(label='costo', max_length=20)
    id = forms.CharField(label='id', max_length=20)

class crearConfig_form(forms.Form):
           
    nombre = forms.CharField(label='nombre', max_length=20)
    id = forms.CharField(label='id', max_length=20)
    descripcion = forms.CharField(label='descripcion', max_length=100)
    recursos = forms.MultipleChoiceField(
        widget  = forms.CheckboxSelectMultiple,
    )
    
    
    