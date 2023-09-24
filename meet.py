from __init__ import *
from run import name, url

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, ElementNotInteractableException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from random import randint



"https://meet.google.com/etf-abah-ximyyy"
'https://meet.google.com/zyf-yqur-oam'
"51.159.24.172"

runs = 0

def join():

    options = Options()
    options.add_argument("--incognito")
    # options.add_argument("--headless")

    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_experimental_option("useAutomationExtension", False)

    options.page_load_strategy = 'eager'
    service = Service(executable_path="/Users/dark/Downloads/geckodriver")
    driver = webdriver.Edge(options=options, service=service)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    wait = WebDriverWait(driver, timeout=30)

    driver.get(url)
    sleep(15)

    if "Something went wrong" in driver.title:
        print('This meeting link is invalid.')
        driver.quit()


    def starter():
        try:
            text_box = driver.find_element(By.CSS_SELECTOR, "#c13")
            chosen_name = str(name[randint(0, len(name))]['names']).capitalize()
            text_box.send_keys(chosen_name)

            first_join_button = driver.find_element(By.CSS_SELECTOR, "body > c-wiz > div > div > div:nth-child(14) > div.crqnQb > div > div.gAGjv > div.vgJExf > div > div > div.d7iDfe.NONs6c > div.shTJQe > div.jtn8y > div.XCoPyb > div:nth-child(1) > button > span")
            wait.until(EC.element_to_be_clickable(first_join_button)).click()
            sleep(3)
            return True

            # email_box = driver.find_element(By.NAME, "inputemail")
            # second_join_button = driver.find_element(By.ID, "joinBtn")
            # email = re.sub('[\s+]', '', name) + str(randint(1, 100000)) + '@yev.me'
            # email_box.send_keys(email)
            # second_join_button.click()
            # sleep(3)

            # third_join_btn = driver.find_element(By.CLASS_NAME, "preview-join-button")
            # wait.until(EC.element_to_be_clickable(third_join_btn)).click()
            # sleep(10)
            
        except NoSuchElementException:
            return False


    def recorder():
        try:
            rec_pop = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div/div/button[1]")
            wait.until(EC.element_to_be_clickable(rec_pop)).click()
            return True

        except:
            return False


    def disable_audio_video1():
        try:
            disable_video_btn = driver.find_element(By.CSS_SELECTOR, "body > c-wiz > div > div > div:nth-child(14) > div.crqnQb > div > div.gAGjv > div.vgJExf > div > div > div.ZUpb4c > div.oORaUb.XDitY.NONs6c > div > div.EhAUAc > div.GOH7Zb > div > div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.M9Bg4d.OGbUle.FTMc0c.N2RpBe.jY9Dbb > div.I5fjHe.wb61gb")
            wait.until(EC.element_to_be_clickable(disable_video_btn)).click()

            sleep(1)

            mute_audio_btn = driver.find_element(By.CSS_SELECTOR, "body > c-wiz > div > div > div:nth-child(14) > div.crqnQb > div > div.gAGjv > div.vgJExf > div > div > div.ZUpb4c > div.oORaUb.XDitY.NONs6c > div > div.EhAUAc > div.ZB88ed > div > div > div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.M9Bg4d.OGbUle.FTMc0c.N2RpBe.jY9Dbb > div.I5fjHe.wb61gb")
            wait.until(EC.element_to_be_clickable(mute_audio_btn)).click()
            return True

        except:
            return False
    

    def disable_audio_video2():
        try:
            disable_btn = driver.find_element(By.CSS_SELECTOR, "#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.Qb2h6b.xInSQ.PBbOsf.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.VlHPz > div > div:nth-child(2) > button > span")
            wait.until(EC.element_to_be_clickable(disable_btn)).click()
            return True
        
        except:
            return False
    

    def leave():
        try:
            leave_button = driver.find_element(By.CSS_SELECTOR, "#foot-bar > div.footer__leave-btn-container > button")
            wait.until(EC.element_to_be_clickable(leave_button)).click()
            
            confirm_leave_button = driver.find_element(By.CSS_SELECTOR, "#wc-footer > div.footer__inner.leave-option-container > div:nth-child(2) > div > div > button")
            wait.until(EC.element_to_be_clickable(confirm_leave_button)).click()
            return True
        
        except:
            return False
    
    
    try:
        disabled = disable_audio_video2()
        if not disabled:
            print("Dangerous!")
            exit("Exiting")
        else:
            start = starter()
            if not start:
                exit("Internal error occured")
            else:
                # is_recorded = recorder()
                # if is_recorded:
                #     print("Meeting is being recorded")
                # else:
                #     print("Meeting not recorded")
                # sleep(5)

                # joined_audio = audio()
                # if joined_audio:
                #     print("Connected to audio")
                # else:
                #     print("Not connected to audio")
                # sleep(1)

                print('Joined meeting')
                # sleep(11000)
                sleep(180)

                left = leave()
                if left:
                    print("Participant meeting timeout is reached.")
                    sleep(1)
                    driver.quit()
                    print("Respawning in 5 seconds...\n")
                    sleep(5)
                else:
                    driver.quit()
                    print("Respawning in 5 seconds...\n")
                    sleep(5)

    except NoSuchElementException:
        print('Error! Please check your internet connection')
        sleep(1)
        driver.quit()
        print("Retrying in 5 seconds...\n")
        sleep(5)

    
    finally:
        clear(command=clear_arg)
        global runs
        runs += 1
        # print(f"Runs are {runs}")
        if runs == 3:
            exit("Runtime completed.")
        return join()


join()


