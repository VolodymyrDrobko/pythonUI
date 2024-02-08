import json

PATH = "C:\\*\\PycharmProjects\\newProject\\utils\\resources\\"
TEST_DATA_JSON = "test_user.json"


def get_json(file_name):
    path = f"{PATH}\\{file_name}"
    with open(path, 'r') as file:
        user = json.load(file)
        return user


def read(file_name, key: str) -> str:
    path = f"{PATH}\\{file_name}"
    with open(path, 'r') as file:
        text = file.read()
        user = json.loads(text)
        return user[key]


def write(file_name, key: str, value: str):
    path = f"{PATH}\\{file_name}"
    user = get_json(file_name)
    with open(path, 'w') as file:
        user[key] = value
        file.write(json.dumps(user, indent=2))


def update_password(password: str) -> None:
    old_password = read(TEST_DATA_JSON, "password")
    write(TEST_DATA_JSON, "old_password", old_password)
    write(TEST_DATA_JSON, "password", password)


