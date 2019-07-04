from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

try:
    import Queue as queue
except:
    import queue


class co_author_crawlers():

    browser=webdriver.Chrome()

    def get_name_and_urls(self, url):
        ca = {}
        self.browser.get(url)
        self.browser.implicitly_wait(5)

        for i in range(1, 6):
            try:
                i = str(i)
                name = self.browser.find_element_by_xpath(
                    '//*[@id="content"]/div/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[2]/ul/li[' + i + ']/div/div/div[2]/div/div/div/div/div/a').text
                url = self.browser.find_element_by_xpath(
                    '//*[@id="content"]/div/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[2]/ul/li[' + i + ']/div/div/div[2]/div/div/div/div/div/a').get_attribute(
                    'href')
                ca[name] = url
            except:
                NoSuchElementException

        return ca

    def get_nodes_and_edges(self, dict, root, nodes, edges):
        for key in dict.keys():
            nodes.append(key)
            edges.append((root, key))

    def process(self, name_url_pair, nodes, edges):
        for key, value in name_url_pair.items():
            co_author = co_author_crawlers.get_name_and_urls(co_author_crawlers(), value)
            co_author_crawlers.get_nodes_and_edges(co_author_crawlers(), co_author, key, nodes, edges)
        return co_author

