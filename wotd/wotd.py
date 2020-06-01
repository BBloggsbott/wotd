import yaml
import sys
from pathlib import Path
from termcolor import colored

import colorama

from languages import LANGUAGES, SOURCES, ENGLISH, Language, MERRIAM_WEBSTER, TRANSPARENT_LANGUAGE
from scrappers import get_from_transparent_language, get_from_merriam_webster, WORD_KEY, MEANING_KEY, POS_KEY, EXAMPLE_KEY, EXAMPLE_EN_KEY

CONFIG_LANG = "lang"
CONFIG_OUTPUT_PATTERN = "output_pattern"
CONFIG_WORD_COLOR = "word_color"
CONFIG_MEANING_COLOR = "meaning_color"
CONFIG_POS_COLOR = "pos_color"
CONFIG_FILENAME = ".wotd.config"

PATTERN_WORD = "[wotd_word]"
PATTERN_MEANING = "[wotd_meaning]"
PATTERN_POS = "[wotd_pos]"
PATTERN_EXAMPLE = "[wotd_example]"
PATTERN_EXAMPLE_EN = "[wotd_example_en]"

DEFAULT_LANG = ENGLISH.code
DEFAULT_PATTERN = "{} | {} | {} | {} | {}".format(PATTERN_WORD, PATTERN_MEANING, PATTERN_POS, PATTERN_EXAMPLE, PATTERN_EXAMPLE_EN)
DEFAULT_WORD_COLOR = "green"
DEFAULT_MEANING_COLOR = "yellow"
DEFAULT_POS_COLOR = "red"
DEFAULT_CONFIG = {
    CONFIG_LANG: DEFAULT_LANG,
    CONFIG_OUTPUT_PATTERN: DEFAULT_PATTERN,
    CONFIG_WORD_COLOR: DEFAULT_WORD_COLOR,
    CONFIG_MEANING_COLOR: DEFAULT_MEANING_COLOR,
    CONFIG_POS_COLOR: DEFAULT_POS_COLOR
}

class WOTDConfig:
    def __init__(self, config_file :Path):
        self.config_file = str(config_file)
        if not config_file.exists():
            print("Config file doesn't exist. Using defaults")
            self.write_default_config()
            config = {}
        else:
            config_stream = open(self.config_file, "r")
            try:
                config = yaml.load(config_stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as err:
                print("Error with config file for wotd. Using defaults")
                config_stream.close()
                config = {}
        self.lang = config.get(CONFIG_LANG, DEFAULT_LANG)
        self.output_pattern = config.get(CONFIG_OUTPUT_PATTERN, DEFAULT_PATTERN)
        self.word_color = config.get(CONFIG_WORD_COLOR, DEFAULT_WORD_COLOR)
        self.meaning_color = config.get(CONFIG_MEANING_COLOR, DEFAULT_MEANING_COLOR)
        self.pos_color = config.get(CONFIG_POS_COLOR, DEFAULT_POS_COLOR)

        if ENGLISH == self.lang:
            self.modify_pattern_for_en()

    def write_default_config(self):
        config_stream = open(self.config_file, "w")
        yaml.dump(DEFAULT_CONFIG, config_stream)
        config_stream.close()

    def modify_pattern_for_en(self):
        self.output_pattern = self.output_pattern.replace(PATTERN_EXAMPLE_EN, "")

def get_word_from_site(lang :Language, source :str):
    if source == TRANSPARENT_LANGUAGE:
        return get_from_transparent_language(lang)
    elif source == MERRIAM_WEBSTER:
        return get_from_merriam_webster(lang)

def str_from_pattern(config: WOTDConfig, word: dict):
    word_string = config.output_pattern.replace(PATTERN_WORD, colored(word[WORD_KEY], config.word_color))
    word_string = word_string.replace(PATTERN_MEANING, colored(word[MEANING_KEY], config.meaning_color))
    word_string = word_string.replace(PATTERN_POS, colored(word[POS_KEY], config.pos_color))
    word_string = word_string.replace(PATTERN_EXAMPLE, word[EXAMPLE_KEY])
    word_string = word_string.replace(PATTERN_EXAMPLE_EN, word.get(EXAMPLE_EN_KEY, ""))
    return word_string

def main():
    colorama.init()
    home = Path.home()
    config_file = home / CONFIG_FILENAME
    wotd_config = WOTDConfig(config_file)
    langs = list(filter(lambda x: x == wotd_config.lang, LANGUAGES))
    word = None
    if len(langs) == 0:
        print("Requested language {} not found".format(wotd_config.lang))
        sys.exit(1)
    for source in SOURCES:
        if source in langs[0].site:
            word = get_word_from_site(langs[0], source)
            break
    
    if word is not None:
        print(str_from_pattern(wotd_config, word))
    else:
        print("Error getting Word of the day")
        sys.exit(1)

