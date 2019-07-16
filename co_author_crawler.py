from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import researchGate_id


def add_to_set(set, name):
    set.append(name)


def add_to_edges(set, name1, name2):
    set.append((name1, name2))


def crawler(browser, urls, nodes1, nodes2, edges, k=1):
    browser.get('https://www.researchgate.net/login')
    browser.find_element_by_id('input-login').send_keys(researchGate_id.user)
    browser.find_element_by_id('input-password').send_keys(researchGate_id.password)
    browser.find_element_by_class_name("nova-c-button__label").find_element(By.XPATH, "./..").click()
    browser.implicitly_wait(5)

    for url in urls:
        try:
            browser.get(url)
            browser.implicitly_wait(5)
            temp_name = url.split("/")[4]
            add_to_set(nodes1, temp_name)
            try:
                browser.find_element_by_xpath(
                    '//*[@id="content"]/div/div[4]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[2]/button').click()
                browser.implicitly_wait(5)
                for i in range(1, 51):
                    i = str(i)
                    try:
                        if browser.find_element_by_xpath(
                                '/html/body/div[4]/span/div/div[2]/div/div[2]/div[2]/div/ul/li[' + i + ']/div/div').get_attribute(
                            'class') == 'nova-l-flex__item nova-l-flex nova-l-flex--gutter-xs nova-l-flex--direction-row@s-up nova-l-flex--align-items-stretch@s-up nova-l-flex--justify-content-flex-start@s-up nova-l-flex--wrap-nowrap@s-up':
                            temp = browser.find_element_by_xpath(
                                '/html/body/div[4]/span/div/div[2]/div/div[2]/div[2]/div/ul/li[' + i + ']/div/div/div[2]/div/div/div/div/div/a').get_attribute(
                                'href')
                            temp_co = temp.split("/")[4].split("?")[0]
                            add_to_edges(edges, temp_name, temp_co)
                            if browser.find_element_by_xpath(
                                    '/html/body/div[4]/span/div/div[2]/div/div[2]/div[2]/div/ul/li[' + i + ']/div/div/div[2]/div/div/div/div/ul/li[3]/span').text == 'XXXXXXXXXX':
                                add_to_set(nodes1, temp_co)
                            else:
                                add_to_set(nodes2, temp_co)
                        else:
                            break
                    except:
                        NoSuchElementException
            except:
                pass
        except:
            pass
        print(k)
        k += 1
