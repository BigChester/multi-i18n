# C API

## 1. Initialize the multi-language library

```c
multi_i18n_status_t multi_i18n_init(const multi_i18n_language_pack_t* language_pack);
```

## 2. Set the locale

```c
multi_i18n_status_t multi_i18n_set_locale(const char* locale);
```

## 3. Get the text of the message

```c
const char* multi_i18n_get_text(const char *msg_id);
```

## 4. Get the text of the message with options

```c
const char* multi_i18n_get_option_text(const char *msg_id, size_t idx);
```

## 5. Get the current locale

```c
const char* multi_i18n_get_current_locale(void);
```

## 6. Macros for getting text

These macros provide a shorter way to get translated text:

- `_(text)`: Get translated text for the given message ID
- `_o(text, idx)`: Get translated option text for the given message ID and index
