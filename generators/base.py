from abc import ABC, abstractmethod
from typing import Dict, Type

class LanguageGenerator(ABC):
    @abstractmethod
    def generate(self, translations: Dict[str, str],
                 output_dir: str) -> None:
        """
        Generate code files according to the translations
        :param translations: language content key-value
        :param output_dir: output directory path
        """
        pass