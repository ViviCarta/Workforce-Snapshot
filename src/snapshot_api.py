import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_workforce_data():
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise Exception(f"API Request Failed: {response.status_code}")
    return response.json()

def generate_snapshot_report(data):
    report_lines = ["Workforce Snapshot Report", "-------------------------"]
    for user in data:
        name = user.get("name")
        email = user.get("email")
        company = user.get("company", {}).get("name")
        report_lines.append(f"Employee: {name}")
        report_lines.append(f"Email: {email}")
        report_lines.append(f"Company: {company}")
        report_lines.append("")
    return "\n".join(report_lines)

if __name__ == "__main__":
    data = fetch_workforce_data()
    report = generate_snapshot_report(data)
    with open("../output/example_report.txt", "w") as f:
        f.write(report)
    print(report)
