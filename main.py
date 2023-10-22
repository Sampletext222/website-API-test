import requests
from datetime import date

BASE_URL = 'https://leecare.barossavillage.org/platinum5/'
LOGIN_URL = BASE_URL # Update with the actual login endpoint
REPORT_REQUEST_URL = BASE_URL + 'ltcapp/ltcservice'  # This seems to be where GWT RPC requests are sent, but verify it

HEADERS = {
    'Referer': BASE_URL,
    'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# I'm assuming the login payload remains the same as the one in the previous example
LOGIN_PAYLOAD = {
    'username': 'julians',
    'password': 'Torres23!'
}

def generate_report_payload(year, month, day):
    # This function takes the date and returns the payload with that date inserted
    # Adjust this to fit the exact structure of the payload if needed
    base_payload = "...|15|{year}|{month}|{day}|0|9|0|..."
    return base_payload.format(year=year, month=month, day=day)

def fetch_report_for_date(year, month, day):
    with requests.Session() as session:
        # Logging in
        response = session.post(LOGIN_URL, data=LOGIN_PAYLOAD, headers=HEADERS)
        if response.status_code == 200:
            print("Successfully logged in!")
        else:
            print("Failed to log in.")
            return

        # Generating the report request payload with the desired date
        payload = generate_report_payload(year, month, day)

        # Fetching the report
        report_response = session.post(REPORT_REQUEST_URL, data=payload, headers=HEADERS)
        return report_response.text  # or whatever processing you need

# Example usage
year, month, day = date.today().year, date.today().month, date.today().day
report_data = fetch_report_for_date(year, month, day)
print(report_data)
