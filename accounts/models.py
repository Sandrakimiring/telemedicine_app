import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    USER_TYPES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    user_type = models.CharField(max_length=7, choices=USER_TYPES)
    specialization = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Specialization area for doctors (e.g., Cardiologist)."
    )
    credentials = models.TextField(
        blank=True, 
        null=True,
        validators=[MinLengthValidator(10, "Credentials must be at least 10 characters.")],
        help_text="Professional credentials or certifications."
    )
    profile_image = models.ImageField(
        upload_to='user_profiles/',
        blank=True,
        null=True,
        help_text="Optional profile image."
    )
    date_of_birth = models.DateField(
        blank=True, 
        null=True, 
        help_text="Date of birth for the user."
    )
    is_active = models.BooleanField(default=True, help_text="Indicates if the user is active.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the user account was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Time when the user account was last updated.")

    # Adjust the related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_groups",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions",
        related_query_name="customuser",
    )

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

