import os
import time
from collections import namedtuple

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from report_creator.file_uploader import upload_file
from report_creator.utils import get_formatted_date_for_today

JIRA_WORKSPACE_NAME = os.environ.get("JIRA_WORKSPACE_NAME")
JIRA_DASHBOARD_ID = os.environ.get("JIRA_DASHBOARD_ID")
JIRA_PROJECT_ID = os.environ.get("JIRA_PROJECT_ID")
JIRA_BOARD_ID = os.environ.get("JIRA_BOARD_ID") #todo: find main board of project
JIRA_CLOUD_SESSION_TOKEN = os.environ.get("JIRA_CLOUD_SESSION_TOKEN")
JiraInformationModel = namedtuple('JiraInformationModel', ['dashboard_image_url', 'burndown_chart_image_url'])


def _take_dashboard_screenshot(jira_workspace_name: str, dashboard_id: str) -> str:
    print('Espera mais um pouquinho... tirando screenshot do Dashboard...')
    temp_img_name = 'temp_dashboard_image.png'
    dashboard_url = f'https://{jira_workspace_name}.atlassian.net/jira/dashboards/{dashboard_id}'

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--log-level=3")

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get(dashboard_url)
    browser.add_cookie({"name": "cloud.session.token", "value": JIRA_CLOUD_SESSION_TOKEN})
    browser.get(dashboard_url)
    print('Esse trem é meio demorado...')
    time.sleep(30)
    element=browser.find_element("xpath", '//div[@id="dashboard"]')
    total_height = element.size["height"]+1000
    browser.set_window_size(1800, total_height)

    print('Calma que vai...')
    time.sleep(20)

    browser.save_screenshot(temp_img_name)
    browser.quit()
    return temp_img_name

def _take_burndown_screenshot(jira_burndown_workspace_name: str, jira_project_id: str, jira_board_id: str) -> str: #todo: refact to remove coding duplicates
    print('Espera mais um pouquinho... tirando screenshot do Burndown...')
    temp_burndown_img_name = 'temp_burndown_image.png'
    burndown_url = f'https://{jira_burndown_workspace_name}.atlassian.net/jira/software/projects/{jira_project_id}/boards/{jira_board_id}/reports/burndown'

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(burndown_url)
    driver.add_cookie({"name": "cloud.session.token", "value": JIRA_CLOUD_SESSION_TOKEN})
    driver.get(burndown_url)
    print('Aguardando carregar as paradinhas...')
    time.sleep(10)
    burndown_element=driver.find_element("xpath", '//*[@id="ak-main-content"]/div')
    total_height_burndown = burndown_element.size["height"]+400
    driver.set_window_size(1800, total_height_burndown)

    print('Esse é longo que nem o outro...')
    time.sleep(10)

    driver.save_screenshot(temp_burndown_img_name)
    driver.quit()
    return temp_burndown_img_name

def get_jira_info() -> JiraInformationModel:    
    dashboard_temp_file_name = _take_dashboard_screenshot(JIRA_WORKSPACE_NAME, JIRA_DASHBOARD_ID)
    burndown_temp_file_name = _take_burndown_screenshot(JIRA_WORKSPACE_NAME, JIRA_PROJECT_ID,  JIRA_BOARD_ID)
    date = get_formatted_date_for_today("%Y_%m_%d")
    return JiraInformationModel(
        dashboard_image_url=upload_file(
            dashboard_temp_file_name,
            f'jira-{JIRA_WORKSPACE_NAME}/dashboard-{date}.png'
        ),
        burndown_chart_image_url=upload_file(
            burndown_temp_file_name,
            f'jira-{JIRA_WORKSPACE_NAME}/burndown-{date}.png'
        )
    )


if __name__ == '__main__':
    # Just used to test requests in dev env
    _take_dashboard_screenshot('tokyodrift', '10001')
    _take_burndown_screenshot('tokyodrift', 'TD', '1')
