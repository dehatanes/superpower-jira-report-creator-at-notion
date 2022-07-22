import os
import requests

NOTION_API_TOKEN = os.environ.get("NOTION_API_KEY")
NOTION_DATABASE_ID = os.environ.get("NOTION_DATABASE_ID")
NOTION_BASE_URL = os.environ.get("NOTION_BASE_URL")
NOTION_TEMPLATE_PAGE_ID = os.environ.get("NOTION_TEMPLATE_PAGE_ID")
notion_api_base_path = 'https://api.notion.com/v1'
notion_api_version = '2022-06-28'


def get_database_properties() -> dict:
    endpoint = f"{notion_api_base_path}/databases/{NOTION_DATABASE_ID}"
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Notion-Version': notion_api_version,
    }
    resp = requests.get(endpoint, headers=headers)
    # todo -> handle request errors
    return resp.json()

def get_page(page_id: str) -> list:
    endpoint = f"{notion_api_base_path}/pages/{page_id}"
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Notion-Version': notion_api_version,
        'Content-Type': 'application/json',
    }
    resp = requests.get(endpoint, headers=headers)
    # todo -> handle request errors
    return resp.json()

def get_template_content() -> list:
    endpoint = f"{notion_api_base_path}/blocks/{NOTION_TEMPLATE_PAGE_ID}/children"
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Notion-Version': notion_api_version,
        'Content-Type': 'application/json',
    }
    resp = requests.get(endpoint, headers=headers)
    children = resp.json().get("results")
    # todo -> handle request errors
    return children


def get_page_content(page_id: str) -> list:
    endpoint = f"{notion_api_base_path}/blocks/{page_id}/children"
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Notion-Version': notion_api_version,
        'Content-Type': 'application/json',
    }
    resp = requests.get(endpoint, headers=headers)
    children = resp.json().get("results")
    # todo -> handle request errors
    return children


def create_new_page_in_db(page_properties: dict, page_children: list) -> dict:
    endpoint = f"{notion_api_base_path}/pages"
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Notion-Version': notion_api_version,
        'Content-Type': 'application/json',
    }
    body = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": page_properties,
        "children": page_children
    }
    resp = requests.post(endpoint, json=body, headers=headers)
    # todo -> handle request errors
    return resp.json()


if __name__ == '__main__':
    # Just used to test requests in dev env
    from .utils import beauty_print
    response = get_database_properties()
    beauty_print(response)
