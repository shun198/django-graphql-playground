"""
権限用のモジュール
"""
from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """ "管理者か判別する為のクラス"""

    def has_permission(self, request, view):
        """権限の有無を確認する

        Args:
            request (Request):
            view (Callable):

        Returns:
            bool
        """

        if request.user.is_superuser:
            return True
        elif request.user.is_authenticated:
            return request.user.group.name == "管理者"
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """対象のオブジェクトに対して権限の有無を確認する

        Args:
            request (Request):
            view (Callable):
            obj (Model):

        Returns:
            bool
        """

        if request.user.is_superuser:
            return True
        elif request.user.is_authenticated:
            return request.user.group.name == "管理者"
        else:
            return False


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        """スーパーユーザかどうか判定

        Args:
            request: リクエスト
            view: ビュー

        Returns:
            スーパーユーザならTrue
            それ以外はFalse
        """
        return request.user.is_superuser
