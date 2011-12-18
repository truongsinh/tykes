from django.conf import settings

#FAIL_SILENTLY = getattr(settings, 'MULTILINGUAL_FAIL_SILENTLY', not settings.DEBUG)
FAIL_SILENTLY = True
DEFAULT_LANGUAGE = getattr(settings, 'MULTILINGUAL_LANGUAGE_CODE', settings.LANGUAGE_CODE)
#FALL_BACK_TO_DEFAULT = getattr(settings, 'MULTILINGUAL_FALL_BACK_TO_DEFAULT', True)
#FALL_BACK_TO_DEFAULT 0 return defect object, 1 return in object in default language, 2 do not return
FALL_BACK_TO_DEFAULT = 1
LANGUAGES = getattr(settings, 'MULTILINGUAL_LANGUAGES', settings.LANGUAGES)
AUTO_HIDE_LANGUAGE = getattr(settings, 'MULTILINGUAL_AUTO_HIDE_LANGUAGE', len(LANGUAGES) == 1)
