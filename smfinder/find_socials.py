from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# Time Taken
# Worst Case - 40s
# Best Case - 25s

def find_socials(name):

  SEARCH_NAME = name
  MAX_RESULTS = 5
  MAX_TRIES = 3

  insta_list = []
  linkedin_list = []
  facebook_list = []
  twitter_list = []

  s = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=s)


  # INSTAGRAM

  try:
    driver.get("https://instagram.com")
    sleep(1)

    login_form =  driver.find_element_by_id("loginForm")
    username = login_form.find_element_by_css_selector("input[type=\"text\"]")
    password = login_form.find_element_by_css_selector("input[type=\"password\"]")
    submit = login_form.find_element_by_css_selector("button[type=\"submit\"]")
    username.send_keys("sm.finder")
    password.send_keys("smfinder69")
    submit.click()
    sleep(4)

    search_inp = driver.find_element_by_css_selector("input[placeholder=\"Search\"]")
    search_inp.send_keys(SEARCH_NAME)
    sleep(1)

    id_list_elem = driver.find_element_by_css_selector("div.yPP5B div._01UL2 div.fuqBx")
    id_list = id_list_elem.find_elements_by_css_selector("a.-qQT3")
    img = driver.find_elements_by_css_selector("img._6q-tv[data-testid=\"user-avatar\"]")


    for i in range(MAX_RESULTS):
      iid = id_list[i]
      user = iid.find_element_by_css_selector("div._7UhW9.xLCgt.qyrsm.KV-D4.uL8Hv")
      name = iid.find_element_by_css_selector("div._7UhW9.xLCgt.MMzan._0PwGv.fDxYl")
      insta_list.append([img[i].get_attribute("src"), name.text, user.text, iid.get_attribute("href")])

    sleep(1)
  
  except Exception:
    pass


  # LINKEDIN

  try:

    for j in range(MAX_TRIES):
      try:
        driver.get("https://www.linkedin.com/")
        sleep(1)

        driver.find_elements_by_css_selector("span.top-nav-link__label-text")[1].click()
        sleep(1)
        search_inp = driver.find_element_by_css_selector("input[name=\"firstName\"]")
        search_inp.send_keys(SEARCH_NAME)
        search_inp.send_keys(Keys.ENTER)

        links = driver.find_elements_by_css_selector("a.base-card.base-card--link.base-search-card.base-search-card--link.people-search-card")
        image = driver.find_elements_by_css_selector("div.search-entity-media img.artdeco-entity-image")

        for i in range(MAX_RESULTS):
          link = links[i]
          name = link.find_element_by_css_selector("h3.base-search-card__title")
          loc = link.find_element_by_css_selector("p.people-search-card__location")
          linkedin_list.append([image[i].get_attribute("src"), name.text, loc.text, link.get_attribute("href")])

        break
      except Exception as e:
        print(e)
        print("\nTriying again\n")
        sleep(2)


    # Facebook

    driver.get("https://www.facebook.com")
    sleep(1)

    username_inp = driver.find_element_by_id("email")
    password_inp = driver.find_element_by_id("pass")
    login_button = driver.find_element_by_css_selector("button[type=\"submit\"]")
    username_inp.send_keys("smfinder.contact@gmail.com")
    password_inp.send_keys("smfinder69")
    login_button.click()
    sleep(4)

    for j in range(MAX_TRIES):
      try:
        serach_inp = driver.find_element_by_css_selector("input[placeholder=\"Search Facebook\"]")
        serach_inp.send_keys(SEARCH_NAME)
        serach_inp.send_keys(Keys.ENTER)
        sleep(1)

        people_div = driver.find_element_by_css_selector("div[role=\"article\"]")
        id_list_link = people_div.find_elements_by_css_selector("a[role=\"link\"]")
        # img = people_div.find_element_by_css_selector("svg.pzggbiyp[role=\"img\"] image")

        for i in range(MAX_RESULTS):
          id_link = id_list_link[i]
          facebook_list.append([id_link.get_attribute("aria-label"), 0, id_link.get_attribute("href")])
        break
      except Exception as e:
        print(e)
        print("\nTriying again\n")
        sleep(2)
  except Exception:
    pass

  # twitter

  try:
    driver.get(f"https://twitter.com/search?q={SEARCH_NAME.replace(' ', '%20')}&src=typed_query&f=user")
    sleep(2)

    main_sec = driver.find_element_by_css_selector("section[role=\"region\"].css-1dbjc4n")

    name_list = main_sec.find_elements_by_css_selector("div.css-1dbjc4n.r-1wbh5a2.r-dnmrzs span span")
    user_list = main_sec.find_elements_by_css_selector("div.css-1dbjc4n.r-18u37iz.r-1wbh5a2 span")
    img = main_sec.find_elements_by_css_selector("img.css-9pa8cd")

    for i in range(MAX_RESULTS):
      twitter_list.append([img[i].get_attribute("src"), name_list[i].text, user_list[i].text, 0])
  except Exception:
    pass
  sleep(1)
  driver.close()


  ans = {'instagram': [], 'facebook': [], 'linkedin': [], 'twitter': []}

  for i in range(MAX_RESULTS):
    if insta_list:
      x = insta_list[i]
      ans["instagram"].append({'dp': x[0], 'det': [x[1], x[2], x[3]]})

  for i in range(MAX_RESULTS):
    if (facebook_list):
      x = facebook_list[i]
      ans["facebook"].append({'dp': 0, 'det': [x[0], x[1], x[2]]})

  for i in range(MAX_RESULTS):
    if linkedin_list:
      x = linkedin_list[i]
      ans["linkedin"].append({'dp': x[0], 'det': [x[1], x[2], x[3]]})

  for i in range(MAX_RESULTS):
    if twitter_list:
      x = twitter_list[i]
      ans["twitter"].append({'dp': x[0], 'det': [x[1], x[2], x[3]]})

  return ans

