from appium import webdriver
import base64
import os
import time
import unittest

class FlipkartTesting(unittest.TestCase):
     def setUp(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "app": "/Users/adik/Downloads/flipkart.apk",
            "appPackage": "com.flipkart.android",
            "appWaitActivity": "com.flipkart.android.activity.MSignupActivity"
             }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(20)
        self.driver.start_recording_screen()


     def testlogin(self):
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id("com.flipkart.android:id/mobileNo").click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id("com.flipkart.android:id/mobileNo").send_keys("4")
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id("com.flipkart.android:id/country_code_info").click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id("com.flipkart.android:id/search_country_name").send_keys("Canada")
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id("com.flipkart.android:id/country_row_item_full_name").click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id("com.flipkart.android:id/mobileNo").clear()
            self.driver.find_element_by_id("com.flipkart.android:id/mobileNo").send_keys("4169099630")   #entering phone number
            self.driver.find_element_by_id("com.flipkart.android:id/btn_mlogin").click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id("com.flipkart.android:id/et_password").click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id("com.flipkart.android:id/et_password").send_keys("adikadik")
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id("com.flipkart.android:id/btn_mlogin").click()


     def tear_down(self):
        ts = (time.strftime("%Y_%m_%d_%H%M%S"))
        activityname = self.driver.current_activity
        filename = activityname+ts
        self.driver.save_screenshot("/Users/adik/Desktop/" + filename + ".png")
        video_rawdata = self.driver.stop_recording_screen()
        video_name = self.driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")
        filepath = os.path.join("/Users/adik/Desktop/", video_name + ".mp4")
        with open(filepath, "wb") as vd:
          vd.write(base64.b64decode(video_rawdata))

if __name__== 'main':
    unittest.main()