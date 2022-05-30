import requests
import json


APIKey = "KZUnqVPCNcIMB5QjFoYCFzlNC"
APIKeySecret = "SUPusochNvzaaPeY4NHocaaHS5vnD7fHO840X4TBzgT0g8fv1r"
BearerToken = "AAAAAAAAAAAAAAAAAAAAAFygbAEAAAAA1log034O9FEfOB%2Fk9uma0QmP9K4%3DCigwVqJgG2FsXcIb5eFKykGNDUkCOi8DmqaLEcg9FHq0Wv56VQ"
AccessToken = "1174342365911207938-LVttzOSiHD9mnXHZkOmy8Ntg6hBsBv"
AccessTokenSecret = "VZcUA9NsxSJy4Bz1MAurDB4ulBZz87X4eXwPTQXi9nRrc"



def create_url():
    # Replace with user ID below
    user_id = 2244994945
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)

def get_params():
    return {"tweet.fields": "author_id"}

def bearer_oauth(r):

    r.headers["Authorization"] = f"Bearer {BearerToken}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()