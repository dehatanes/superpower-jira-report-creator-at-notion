from report_creator.utils import get_formatted_date_for_today
from .notion_adapter import (
    get_database_properties,
    get_template_content,
    create_new_page_in_db,
    NOTION_BASE_URL
)


def main():
    print()
    print("JIRA<>NOTION - REPORT GENERATOR 2000")
    print("--------------------------------------------")
    print()
    print("Aguarde um instante... criando página...")

    properties_schema = get_properties_schema()
    template_content = get_template_content()
    new_page_properties, new_page_children = generate_page_properties(properties_schema, template_content)       
    # print(f'{new_page_properties}')
    new_page_id = create_page(new_page_properties, new_page_children)

    print()
    print('--------------------------------------------')
    print('Página criada com sucesso!')
    print(f'Você pode visitá-la aqui: {NOTION_BASE_URL}/{"".join(new_page_id.split("-"))}')


def get_properties_schema() -> dict:
    resp = get_database_properties()
    return resp.get('properties')


def create_page(properties: dict, page_children: list) -> str:
    resp = create_new_page_in_db(properties, page_children)
    print(f'{resp}')
    return resp.get('id')


def get_prop_value(prop_name: str, prop: dict):
    # Todo: handle values selection
    prop_type = prop['type']
    if prop_type == "title":
        date = get_formatted_date_for_today(formatter="%d.%m.%Y")
        return [{"text": {"content": f'[{date}] Sprint Report'}}]
    elif prop_type == "date":
        today = get_formatted_date_for_today(formatter="%Y-%m-%d")
        return {"start": today}
    elif prop_type == "multi_select":
        options = [choice['name'] for choice in prop["multi_select"]["options"]]
        resp = input(f"Insira os valores de '{prop_name}' separados por vírgula.\n[Valores aceitos:{options}]: ")
        return [{"name": chosen_tag} for chosen_tag in resp.split(",")]
    elif prop_type == "select":
        options = [choice['name'] for choice in prop["select"]["options"]]
        resp = input(f"Insira o valore de '{prop_name}'.\n[Valores aceitos:{options}]: ")
        return {"name": resp}

def get_child_value(prop_child_type: str, child_prop: dict) -> dict:
    block = { "object": "block"}
    block['type'] = prop_child_type
    block[prop_child_type] = child_prop[prop_child_type]
    return block

def generate_page_properties(properties_schema: dict, get_page_content: dict) -> (dict, list):
    properties = {
        prop['id']: {prop['type']: get_prop_value(name, prop)}
        for name, prop in properties_schema.items() if get_prop_value(name, prop)
    }
    properties_children = []
    for child in get_page_content:
        if child['type'] != 'image':
            properties_children.append(get_child_value(child['type'], child))
    return properties,properties_children

main()
