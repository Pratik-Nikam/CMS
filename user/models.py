from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import RegexValidator


validate_phone = RegexValidator(r"^\d{10}$", 'Only 10 digits allowed.')
validate_pincode = RegexValidator(r"^\d{6}$", 'Only 6 digits are allowed.')
"""
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
"""


class UserProfile(models.Model):
    id = models.AutoField(
        db_column="id",
        verbose_name="Id",
        primary_key=True,
        help_text="Primary key auto incremental unique interger values.",
        blank=True,
    )
    email = models.EmailField(
        max_length=254,
        db_column="email",
        unique=True,
        blank=False,
        null=False,
        help_text="Email Id of the user,should be unique for each user",
    )
    name = models.CharField(
        max_length=254,
        db_column="name",
        unique=True,
        blank=False,
        null=False,
        help_text="Please enter Full Name",
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        verbose_name="User Id",
        help_text="User Id is the foreign key of User Table. This Id is linked with a particular. All the user's will have an entry in this table.",
    )
    phone = models.PositiveIntegerField(
        validators=[validate_phone],
        db_column="phone",
        null=False,
        blank=False,
        verbose_name="Phone Number",
        help_text="Phone number of user",
    )
    address = models.CharField(
        max_length=254,
        db_column="address",
        blank=True,
        null=True,
        help_text="Please enter Address",
    )
    city = models.CharField(
        max_length=50,
        db_column="city",
        blank=True,
        null=True,
        help_text="Please enter City name",
    )
    state = models.CharField(
        max_length=50,
        db_column="state",
        blank=True,
        null=True,
        help_text="Please enter State name",
    )
    country = models.CharField(
        max_length=50,
        db_column="country",
        blank=True,
        null=True,
        help_text="Please enter Country name",
    )
    pincode = models.PositiveIntegerField(
        validators=[validate_pincode],
        db_column="pincode",
        null=False,
        blank=False,
        verbose_name="Pincode",
        help_text="Area Pincode",
    )
    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        auto_now_add=True,

    )
    update_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Update Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        editable=False,
        auto_now_add=True,
    )
    is_active = models.BooleanField(
        db_column="is_active",
        default=True,
        verbose_name="Is Active",
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    class Meta:
        db_table = "user_profile"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.create_date = timezone.now()
        self.update_date = timezone.now()
        super().save(*args, **kwargs)
