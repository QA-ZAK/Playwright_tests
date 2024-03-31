from config.url import Url #импортирует класс Url, который мы написали в модуле url.py.
from config.playwright import Playwright
from config.expectations import Expectations

url = Url()  #создает переменную, значением которой является экземпляр класса Url.
playwright = Playwright()
expectations = Expectations()