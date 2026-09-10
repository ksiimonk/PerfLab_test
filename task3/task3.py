import sys
import json


def fill_values(data, values):
    if isinstance(data, dict):

        if "id" in data and data["id"] in values:
            data["value"] = values[data["id"]]

        if "values" in data:
            fill_values(data["values"], values)

    elif isinstance(data, list):

        for item in data:
            fill_values(item, values)


def main():
    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    report_file = sys.argv[3]

    with open(tests_file, "r", encoding="utf-8") as file:
        tests = json.load(file)

    with open(values_file, "r", encoding="utf-8") as file:
        values_data = json.load(file)

    values = {
        item["id"]: item["value"]
        for item in values_data["values"]
    }

    fill_values(tests, values)

    with open(report_file, "w", encoding="utf-8") as file:
        json.dump(
            tests,
            file,
            ensure_ascii=False,
            indent=2
        )


if __name__ == "__main__":
    main()