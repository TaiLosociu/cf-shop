import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_username(username):
    """
    Validates username format and uniqueness
    """
    # Check length
    if len(username) < 4:
        raise ValidationError('Tên đăng nhập phải có ít nhất 4 ký tự.')
    if len(username) > 30:
        raise ValidationError('Tên đăng nhập không được quá 30 ký tự.')
    
    # Check valid characters (alphanumeric, @, +, -, _, .)
    if not re.match(r'^[\w.@+-]+$', username):
        raise ValidationError('Tên đăng nhập chỉ chứa chữ, số, @, +, -, _ và dấu chấm.')
    
    # Check if username already exists
    if User.objects.filter(username=username).exists():
        raise ValidationError('Tên đăng nhập này đã được sử dụng.')
    
    return username


def validate_password_strength(password):
    """
    Validates password strength requirements
    """
    if len(password) < 8:
        raise ValidationError('Mật khẩu phải có ít nhất 8 ký tự.')
    
    # Check for uppercase
    if not re.search(r'[A-Z]', password):
        raise ValidationError('Mật khẩu phải chứa ít nhất một chữ cái in hoa.')
    
    # Check for lowercase
    if not re.search(r'[a-z]', password):
        raise ValidationError('Mật khẩu phải chứa ít nhất một chữ cái thường.')
    
    # Check for numbers
    if not re.search(r'\d', password):
        raise ValidationError('Mật khẩu phải chứa ít nhất một chữ số.')
    
    # Check for special characters
    if not re.search(r'[@$!%*?&]', password):
        raise ValidationError('Mật khẩu phải chứa ít nhất một ký tự đặc biệt (@$!%*?&).')
    
    return password


def validate_email_format(email):
    """
    Validates email format
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError('Email không hợp lệ.')
    
    if User.objects.filter(email=email).exists():
        raise ValidationError('Email này đã được sử dụng.')
    
    return email


def validate_password_match(password1, password2):
    """
    Validates that both passwords match
    """
    if password1 != password2:
        raise ValidationError('Hai mật khẩu không khớp.')
    
    return password1
