from django import forms
from django.contrib import admin
from .models import User, Posts, Album, Photos, Comments, Todos
class CustomUserCreationForm(forms.ModelForm):
    street = forms.CharField(max_length=100)
    suite = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    zipcode = forms.CharField(max_length=10)
    lat = forms.CharField(max_length=20)
    lng = forms.CharField(max_length=20)
    company_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'phone', 'website']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        # Adres alanını JSON olarak birleştirme
        address_data = {
            'street': self.cleaned_data['street'],
            'suite': self.cleaned_data['suite'],
            'city': self.cleaned_data['city'],
            'zipcode': self.cleaned_data['zipcode'],
            'geo': {
                'lat': self.cleaned_data['lat'],
                'lng': self.cleaned_data['lng']
            }
        }
        user.address = address_data
        user.company = {'name': self.cleaned_data['company_name']}
        if commit:
            user.save()
        return user



class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'phone', 'website')
    search_fields = ('name', 'email', 'username')
    form = CustomUserCreationForm

    def get_form(self, request, obj=None, **kwargs):
        if obj:  # Eğer bir nesne varsa (düzenleme işlemi)
            self.form.base_fields['street'].initial = obj.address['street']
            self.form.base_fields['suite'].initial = obj.address['suite']
            self.form.base_fields['city'].initial = obj.address['city']
            self.form.base_fields['zipcode'].initial = obj.address['zipcode']
            self.form.base_fields['lat'].initial = obj.address['geo']['lat']
            self.form.base_fields['lng'].initial = obj.address['geo']['lng']
            self.form.base_fields['company_name'].initial = obj.company['name']
        return super().get_form(request, obj, **kwargs)

# UserAdmin sınıfını ve diğer modelleri kaydediyoruz
admin.site.register(User, UserAdmin)
admin.site.register(Posts)
admin.site.register(Album)
admin.site.register(Photos)
admin.site.register(Comments)
admin.site.register(Todos)