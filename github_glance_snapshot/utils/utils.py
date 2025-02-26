from django.apps import apps
from django.db.models import Model


def get_model(app_label: str, model_name: str) -> Model:
    """
    Get model from app name and model name
    Args:
        app_name (str): app name
        model_name (str): model name

    Returns:
        Model: model
    """
    return apps.get_model(app_label=app_label, model_name=model_name)
