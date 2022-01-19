from selenium import webdriver
import time


def main():
    start_timer_secs = 60 * 4
    desired_remaining_secs = 60 * (1.15)

    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.sporcle.com/games/RobPro/1-100-click-me')

    # Wait for me to login
    input('Press ENTER once you have logged in')

    start_btn = driver.find_element_by_link_text('PLAY QUIZ')
    start_btn.click()

    if desired_remaining_secs > 0:
        time.sleep((start_timer_secs - desired_remaining_secs) - 10)

    for i in range(100):
        driver.find_element_by_id(f'slot{i}').click()


if __name__ == "__main__":
    main()
