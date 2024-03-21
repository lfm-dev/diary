import os

SETTINGS_FILE_PATH = os.path.join(os.getenv('HOME'), '.config/diary/settings.csv')

def get_settings():
    settings = {}
    with open(SETTINGS_FILE_PATH, encoding='utf-8') as settings_file:
        for line in settings_file:
            name, value = line.strip().split(',')
            settings[name] = value
    return settings

SETTINGS = get_settings()
