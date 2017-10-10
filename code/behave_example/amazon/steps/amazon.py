from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


@given(u'we have opened amazon')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://www.amazon.com")
    assert "Amazon" in context.browser.title

@when(u'we search for "{target}"')
def step_impl(context, target):
    assert "Amazon" in context.browser.title
    input_element = context.browser.find_element_by_id('twotabsearchtextbox')   
    assert input_element != None
    input_element.clear()
    input_element.send_keys(target)
    input_element.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Amazon" in context.browser.title

@when(u'scrape the search results')
def step_impl(context):
    assert "Amazon" in context.browser.title
    search_list = context.browser.find_element_by_id("s-results-list-atf")
    assert search_list != None
    search_items = search_list.find_elements_by_tag_name("li")
    assert type(search_items) is list
    assert len(search_items) >= 1
    search_titles = []
    for item in search_items:
        headers = item.find_elements_by_tag_name("h2")
        if len(headers) == 1:
            search_titles.append(headers[0].text)
    context.search_titles = search_titles

@then(u'we will find a "{vendor}" product in the results')
def step_impl(context,vendor):
    for result in context.search_titles[0:10]:
        if vendor in result.lower():
            print("SUCCESS! WE WILL DOMINATE THE BLENDER WORLD!")
            return
    assert False

@then(u'we will find a "{vendor}" product in the top "{n}" results')
def step_impl(context,vendor,n):
    n = int(n)
    for result in context.search_titles[0:n]:
        if vendor in result.lower():
            print("SUCCESS! WE WILL DOMINATE THE BLENDER WORLD!")
            return
    assert False

@then(u'we will close the browser')
def step_impl(context):
    context.browser.close()
