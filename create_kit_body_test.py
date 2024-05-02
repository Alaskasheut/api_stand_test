import sender_stand_request
import data

#----------------------------------------GET USER----------------------------------------
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

# ----------------------------------------GET USER TOKEN----------------------------------------
def get_new_user_token():
    user_body = get_user_body("Alma")
    user_response = sender_stand_request.post_new_user(user_body)
    return user_response.json()['authToken']


#----------------------------------------GET NEW KIT NAME----------------------------------------
def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body


#--------------------------------POSITIVE ASSERT IN CREATE KIT {NAME}----------------------------
def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    auth_Token=get_new_user_token()
    kit_response = sender_stand_request.post_create_new_client_kit(kit_body,auth_Token)

    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_body['name']

#--------------------------------NEGATIVE ASSERT IN CREATE KIT {NAME}----------------------------
def negative_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    auth_Token = get_new_user_token()
    kit_response = sender_stand_request.post_create_new_client_kit(kit_body, auth_Token)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def negative_assert_no_parameter():
    kit_body=data.kit_body_empty.copy()
    auth_Token = get_new_user_token()
    kit_response = sender_stand_request.post_create_new_client_kit(kit_body, auth_Token)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400



#---------------------------------TEST CASES IN CREATE A KIT {NAME}------------------------------

#Test 1
#One character accepted in file:name
#def test_create_kit_1_letter_in_name_get_success_response():
#    positive_assert("A")

#Test 2
#511 characters accepted in file:name
#def test_create_kit_511_letter_in_name_get_success_response():
#    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Test 3
# Name field empty
#def test_create_kit_empty_in_name_get_error_response():
#    negative_assert("")

#Test 4
#512 characters accepted in file:name
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Test 5
#Special characters rejected in name field
def test_create_kit_special_characters_in_name_get_error_response():
    positive_assert("№%@,")


#Test 6
#Spaces are accepted in Name field
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert("A Aaa ")

#Test 7
#Numbers are accepted in Name field
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

#Test 8
#The Parameter do not passe to request
def test_create_kit_no_parameter_in_name_get_error_response():
    negative_assert_no_parameter()

#Test 9
#It has been passed a different parameter in the field name
def test_create_kit_different_parameter_in_name_get_error_response():
    negative_assert(123)
