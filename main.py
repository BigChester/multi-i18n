import argparse
from pathlib import Path
from utils.yaml_loader import load_yaml_files
from manager import GeneratorManager

def main():
    parser = argparse.ArgumentParser(description="Multi-language Code Generator")
    parser.add_argument("--yaml-dir", required=True, help="Path to the directory containing YAML files.")
    parser.add_argument("--output-dir", required=True, help="Path to the output directory.")
    parser.add_argument("--languages", default=None, help="Comma-separated list of target languages (e.g., 'python,c'). Default: all.")
    args = parser.parse_args()

    yaml_dir = Path(args.yaml_dir)
    output_dir = Path(args.output_dir)
    if not yaml_dir.is_dir():
        print(f"Error: YAML directory '{yaml_dir}' does not exist.")
        return
    output_dir.mkdir(parents=True, exist_ok=True)

    translations = load_yaml_files(yaml_dir)

    manager = GeneratorManager()
    target_languages = args.languages.split(",") if args.languages else manager.get_supported_languages()

    for language in target_languages:
        lang_output_dir = output_dir / language
        lang_output_dir.mkdir(parents=True, exist_ok=True)
        manager.generate(language, translations, lang_output_dir)


if __name__ == "__main__":
    main()
