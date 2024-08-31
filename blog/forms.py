from django.forms import ModelForm
from .models import Post, Tag
from django_select2.forms import Select2MultipleWidget, ModelSelect2TagWidget


class TagSelect2TagWidget(ModelSelect2TagWidget):
    queryset = Tag.objects.all()
    search_fields = ['name__icontains']

    def value_from_datadict(self, data, files, name):
        """Create objects for given non-primary-key values. Return list of all primary keys."""
        # Obtém os valores do formulário
        values = set(super().value_from_datadict(data, files, name))
        
        # Separar IDs existentes de novos valores
        existing_ids = set()
        new_values = set()

        for val in values:
            if str(val).isdigit():
                existing_ids.add(val)
            else:
                new_values.add(val)
        
        # Verifica quais IDs já existem no banco de dados
        pks = set(self.queryset.filter(pk__in=existing_ids).values_list('pk', flat=True))
        cleaned_values = list(map(str, pks))  # Converte os IDs existentes para strings
        
        # Cria novas tags para valores que não são IDs existentes
        for val in new_values:
            if val not in pks:  # Certifique-se de que a string não seja interpretada como ID
                new_tag = self.queryset.create(name=val)
                cleaned_values.append(str(new_tag.pk))  # Adiciona o ID da nova tag

        return cleaned_values


class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False
        
    class Meta:
        model = Post
        exclude = ['slug', 'author', 'created_at', 'updated_at', 'published_at', 'views']
        widgets = {
            'categories': Select2MultipleWidget,
            'tags': TagSelect2TagWidget,
        }
