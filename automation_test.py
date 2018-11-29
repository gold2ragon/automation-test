# my skype : makswgnr

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("D:\\DevTools\\Chrome Driver\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://signup.insly.com/signup")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id("broker_name").send_keys("Veronika Personal Company")
driver.find_element_by_id("broker_address_country").send_keys("United States Of America")
driver.find_element_by_id("broker_tag").send_keys("veronikapersonalcompany")
driver.find_element_by_id("prop_company_profile").send_keys("Software Development Company")
driver.find_element_by_id("prop_company_no_employees").send_keys("6-10")
driver.find_element_by_id("prop_company_person_description").send_keys("I am the CEO of the company")

driver.find_element_by_id("broker_admin_email").send_keys("veronkiaB@workemail.com")
driver.find_element_by_id("broker_admin_name").send_keys("Veronika B")
driver.find_element_by_id("broker_person_password").send_keys("abcde12345")
driver.find_element_by_id("broker_person_password_repeat").send_keys("abcde12345")
driver.find_element_by_id("broker_admin_phone").send_keys(" 669-221-6251")

checkboxes = driver.find_element_by_class_name("checklist").find_elements_by_class_name("icon-check-empty")
checkboxes[0].click()
checkboxes[1].click()
checkboxes[2].click()

links = driver.find_element_by_class_name("checklist").find_elements_by_tag_name("a")
links[1].click()

policyDiv = driver.find_element_by_class_name("privacy-policy-dialog").find_element_by_tag_name("div").find_elements_by_tag_name("div")[1]
actions = ActionChains(driver)
actions.move_to_element(policyDiv).perform()

# closeButton = driver.find_element_by_class_name("ui-dialog-titlebar-close").find_elements_by_tag_name("span")
closeButton = driver.find_elements_by_class_name("icon-close")[1]
closeButton.click()

driver.find_element_by_id("submit_save").click()

# driver.quit()