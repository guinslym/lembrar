from django.apps import AppConfig

class RapidamenteConfig(AppConfig):
    name = 'rapidamente'
    #verbose_name = 'rapidos'

    def ready(self):
        # import signal handlers
        #import rapidamente.signals
        pass
