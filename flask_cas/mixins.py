# -*- coding: utf-8 -*-
'''
    flask_cas.mixins
    ------------------
    This module provides mixin objects.
'''


class UserMixin(object):
    id = None
    username = None

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False


class AnonymousUserMixin(object):
    '''
    This is the default object for representing an anonymous user.
    '''
    id = None
    username = None

    @property
    def is_authenticated(self):
        return False

    @property
    def is_active(self):
        return False

    @property
    def is_anonymous(self):
        return True
