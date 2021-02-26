# -*- coding: utf-8 -*-
'''
    flask_cas.utils
    -----------------
    General utilities.
'''


import flask
from flask import current_app
from werkzeug.local import LocalProxy
from .mixins import UserMixin, AnonymousUserMixin

#: A proxy for the current user. If no user is logged in, this will be an
#: anonymous user
current_user = LocalProxy(lambda: _get_user())


def _get_user():
    username = flask.session.get(
        current_app.config['CAS_USERNAME_SESSION_KEY'], None)

    if not username:
        return AnonymousUserMixin()

    u = UserMixin()
    u.username = username

    attributes = flask.session.get(
        current_app.config['CAS_ATTRIBUTES_SESSION_KEY'], None)

    if attributes:
        for attr, val in attributes.items():
            # Remove the 'cas:' of a string
            if attr.startswith('cas:'):
                attr = attr[4:]
            setattr(u, attr, val)

    return u


def _user_context_processor():
    return dict(current_user=_get_user())
