from playwright.sync_api import Page #импортирует класс Page из playwright
import config  #импортирует созданный нами config


class IndexPage:  #создает класс IndexPage

    def open_index_page(self, page: Page) -> None:  #создает метод, который и является необходимым нам шагом
        page.goto(config.url.DOMAIN)