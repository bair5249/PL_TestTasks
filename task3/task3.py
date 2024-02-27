import json


def change_value(template_test, values):
    if template_test['value'] != "":
        return template_test, values
    for id, value in values:
        if "value" in template_test and template_test["id"] == id:
            template_test["value"] = value
    return template_test, values


def check_values(template_test, values):
    if type(template_test) is not list:
        if "value" in template_test.keys():
            template_test, values = change_value(template_test, values)
        if "values" in template_test.keys():
            template_test["values"], values = check_values(template_test["values"], values)
    else:
        for i, iword in enumerate(template_test):
            template_test[i], values = check_values(iword, values)

    return template_test, values


def links(values, tests, report):
    lst = []
    with open(values, "r") as f:
        templates_values = json.load(f)["values"]

    with open(tests, "r") as f:
        templates_tests = json.load(f)

    values = []
    for template_value in templates_values:
        values.append([template_value["id"], template_value["value"]])

    del f, templates_values, tests

    for template_test in templates_tests["tests"]:
        template_test, values = check_values(template_test, values)
        lst.append(template_test)

    with open(report, "w") as file:
        json.dump({"tests": lst}, file, indent=2, ensure_ascii=False)


def main():
    links("values.json", "tests.json", "report.json")


if __name__ == "__main__":
    main()
