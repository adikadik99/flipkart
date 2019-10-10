from appium import webdriver
import base64
import os
import time

desired_cap = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app": "/Users/adik/Downloads/flipkart.apk",
    "appPackage": "com.flipkart.android",
    "appWaitActivity": "com.flipkart.android.activity.MSignupActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

driver.start_recording_screen()

driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()

driver.implicitly_wait(30)

driver.find_element_by_id("com.flipkart.android:id/search_widget_textbox").click()


search_element = driver.find_element_by_id("com.flipkart.android:id/search_autoCompleteTextView")
driver.set_value(search_element, "Iphone")


driver.execute_script('mobile:performEditorAction', {'action':'search'})
driver.implicitly_wait(120)

driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()
driver.implicitly_wait(60)
driver.find_element_by_xpath("//android.widget.TextView[@bounds='[459,544][556,582]']").click()
driver.implicitly_wait(60)
driver.find_element_by_xpath("//android.widget.TextView[@bounds='[45,1694][354,1794]']").click()
driver.implicitly_wait(60)
driver.find_element_by_id("com.flipkart.android:id/txt_btn_add_to_cart").click()
driver.implicitly_wait(60)
driver.find_element_by_xpath("//android.view.View[@bounds='[630,1653][1063,1779]']").click()

ts = (time.strftime("%Y_%m_%d_%H%M%S"))
activityname = driver.current_activity
filename = activityname+ts

driver.save_screenshot("/Users/adik/Desktop/" + filename + ".png")



video_rawdata = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

filepath = os.path.join("/Users/adik/Desktop/", video_name + ".mp4")
with open(filepath, "wb") as vd:
    vd.write(base64.b64decode(video_rawdata))
