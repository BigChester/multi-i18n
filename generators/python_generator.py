from typing import Dict
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from .base import LanguageGenerator

class PythonGenerator(LanguageGenerator):
    """使用 Jinja2 模板生成 Python 代码的生成器"""
    
    def generate(self, translations: Dict[str, str], output_dir: str) -> None:
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("python_template.j2")
        
        output = template.render(translations=translations)
        
        file_path = Path(output_dir) / "translations.py"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Python translations generated at {file_path}")
