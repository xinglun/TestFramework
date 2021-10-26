from util.common import readParams

# fix headers
def read_headers(data):
    headers = readParams.read_param(data['request']['headers'])
    if data['request'].get("accessToken") != None:
        accessToken = readParams.read_param(data['request']['accessToken'])
        headers = {**headers,**{'Authorization':accessToken['accessToken']}}
    if data['request'].get("firmId") != None:
        firmId = readParams.read_param(data['request']['firmId'])
        headers = {**headers,**firmId}   
    if data['request'].get("publisherId") != None:
        publisherId = readParams.read_param(data['request']['publisherId'])
        headers = {**headers,**publisherId}      
    if data['request'].get("refreshToken") != None:
        refreshToken = readParams.read_param(data['request']['refreshToken'])
        headers = {**headers,**refreshToken}
    if data['request'].get("roleId") != None:
        roleId = readParams.read_param(data['request']['roleId'])
        headers = {**headers,**roleId}
    if data['request'].get("userId") != None:
        userId = readParams.read_param(data['request']['userId'])
        headers = {**headers,**userId} 
    if data['request'].get("userName") != None:
        userName = readParams.read_param(data['request']['userName'])
        headers = {**headers,**userName}    
    return headers       

