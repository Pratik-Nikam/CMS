from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.conf import settings
from user.models import UserProfile
from django.contrib.auth import get_user_model


class Category(models.Model):
    category_name = models.CharField(
        db_column="category_name",
        max_length=30,
        verbose_name="Category Name",
        blank=True,
        help_text="Type of category",
    )
    def __str__(self):
        return f"{self.category_name}"


# This is a class based model used to save Content of Author related information
class Content(models.Model):
    id = models.AutoField(
        db_column="id",
        verbose_name="Id",
        primary_key=True,
        help_text="Auto incremental unique interger values.",
    )
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name="creted_by_user")
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(
        db_column="title",
        max_length=30,
        verbose_name="Title",
        blank=False,
        help_text="Title of content data",
    )
    body = models.CharField(
        db_column="body",
        max_length=300,
        verbose_name="Body",
        blank=False,
        help_text="Body of data",
    )
    summary = models.CharField(
        db_column="summary",
        max_length=60,
        verbose_name="Summary",
        blank=False,
        help_text="Summary Information",
    )
    categories = models.ManyToManyField(
        Category,
    )
    document = models.FileField(
        upload_to='documents/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        null=False,
        blank=False
    )
    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        blank=True,
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Update Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        editable=False,
        auto_now_add=True
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
        db_table = "content"
        verbose_name = "Content"
        verbose_name_plural = "Contents"

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()

        self.updated_date = timezone.now()
        super().save(*args, **kwargs)
