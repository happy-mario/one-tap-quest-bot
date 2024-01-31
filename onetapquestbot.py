#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui

def find_and_click_color(target_color, tolerance= 17, interval=1, click_delay=9):
    # Set the path to your chromedriver executable
    chromedriver_path = '/Users/mariotedeschi/Downloads/chromedriver-mac-arm64 3/chromedriver'
    
    # Configure ChromeOptions with the executable_path
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome_options.add_argument(f"chromedriver_path={chromedriver_path}")
    
    # Initialize the Chrome WebDriver with ChromeOptions
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://shimage.net/one-tap-quest/") 
    driver.maximize_window()
    # Wait for the website to load (adjust the sleep duration based on your website's loading time)
    time.sleep(5)  # 5 seconds delay as an example; adjust as needed
    
    while True:
        
        # Search for the target color in the captured screen
        screen = pyautogui.screenshot(region=(0, 365, 655, 540))
        screen.save('/Users/mariotedeschi/Desktop/dumb_screen_shot/slimy_goober.png')
        screen_width, screen_height = screen.size

        print("Screenshot taken")
        
        # Variable to track whether a click has been made in the current iteration
        click_made = False

        for x in range(screen_width):
            for y in range(screen_height):  # Limit y value to 830
                pixel_color = screen.getpixel((x, y))

                # Check if the pixel color matches the target color with increased tolerance
                if all(abs(a - b) <= tolerance for a, b in zip(pixel_color, target_color)):
                    # Click on the center of the matched region using selenium
                    if not click_made:
                        element = driver.find_element(By.XPATH, '//body')
                        element.send_keys(Keys.HOME)
                        pyautogui.click(x, y+365)
                        print("Clicked at", x, y)
                        click_made = True  # Set the flag to true 

                        # Wait for click_delay seconds before the next click
                        time.sleep(click_delay)

                        # Click again after the delay
                        element.send_keys(Keys.HOME)
                        pyautogui.click(x, y+365)
                        print("Clicked again at", x, y)
                        
                        # Break out of the inner loop after the second click
                        break

                # Check if a click was made, if not, continue to the next iteration
                if not click_made:
                    continue
        
        print("Color detection loop executed")

        # Wait for the next iteration
        time.sleep(interval)

# Example usage
target_color = (127, 73, 9)  # RGB value of the new target color
interval = 1  # Set the interval to 1 second
click_delay = 9  # Set the click delay to 9 seconds
find_and_click_color(target_color, interval=interval, click_delay=click_delay)


# In[ ]:




