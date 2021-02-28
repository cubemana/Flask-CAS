# -*- coding: utf-8 -*-
'''
    flask_login.signals
    -------------------
    This module provides signals to get notified when Flask-Login performs
    certain actions.
'''


from flask.signals import Namespace


_signals = Namespace()


#: Sent when a user is logged in. In addition to the app (which is the
#: sender), it is passed `user`, which is the user being logged in.
user_logged_in = _signals.signal('logged-in')

#: Sent when a user is logged out. In addition to the app (which is the
#: sender), it is passed `user`, which is the user being logged out.
user_logged_out = _signals.signal('logged-out')
