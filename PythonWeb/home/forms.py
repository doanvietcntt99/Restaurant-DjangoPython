from django import forms
import re
from django.contrib.auth.models import User
from .models import *
import hashlib
from datetimepicker.widgets import DateTimePicker
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

class BookingForm(forms.Form):
    nameBooking = forms.CharField(label='Họ Và Tên', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Họ và Tên'}))
    emailBooking = forms.EmailField(label='Email', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phoneBooking = forms.CharField(label='Số Điện Thoại', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Số Điện Thoại'}))
    checkInBooking = forms.DateField(label='Ngày', widget=forms.TextInput(attrs={'placeholder': 'Ngày Tháng', 'type':'date'}))
    timeBooking = forms.TimeField(label='Thời gian', widget=forms.TextInput(attrs={'placeholder': 'Thời gian', 'type':'time'}))
    numberOfGuest = forms.IntegerField(label = 'Số Người', widget=forms.TextInput(attrs={'placeholder': 'Số Người'}))
    def save(self):
        a = Booking()
        a.nameBooking = self.cleaned_data['nameBooking']
        a.emailBooking = self.cleaned_data['emailBooking']
        a.phoneBooking = self.cleaned_data['phoneBooking']
        a.checkInBooking = self.cleaned_data['checkInBooking']
        a.timeBooking = self.cleaned_data['timeBooking']
        a.numberOfGuest = self.cleaned_data['numberOfGuest']
        a.save()
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
class LoginForm(forms.Form):
    usernameLoginForm = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    passwordLoginForm = forms.CharField(label='Password', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Password', 'type':'password'}))
    def login(self):
        UserLogin = User.objects.get(self.cleaned_data['usernameLoginForm'] == usernameUser)
        if (UserLogin.passwordUser == self.cleaned_data['passwordLoginForm']):
            return True
        else:
            return False
class RegisterForm(forms.Form):
    usernameUser = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    passwordUser = forms.CharField(label='Password', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Password', 'type':'password'}))
    rePasswordUser = forms.CharField(label='Password', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'RePassword', 'type':'password'}))
    fullnameUser = forms.CharField(label='Họ Và Tên', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Họ và Tên'}))
    phoneUser = forms.CharField(label='Phone', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Số Điện Thoại'}))
    emailUser = forms.CharField(label='Email', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    def clean_password(self):
        if (self.cleaned_data['passwordUser'] == self.cleaned_data['rePasswordUser']):
            return True
        else:
            return False
    def save(self):
        a = User()
        a.usernameUser = self.cleaned_data['usernameUser']
        a.passwordUser = encrypt_string(self.cleaned_data['passwordUser'])
        a.fullnameUser = self.cleaned_data['fullnameUser']
        a.dobUser = '1999-01-02'
        a.addressUSer = 'Hà Nội'
        a.emailUser = self.cleaned_data['emailUser']
        a.phoneUser = self.cleaned_data['phoneUser']
        a.avatarUser = 'images/users/86375348_187159582384515_1906251973686984704_n_491KJzH.jpg'
        a.statusUser = '1'
        a.save()
class UserDetailForm(forms.Form):
    usernameUser = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'value': 'Username'}))
    fullnameUser = forms.CharField(label='Fullname', max_length=30)
    dobUser = forms.DateField(label='DOB', widget=DateTimePicker(),)
    addressUSer = forms.CharField(label='Address')
    emailUser = forms.CharField(label='Email')
    phoneUser = forms.CharField(label='Phone', max_length=12)
    def save(self):
        a = User.objects.get(usernameUser=self.cleaned_data['usernameUser'])
        a.fullnameUser = self.cleaned_data['fullnameUser']
        a.dobUser = self.cleaned_data['dobUser']
        a.addressUSer = self.cleaned_data['addressUSer']
        a.emailUser = self.cleaned_data['emailUser']
        a.phoneUser = self.cleaned_data['phoneUser']
        a.save()
class ReviewCustomerForm(forms.Form):
    id_author = forms.IntegerField()
    reviewContent = forms.CharField(label='reviewContent', max_length=50, widget=forms.TextInput(attrs={'style': 'color:white!black'}))
    def save(self):
        a = ReviewCustomer()
        a.author = request.session.get('idUser')
        a.reviewContent = self.cleaned_data['reviewContent']
