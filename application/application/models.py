from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    """システムユーザ"""

    username_validator = UnicodeUsernameValidator()

    # 不要なフィールドはNoneにすることができる
    first_name = None
    last_name = None
    date_joined = None
    groups = None
    id = models.AutoField(
        primary_key=True,
        db_comment="ID",
    )
    employee_number = models.CharField(
        unique=True,
        validators=[RegexValidator(r"^[0-9]{8}$")],
        max_length=8,
        db_comment="社員番号",
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        db_comment="ユーザ名",
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        db_comment="メールアドレス",
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.DO_NOTHING,
        related_name="users",
        db_comment="社員権限用グループ",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="作成日",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_comment="更新日",
    )
    is_verified = models.BooleanField(
        default=False,
        db_comment="有効化有無",
    )
    created_by = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(class)s_created_by",
        db_comment="作成者",
    )
    updated_by = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(class)s_updated_by",
        db_comment="更新者",
    )

    USERNAME_FIELD = "employee_number"
    REQUIRED_FIELDS = ["email", "username"]

    class Meta:
        ordering = ["employee_number"]
        db_table = "User"
        db_table_comment = "システムユーザ"

    def save(self, *args, **kwargs):
        # 既に登録されているシステム利用者情報の保存処理
        if self.id:
            if not "updated_by" in kwargs:
                self.updated_by = self
            else:
                self.updated_by = kwargs.get("updated_by")
                kwargs.pop("updated_by")
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class Category(models.Model):
    """分類"""

    id = models.AutoField(
        primary_key=True,
        db_comment="ID",
    )
    name = models.CharField(
        max_length=100,
        db_comment="分類名",
    )

    class Meta:
        db_table = "Category"
        db_table_comment = "分類"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """原材料"""

    id = models.AutoField(
        primary_key=True,
        db_comment="ID",
    )
    name = models.CharField(
        max_length=100,
        db_comment="原材料名",
    )
    notes = models.TextField(
        db_comment="原材料メモ",
    )
    category = models.ForeignKey(
        Category,
        related_name="ingredients",
        on_delete=models.CASCADE,
        db_comment="分類FK",
    )

    class Meta:
        db_table = "Ingredient"
        db_table_comment = "原材料"

    def __str__(self):
        return self.name
