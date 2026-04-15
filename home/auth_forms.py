from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .auth_validators import (
    validate_username, validate_password_strength, 
    validate_email_format, validate_password_match
)


class CustomSignUpForm(UserCreationForm):
    """
    Custom signup form with additional validation
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nhập địa chỉ email'
            }
        ),
        help_text='Email phải hợp lệ và không trùng lặp.'
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tên đăng nhập (4-30 ký tự)',
                    'minlength': '4',
                    'maxlength': '30'
                }
            ),
        }
    
    password1 = forms.CharField(
        label='Mật khẩu',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nhập mật khẩu'
            }
        ),
        help_text='''
        • Tối thiểu 8 ký tự<br>
        • Hỗn hợp chữ in hoa, thường, số và ký tự đặc biệt (@$!%*?&)
        '''
    )
    
    password2 = forms.CharField(
        label='Xác nhận Mật khẩu',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nhập lại mật khẩu'
            }
        )
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            validate_username(username)
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            validate_email_format(email)
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            validate_password_strength(password1)
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2:
            validate_password_match(password1, password2)
        
        return cleaned_data


class CustomLoginForm(AuthenticationForm):
    """
    Custom login form with styling
    """
    username = forms.CharField(
        label='Tên đăng nhập hoặc Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tên đăng nhập hoặc email'
            }
        )
    )
    
    password = forms.CharField(
        label='Mật khẩu',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nhập mật khẩu'
            }
        )
    )
    
    remember_me = forms.BooleanField(
        required=False,
        label='Ghi nhớ tôi',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input'
            }
        )
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            # Try login with username first, then email
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=username)
                except User.DoesNotExist:
                    raise forms.ValidationError('Tên đăng nhập, email hoặc mật khẩu không chính xác.')
            
            # Verify password
            if not user.check_password(password):
                raise forms.ValidationError('Tên đăng nhập, email hoặc mật khẩu không chính xác.')
        
        return cleaned_data
