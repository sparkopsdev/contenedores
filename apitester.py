import json
from typing import Any, Dict, Optional

import requests

from src.config import settings


def get_base_url() -> str:
    """
    Returns the base URL of the API, using the external server and port
    defined in the global settings.
    """
    server = settings.apiExternalServer
    port = settings.apiExternalPort
    baseURL = f"http://{server}:{port}"
    return baseURL


def pretty_print_response(response: requests.Response) -> None:
    """
    Prints HTTP status and JSON/text body in a readable format.
    """
    print(f"Status: {response.status_code}")
    try:
        data = response.json()
        print("Response JSON:")
        print(json.dumps(data, indent=2))
    except ValueError:
        if response.text:
            print("Response text:")
            print(response.text)
        else:
            print("No content.")


def call_list_persons() -> None:
    """
    Calls GET /person.
    """
    url = f"{get_base_url()}/person"
    print(f"\n=== GET {url} ===")
    response = requests.get(url)
    pretty_print_response(response)


def call_get_person(person_id: int) -> None:
    """
    Calls GET /person/{id}.
    """
    url = f"{get_base_url()}/person/{person_id}"
    print(f"\n=== GET {url} ===")
    response = requests.get(url)
    pretty_print_response(response)


def call_create_person(
    first_name: str,
    last_name: str,
    dni: str,
    birth_province: str,
) -> Optional[int]:
    """
    Calls POST /person and returns the created person's ID if successful.
    """
    url = f"{get_base_url()}/person"
    payload: Dict[str, Any] = {
        "firstName": first_name,
        "lastName": last_name,
        "dni": dni,
        "birthProvince": birth_province,
    }

    print(f"\n=== POST {url} ===")
    print("Payload:")
    print(json.dumps(payload, indent=2))

    response = requests.post(url, json=payload)
    pretty_print_response(response)

    if response.ok:
        try:
            data = response.json()
            return data.get("id")
        except ValueError:
            return None
    return None


def call_delete_person(person_id: int) -> None:
    """
    Calls DELETE /person/{id}.
    """
    url = f"{get_base_url()}/person/{person_id}"
    print(f"\n=== DELETE {url} ===")
    response = requests.delete(url)
    pretty_print_response(response)


def main() -> None:
    """
    Simple API tester that sequentially calls all endpoints:
    - GET /person
    - POST /person
    - GET /person/{id}
    - DELETE /person/{id}
    - GET /person (again)
    """
    print(f"Using base URL: {get_base_url()}")

    # 1) List persons (may be empty or return your 404 "The list is empty")
    call_list_persons()

    # 2) Create a new test person
    created_id = call_create_person(
        first_name="Test",
        last_name="User",
        dni="TEST-DNI-001",
        birth_province="TestProvince",
    )

    if created_id is None:
        print("\nCould not create test person, stopping here.")
        return

    # 3) Get that person
    call_get_person(created_id)

    # 4) List again
    call_list_persons()

    # 5) Delete that person
    call_delete_person(created_id)

    # 6) Final list
    call_list_persons()


if __name__ == "__main__":
    main()
