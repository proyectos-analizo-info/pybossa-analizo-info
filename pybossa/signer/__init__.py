from itsdangerous import URLSafeTimedSerializer


class Signer(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None: # pragma: no cover
            self.init_app(app)

    def init_app(self, app):
        key = app.config['ITSDANGEROUSKEY']
        self.signer = URLSafeTimedSerializer(key)
