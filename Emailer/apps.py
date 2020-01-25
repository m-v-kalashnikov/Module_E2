from django.apps import AppConfig


class EmailerConfig(AppConfig):
    name = 'Emailer'

    def ready(self):
        import Emailer.signals
