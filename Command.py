import SendBeatsCollector
import json


def main():
    url = SendBeatsCollector.create_url()
    params = SendBeatsCollector.get_params()
    json_response = SendBeatsCollector.connect_to_endpoint(url, params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()