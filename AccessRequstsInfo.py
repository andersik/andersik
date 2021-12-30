import pip._vendor.requests
import json

url = "https://ogeprod.api.identitynow.com/oauth/token"

payload='grant_type=client_credentials&client_id=c217c828d8b94c4d8d359e6f2f74e759&client_secret=bd74ba183ce44303b3d9a8aa9f0c4b686d78d3df9321c1d7c30dc3cd364c2663'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = pip._vendor.requests.request("POST", url, headers=headers, data=payload)
jsonResponse = response.json()

#print(jsonResponse["access_token"])

identityUrl = "https://ogeprod.api.identitynow.com/v2/identities/00045420"
payload={}
authenticatedHeader = {
  'Authorization': 'Bearer ' + jsonResponse["access_token"]
}
response = pip._vendor.requests.request("GET", identityUrl, headers=authenticatedHeader, data=payload)
jsonIdentityResponse = response.json()

#print(jsonIdentityResponse)

accessRequestUrl = "https://ogeprod.api.identitynow.com/beta/access-request-status?regarding-identity=" + jsonIdentityResponse["externalId"]
response = pip._vendor.requests.request("GET",accessRequestUrl, headers=authenticatedHeader, data=payload)
jsonAccessRequest = response.json()

#print(jsonAccessRequest)

for item in jsonAccessRequest:
    print(item["name"])

#print(response.text.access_token)