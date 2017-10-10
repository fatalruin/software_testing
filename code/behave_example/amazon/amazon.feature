Feature: we can check for our product on the front page

  Scenario: look for a blender
     Given we have opened amazon
      when we search for "camera"
       and scrape the search results
      then we will find a "canon" product in the top "10" results
       and we will close the browser

  Scenario: look for a blender
     Given we have opened amazon
      when we search for "blender"
       and scrape the search results
      then we will find a "ninja" product in the top "5" results
       and we will close the browser