import configuration
import requests
import data

#----------------------------------------GET----------------------------------------

#def get_docs():
#    return requests.get(configuration.URL_SERVICE + configuration.DOCS_PATH)

#response = get_docs()
#print(response.status_code)
#print(response.request)

#def get_logs():
#    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

#response = get_logs()
#print(response.status_code)
#print(response.request)
#print(response.headers)


#def get_logs():
#    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
#                        params={'count':20})

#response = get_logs()
#print(response.status_code)
#print(response.request)
#print(response.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USER_TABLE_PATH)

#response = get_users_table()
#print(response.status_code)
#print(response.json())


#----------------------------------------POST----------------------------------------

#Create a new user

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,json=body,headers=data.headers)
#response=post_new_user(data.user_body)
#response = post_new_user(data.user_body)
#print(response.status_code)
#print(response.json())


#Search a kit by products

#def post_products_kits(products_kits):
#    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_kits, headers=data.headers)

#response = post_products_kits(data.product_ids)
#print(response.status_code)
#print(response.json())


#Create a new kit in an client account
def post_create_new_client_kit(kit_body,auth_Token):
    current_headers=data.headers.copy()
    current_headers['Authorization'] = "Bearer " + auth_Token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, json=kit_body,headers=current_headers
    )
#response_kit=post_create_new_client_kit(data.kit_body,response.json()["authToken"])
#print(response_kit.status_code)
#print(response_kit.json())







