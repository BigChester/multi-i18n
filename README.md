# multi_i18n - Multi-language Support for Internationalization

This repo generates API files for multiple programming languages based on YAML files. 🎯 Simplifies multilingual text management for your software. 🌍 Ensures global accessibility. 💻

## Architecture

### 1. Multi-Language Resource

Multi-language contents are stored in **YAML** files. Each YAML file correspond to one language, such as en-GB, zh-CH.

### 2. Core Library

- Use **Strategy** pattern && **Simple Factory** pattern to design this module
- Yaml parser
- Language store
- Language manager

### 3. API Generator

- Generate API with target language according to YAML files
- Target language contains C, Python, ... ...

## Install & Run the Script

### Environment Required

- Python>=3.9.6
- Others see [requirements.txt](./requirements.txt)

### Generate Code

Generate all support programming language:

```bash
./dist/multi_i18n.exe main.py --yaml-dir ./translations --output-dir ./generated
```

Generate specified programming language:

```bash
./dist/multi_i18n.exe --yaml-dir ./translations --output-dir ./generated --languages c
```

## API

- [C](./API/C.md)

## TODO

- [ ] Scan all YML files in the direct folders and generate only one src file from all YML srcs
- [ ] Adding relative path has some bugs
- [ ] Support counting the number of strings
- [ ] Support generating code for Python

## Contribution

If you have any suggestions or improvements, please make sure to create a new issue or pull request.

And test the code before submitting.

See [test](./tests/test.md) for more test information.

## Reference

- [*GNU gettext*](https://www.gnu.org/software/gettext/)
- [*lv_i18n - Internationalization for LittlevGL*](https://github.com/lvgl/lv_i18n)

## License

The scripts and documentation in this project are released under the [Apache License](./LICENSE)
