from django import forms

from django.forms import SelectDateWidget

from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "item_photo",
            "brand",
            "item_model",
            "date_of_manufacture",
            "category",
            "price",
            "possibility_of_exchange",
            "description"
        ]
        widgets = {
            "date_of_manufacture": SelectDateWidget(years=[i + 1960 for i in range(1, 64)])
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__update_field_widget()

    def __update_field_widget(self):
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
