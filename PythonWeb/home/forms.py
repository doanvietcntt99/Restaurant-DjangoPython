from django import forms
import re
from django.contrib.auth.models import User
from .models import Booking
from .models import Comment
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.nameBooking = kwargs.pop('nameBooking', None)
        self.emailBooking = kwargs.pop('emailBooking', None)
        self.phoneBooking = kwargs.pop('phoneBooking', None)
        self.checkInBooking = kwargs.pop('checkInBooking', None)
        self.timeBooking = kwargs.pop('timeBooking', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        Booking = super().save(commit=False)
        Booking.nameBooking = self.nameBooking
        Booking.emailBooking = self.emailBooking
        Booking.phoneBooking = self.phoneBooking
        Booking.checkInBooking = self.checkInBooking
        Booking.timeBooking = self.timeBooking
        Booking.save()
    class Meta:
        model = Booking
        fields = ["nameBooking","emailBooking","phoneBooking","checkInBooking", "timeBooking"]

class CommentForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()
    class Meta:
        model = Comment
        fields = ["body"]