from django.db.models import Model
from django.apps import apps


class Models:
    """Model Import"""

    USER = {"app_label": "users", "model_name": "User"}

    @staticmethod
    def get_model(app_label: str, model_name: str) -> Model:
        """
        Get model from app name and model name
        Args:
            app_label (str): app name
            model_name (str): model name

        Returns:
            Model: model
        """
        return apps.get_model(app_label=app_label, model_name=model_name)

    @classmethod
    def __getattribute__(cls, name):
        """
        Get model from app name and model name
        Args:
            name (ste): name of the model
        Raises:
            AttributeError: if model not found

        Returns:
            Model: model
        """
        return cls.get_model(**getattr(cls, name))


models = Models()
