import json
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://nardisjazz.com/")
driver.implicitly_wait(30)
time.sleep(5)

evcal_list = driver.find_element(by=By.ID, value="evcal_list")
children = evcal_list.get_property("children")

def replace_text(string):
    rep = ["\n\t\t\t\t\t", "<strong>","\xa0", "&quot;"]
    for e in rep:
        string = string.replace(e,"")
    string = string.replace("- scroll down for English   ","\",\"lineup\":\"")
    string = string.split("</strong>")[0] + "\"}"
    return string

dict_list = []
for e in children:
    string = e.get_property("textContent")
    string2 = replace_text(string)
    try:
        child_dict = json.loads(string2)
        dict_list.append(child_dict)
    except:
        print(dict_list[-1]["name"])
        print(string2)

event_list = []
for e in dict_list:
    event_dict = {}
    event_dict["date"] = e["startDate"].split("T")[0]
    event_dict["time"] = e["startDate"].split("T")[1].split("+")[0]
    event_dict["name"] = e["name"].title()
    event_dict["lineup"] = e["lineup"]
    event_dict["url"] = e["url"]
    event_list.append(event_dict)

event_df = pd.DataFrame()
for e in event_list:
    event_df = pd.concat([event_df,pd.DataFrame([e])], ignore_index=True)
event_df["date"] = pd.to_datetime(event_df["date"])
event_df.to_excel('nardis.xlsx')