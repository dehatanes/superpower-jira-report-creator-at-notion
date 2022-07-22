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
JIRA_CLOUD_SESSION_TOKEN = os.environ.get("JIRA_CLOUD_SESSION_TOKEN")
JiraInformationModel = namedtuple('JiraInformationModel', ['dashboard_image_url'])  # todo: add burndown_chart_image_url


def _take_screenshots(jira_workspace_name: str, dashboard_id: str) -> str:
    print('Espera mais um pouquinho... tirando screenshot do Jira...')
    temp_img_name = 'temp_dashboard_image.png'
    dashboard_url = f'https://{jira_workspace_name}.atlassian.net/jira/dashboards/{dashboard_id}'

    options = webdriver.ChromeOptions()
    options.headless = True

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get(dashboard_url)
    browser.add_cookie({"name": "cloud.session.token", "value": JIRA_CLOUD_SESSION_TOKEN})
    browser.set_window_size(1800, 1630)
    browser.get(dashboard_url)

    print('Esse trem é meio demorado...')
    time.sleep(10)

    browser.save_screenshot(temp_img_name)
    browser.quit()
    return temp_img_name


def get_jira_info() -> JiraInformationModel:
    dashboard_temp_file_name = _take_screenshots(JIRA_WORKSPACE_NAME, JIRA_DASHBOARD_ID)
    date = get_formatted_date_for_today("%Y_%m_%d")
    return JiraInformationModel(
        dashboard_image_url=upload_file(
            dashboard_temp_file_name,
            f'jira-{JIRA_WORKSPACE_NAME}/dashboard-{date}.png'
        ),
    )


if __name__ == '__main__':
    # Just used to test requests in dev env
    _take_screenshots('tokyodrift', '10001')
