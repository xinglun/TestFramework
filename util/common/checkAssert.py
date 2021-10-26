import logging
import allure

def check_assert(data,validate):
    equals = True
    contains =True
    # equals
    for key,value in validate["equals"].items():
        print("equals:",key,value)
        if data["data"] != None and type(data["data"]) is dict:
            if data.get(key) != value and data["data"].get(key) != value:
                equals = False
        else:
            if data.get(key) != value:
                equals = False
    # contains
    if validate["contains"] != None:
        for i in validate["contains"]:
            print("contains:",i)
            if data["data"] != None and type(data["data"]) is dict:
                if i not in data and i not in data["data"]:
                    contains = False
            else:
                if i not in data:
                    equals = False
    # logs
    with allure.step("ASSERT"):
        allure.attach("validate equals", str(validate["equals"]))
        allure.attach("validate contains", str(validate["contains"]))
        allure.attach("response", str(data))
        if equals == False:
            allure.attach("equals assert", "FAILED")
        elif contains == False:
            allure.attach("contains assert", "FAILED")
        else:
            allure.attach("assert", "PASSED")
    return equals and contains 
    



