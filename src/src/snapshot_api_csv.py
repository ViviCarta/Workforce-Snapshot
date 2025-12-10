import requests, csv

API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_workforce_data():
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise Exception(f"API Request Failed: {response.status_code}")
    return response.json()

def export_to_csv(data, filename="../output/workforce_snapshot.csv"):
    fields = ["Employee Name", "Email", "Company"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        for user in data:
            writer.writerow([
                user.get("name"),
                user.get("email"),
                user.get("company", {}).get("name")
            ])
    print("CSV exported:", filename)

if __name__ == "__main__":
    data = fetch_workforce_data()
    export_to_csv(data)
