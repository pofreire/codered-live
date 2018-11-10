from django.apps import AppConfig


class PainelUsuarioConfig(AppConfig):
    name = 'painel'


    def ready(self):
        # import signal handlers
        import painel.signals
