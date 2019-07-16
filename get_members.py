from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import researchGate_id


def get_memebers_url(f, browser, curr_page):
    browser.get('https://www.researchgate.net/login')
    browser.find_element_by_id('input-login').send_keys(researchGate_id.user)
    browser.find_element_by_id('input-password').send_keys(researchGate_id.password)
    browser.find_element_by_class_name("nova-c-button__label").find_element(By.XPATH, "./..").click()
    browser.implicitly_wait(5)

    browser.get(curr_page)
    browser.implicitly_wait(5)

    try:
        last_page = int(browser.find_elements_by_class_name('navi-page-link')[-1].text.strip())
    except:
        last_page = 1

    page_num = 1

    while page_num <= last_page:
        for i in range(1, 26):
            i = str(i)
            try:
                name = browser.find_element_by_xpath(
                    '/html/body/div/div[2]/div/div/div[4]/div/div/div/div/ul/li[' + i + ']/div[3]/h5/a').text
                url = browser.find_element_by_xpath(
                    '/html/body/div/div[2]/div/div/div[4]/div/div/div/div/ul/li[' + i + ']/div[3]/h5/a').get_attribute(
                    'href')
                f.writelines(url + '\n')
            except:
                NoSuchElementException
        page_num += 1
        curr_page = curr_page.split("=")[0] + "=" + str(page_num)
        browser.implicitly_wait(5)
        browser.get(curr_page)


if __name__ == '__main__':
    browser = webdriver.Chrome()
    f = open('XXXXXXX', 'w', encoding='utf-8-sig')
    curr_page = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    get_memebers_url(f, browser, curr_page)
