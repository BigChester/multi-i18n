# multi_i18n - Multi-language Support for Internationalization

This repo generates API files for multiple programming languages based on YAML files. 🎯 Simplifies multilingual text management for your software. 🌍 Ensures global accessibility. 💻

## Architecture

### 1. Multi-Language Resource

Multi-language contents are stored in **YAML** files. Each YAML file correspond to one language, such as en-GB, zh-CH.

### 2. Core Librar

- Use **Strategy** pattern to design this module
- Yaml parser
- Lanugage store
- Language manager

### 3. API Generator

- Generate API with target language according to YAML files
- Target language contains C, Python, ... ...

## Install & Run the Script

...

## Reference
- [*GNU gettext*](https://www.gnu.org/software/gettext/)
- [*lv_i18n - Internationalization for LittlevGL*](https://github.com/lvgl/lv_i18n)