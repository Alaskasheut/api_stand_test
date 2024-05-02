import requests
import configuration
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USER_TABLE_PATH)

response = get_users_table()
print(response.status_code)
print(response.url)