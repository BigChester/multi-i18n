#include <unity.h>
#include <stdio.h>
#include "multi_i18n.h"

void setUp(void)
{
    printf("Running setUp...\n");
    __multi_i18n_reset();
}

void tearDown(void)
{
}

void test_init_with_null_should_fail(void)
{
    printf("Testing null initialization...\n");
    TEST_ASSERT_EQUAL(MULTI_I18N_FAIL, multi_i18n_init(NULL));
}

void test_generated_language_pack(void)
{
    printf("Testing language pack existence...\n");

    // 检查语言包数组是否存在
    printf("Checking if language pack array exists...\n");
    TEST_ASSERT_NOT_NULL(multi_i18n_language_pack);
    printf("Language pack array exists at %p\n", (void *)multi_i18n_language_pack);

    // 检查第一个元素
    printf("Checking first language pack element...\n");
    const multi_i18n_language_t *first_lang = multi_i18n_language_pack[0];
    TEST_ASSERT_NOT_NULL(first_lang);
    printf("First language exists at %p\n", (void *)first_lang);

    // 检查第一个语言的 locale
    printf("Checking first language locale...\n");
    TEST_ASSERT_NOT_NULL(first_lang->locale);
    printf("First language locale: %s\n", first_lang->locale);

    // 检查第一个语言的翻译数组
    printf("Checking first language translations...\n");
    TEST_ASSERT_NOT_NULL(first_lang->singulars);
    printf("First language translations exist at %p\n", (void *)first_lang->singulars);

    // 检查第一个翻译
    printf("Checking first translation...\n");
    const multi_i18n_phrase_t *first_phrase = first_lang->singulars;
    TEST_ASSERT_NOT_NULL(first_phrase->msg_id);
    TEST_ASSERT_NOT_NULL(first_phrase->translation);
    printf("First translation: %s -> %s\n", first_phrase->msg_id, first_phrase->translation);

    // 计数语言包
    printf("Counting language packs...\n");
    size_t count = 0;
    while (multi_i18n_language_pack[count] != NULL)
    {
        printf("Found language %d: %s\n", count, multi_i18n_language_pack[count]->locale);
        count++;
    }
    printf("Total languages found: %d\n", (int)count);
    TEST_ASSERT_TRUE(count > 0);
}

void test_generated_translations(void)
{
    printf("Testing translations...\n");

    // 初始化语言包
    printf("Initializing language pack...\n");
    const multi_i18n_language_pack_t *lang_pack = multi_i18n_language_pack;
    TEST_ASSERT_EQUAL(MULTI_I18N_SUCCESS, multi_i18n_init(lang_pack));
    printf("Language pack initialized\n");

    // 获取当前语言
    printf("Getting current locale...\n");
    const char *current_locale = multi_i18n_get_current_locale();
    printf("Current locale: %s\n", current_locale ? current_locale : "NULL");
    TEST_ASSERT_NOT_NULL(current_locale);

    // 尝试获取翻译
    printf("Testing translation...\n");
    if (multi_i18n_language_pack[0] && multi_i18n_language_pack[0]->singulars)
    {
        const char *first_msg_id = multi_i18n_language_pack[0]->singulars[0].msg_id;
        printf("First message ID: %s\n", first_msg_id);
        const char *result = multi_i18n_get_text(first_msg_id);
        printf("Translation result: %s\n", result ? result : "NULL");
        TEST_ASSERT_NOT_NULL(result);
    }
    else
    {
        printf("No translations available in first language\n");
    }
}

int main(void)
{
    printf("Starting tests...\n");
    UNITY_BEGIN();

    printf("\nRunning test_init_with_null_should_fail...\n");
    RUN_TEST(test_init_with_null_should_fail);

    printf("\nRunning test_generated_language_pack...\n");
    RUN_TEST(test_generated_language_pack);

    printf("\nRunning test_generated_translations...\n");
    RUN_TEST(test_generated_translations);

    return UNITY_END();
}