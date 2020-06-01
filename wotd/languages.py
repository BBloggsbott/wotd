class Language:
    def __init__(self, name, code, site, transparent_language_endpoint=None):
        self.name = name
        self.code = code
        self.site = site
        self.transparent_language_endpoint = transparent_language_endpoint

    def __str__(self):
        return "{} {}".format(self.name, self.code)

    def __eq__(self, x):
        if type(self) == type(x):
            return self.code == x.code
        elif type(x) == str:
            return self.code == x
        else:
            raise TypeError("'=' not supported for {} and {}".format(type(x), type(self)))


TRANSPARENT_LANGUAGE = "transparent_language"
MERRIAM_WEBSTER = "merriam-webster"

SOURCES = (
    MERRIAM_WEBSTER,
    TRANSPARENT_LANGUAGE
    )

ARABIC = Language("Arabic", "ar", (TRANSPARENT_LANGUAGE), "modern-standard-arabic-word-of-the-day&x=1")
BALINESE = Language("Balinese", "ban", (TRANSPARENT_LANGUAGE), "balinesewordoftheday&x=1")
CHINESE = Language("Chinese", "zh", (TRANSPARENT_LANGUAGE), "mandarin-chinese-word-of-the-day&x=1")
DUTCH = Language("Dutch", "nl", (TRANSPARENT_LANGUAGE), "dutch-word-of-the-day&x=1")
ENGLISH = Language("English", "en", (MERRIAM_WEBSTER))
ESPERANTO = Language("Esperanto", "eo", (TRANSPARENT_LANGUAGE), "esperanto-word-of-the-day&x=1")
FRENCH = Language("French", "fr", (TRANSPARENT_LANGUAGE), "french-word-of-the-day&x=1")
GERMAN = Language("German", "de", (TRANSPARENT_LANGUAGE), "german-word-of-the-day&x=1")
HEBREW = Language("Hebrew", "he", (TRANSPARENT_LANGUAGE), "hebrew-word-of-the-day&x=1")
HINDI = Language("Hindi", "hi", (TRANSPARENT_LANGUAGE), "hindi-word-of-the-day&x=1")
INDONESIAN = Language("Indonesian", "id", (TRANSPARENT_LANGUAGE), "indonesian-word-of-the-day&x=1")
IRISH = Language("Irish", "ga", (TRANSPARENT_LANGUAGE), "irish-word-of-the-day&x=1")
ITALIAN = Language("Italian", "it", (TRANSPARENT_LANGUAGE), "italian-word-of-the-day&x=1")
JAPANESE = Language("Japanese", "ja", (TRANSPARENT_LANGUAGE), "japanese-word-of-the-day&x=1")
KOREAN = Language("Korean", "ko", (TRANSPARENT_LANGUAGE), "korean-word-of-the-day&x=1")
LATIN = Language("Latin", "ls", (TRANSPARENT_LANGUAGE), "latin-word-of-the-day&x=1")
NORWEGIAN = Language("Norwegian", "no", (TRANSPARENT_LANGUAGE), "norwegian-word-of-the-day&x=1")
PASHTO = Language("Pashto", "ps", (TRANSPARENT_LANGUAGE), "pashto-word-of-the-day&x=1")
POLISH = Language("Polish", "pl", (TRANSPARENT_LANGUAGE), "polish-word-of-the-day&x=1")
PORTUGUESE = Language("Brazilian Portuguese", "pt", (TRANSPARENT_LANGUAGE), "brazilian-portuguese-word-of-the-day&x=1")
RUSSIAN = Language("Russian", "ru", (TRANSPARENT_LANGUAGE), "russian-word-of-the-day&x=1")
SPANISH = Language("Spanish", "es", (TRANSPARENT_LANGUAGE), "spanish-word-of-the-day&x=1")
SWEDISH = Language("Swedish", "sv", (TRANSPARENT_LANGUAGE), "swedish-word-of-the-day&x=1")
TURKISH = Language("Turkish", "tr", (TRANSPARENT_LANGUAGE), "turkish-word-of-the-day&x=1")
URDU = Language("Urdu", "ur", (TRANSPARENT_LANGUAGE), "urdu-word-of-the-day&x=1")

LANGUAGES = (
    ARABIC,
    BALINESE,
    CHINESE,
    DUTCH,
    ENGLISH,
    ESPERANTO,
    FRENCH,
    GERMAN,
    HEBREW,
    HINDI,
    INDONESIAN,
    IRISH,
    ITALIAN,
    JAPANESE,
    KOREAN,
    LATIN,
    NORWEGIAN,
    PASHTO,
    PORTUGUESE,
    POLISH,
    RUSSIAN,
    SPANISH,
    SWEDISH,
    TURKISH,
    URDU
)

