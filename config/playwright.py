import os


class Playwright:
    PAGE_VIEWPORT_SIZE = {'width': 1920, 'height': 1080} #задает размеры окна браузера
    ENV = os.getenv('ENV') if os.getenv('ENV') is not None else 'stage'
    BROWSER = os.getenv('BROWSER') if os.getenv('BROWSER') is not None else 'chrome' #отвечает за то,
    # в каком браузере будут выполняться автотесты
    IS_HEADLESS = os.getenv('HEADLESS') if os.getenv('HEADLESS') is not None else False
    SLOW_MO = int(os.getenv('SLOW_MO')) if os.getenv('SLOW_MO') is not None else 50
    LOCALE = 'en-US' #задает языковые настройки для браузера, выставляя их на английский язык