import requests
import json
def nfmp_rest_query_auth():
  url_auth = "https://172.29.12.25/rest-gateway/rest/api/v1/auth/token"

  payload="{\n\"grant_type\":\"client_credentials\"\n}\n\n  \n\n\n             "
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46Tm9raWFOc3AxIQ=='
  }

  response_auth = requests.request("POST", url_auth, headers=headers, data=payload,verify=False)
  return response_auth.json()['access_token']

def nfmp_query_vprn_list(arg):
  url = "https://172.29.12.26:8443/nfm-p/rest/api/v1/managedobjects/searchWithFilter"

  payload = "{\r\n  \"resultFilter\": [\r\n    \"ServiceId\",\"objectFullName\",\"id\"\r\n  ],\r\n  \"fullClassName\": \"vprn.Vprn\"\r\n}"
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + arg
    }

  response = requests.request("POST", url, headers=headers, data=payload, verify=False)

  return(response.json())


if __name__ == "__main__":
  key = nfmp_rest_query_auth()
  list = nfmp_query_vprn_list(key)
  print(list)
  print(list[0]['objectFullName'])