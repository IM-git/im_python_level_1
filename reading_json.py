import json


class ReadingJson:

    @staticmethod
    def read_file(way: str):
        with open(way) as text:
            data = json.load(text)
        return data


if __name__ == '__main__':
    PATH = "config.json"
    json_file = ReadingJson.read_file(PATH)
    print(json_file)
    print(json_file["browser"])
    print(json_file["singleton"])
