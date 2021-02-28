"""
flask_cas.__init__
"""

from .__about__ import __version__
from .cas import CAS, login, logout, login_required
from .mixins import UserMixin, AnonymousUserMixin
from .utils import current_user
from .signals import user_logged_in, user_logged_out


__all__ = [
    CAS.__name__,
    UserMixin.__name__,
    AnonymousUserMixin.__name__,
    __version__,
    'login',
    'logout',
    'login_required',
    'current_user',
    'user_logged_in',
    'user_logged_out'
]
