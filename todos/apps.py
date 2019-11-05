from django.apps import AppConfig


class TodosConfig(AppConfig):
    name = 'todos'
    verbose_name = 'Todo Application'

    def ready(self):
        import todos.signals
