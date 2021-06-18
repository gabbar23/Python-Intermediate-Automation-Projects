import requests
from datetime import datetime

today=datetime.now()

#creating-a-user
CREATE_USER_ENDPOINT=" https://pixe.la/v1/users"
USERNAME="gabbar23"
TOKEN="hQpo9Oit6Yg69JHreHUS6GUG7"
create_user_para={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#
# response=requests.post(url=CREATE_USER_ENDPOINT,json=create_user_para)
# print(response.text)

#creating-a-graph
GRAPH_ENDPOINT=(f"{CREATE_USER_ENDPOINT}/{USERNAME}/graphs")
# GRAPH_UPDATE=(f"{CREATE_USER_ENDPOINT}/{USERNAME}/graphs/gabbargraph1")
graph_pra={
    "id":"gabbargraph1",
    "name":"Coding Graph",
    "unit":"hour",
    "type":"int",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}
# graph_response=requests.put(url=GRAPH_UPDATE,json=graph_pra,headers=headers)
# print(graph_response.text)


# Post-a-Pixel

PIXEL_ENDPOINT=(f"{CREATE_USER_ENDPOINT}/{USERNAME}/graphs/gabbargraph1")
pixel_para={
    "date":today.strftime("%Y%m%d"),
    'quantity':"2"
}
header_pixels={
    "X-USER-TOKEN":TOKEN
}
# pixel_response=requests.post(url=PIXEL_ENDPOINT,json=pixel_para,headers=header_pixels)
# print(pixel_response.text)



# update_para={
#     'quantity':"6"
# }
# update_endpoint=(f"{CREATE_USER_ENDPOINT}/{USERNAME}/graphs/gabbargraph1/{today.strftime('%Y%m%d')}")
# pixel_response=requests.put(url=update_endpoint,json=update_para,headers=header_pixels)
# print(pixel_response.text)


# delete_endpoint=(f"{CREATE_USER_ENDPOINT}/{USERNAME}/graphs/gabbargraph1/20210616")
# delete_pixel=requests.delete(url=delete_endpoint,headers=header_pixels)
# print(delete_pixel.text)