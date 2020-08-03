from selenium import webdriver


class WebDriver:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    # returns the name of the weapon
    def get_name(self):
        return self.driver.find_element_by_xpath('//*[@id="firstHeading"]').text

    # quits the wb
    def quit(self):
        self.driver.quit()

    # returns a list of all weapon stats
    def get_info(self):
        stats = self.driver.find_element_by_class_name('stat')
        values = stats.find_elements_by_tag_name('td')
        for i in values:
            print(i.text)
        return values

    # gets the name of the weapon, clicks it.
    def choose_weapon_by_name(self, name):
        tags = self.driver.find_elements_by_tag_name('a')
        for tag in tags:
            if tag.text == name:
                tag.click()
                return
        print(f' the weapon {name} wasnt found. try again or type "pass"')
        new_name=input()
        if new_name != "pass":
            self.choose_weapon_by_name(new_name)
        else:
            return

    # Take you to the last page you visited
    def back(self):
        self.driver.back()