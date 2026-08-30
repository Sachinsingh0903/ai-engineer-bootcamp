import requests

url="https://api.github.com"

try:
    response = requests.get(url,timeout=10)

    print("Status Code:", response.status_code)
    print("Response type:", response.headers.get("Content-Type"))

    response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

    data=response.json()
    print(f"Response type: {type(data)}")
    print("API Response:", data["current_user_url"])  # Print a specific field from the JSON response
    print("API Response:", data["current_user_authorizations_html_url"])  # Print another specific field from the JSON response

except requests.RequestException as error:
    print(f"Request Failed: {error}")

