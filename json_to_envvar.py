import json

with open("newman/newman-run-report-2019-12-17-08-04-31-542-0.json") as jsonfile:
    payload = json.loads(jsonfile.read())
    data = payload["run"]["stats"]
    print(data)

    total_iterations = data["iterations"]["total"]
    total_items = data["items"]["total"]
    total_requests = data["requests"]["total"]
    total_scripts = data["scripts"]["total"]

    failed_iterations = data["iterations"]["failed"]
    failed_items = data["items"]["failed"]
    failed_requests = data["requests"]["failed"]
    failed_scripts = data["scripts"]["failed"]

    with open("newman_envvar", "w") as envfile:
        envfile.write("total_iterations=%s\n" % total_iterations)
        envfile.write("total_items=%s\n" % total_items)
        envfile.write("total_requests=%s\n" % total_requests)
        envfile.write("total_scripts=%s\n" % total_scripts)

        envfile.write("failed_iterations=%s\n" % failed_iterations)
        envfile.write("failed_items=%s\n" % failed_items)
        envfile.write("failed_requests=%s\n" % failed_requests)
        envfile.write("failed_scripts=%s\n" % failed_scripts)
