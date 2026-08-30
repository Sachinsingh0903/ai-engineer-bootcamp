import requests

url = "https://api.github.com/repos/Sachinsingh0903/ai-engineer-bootcamp"

try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)
    print("Response type:", response.headers.get("Content-Type"))

    response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

    data = response.json()
    print(f"Response type: {type(data)}")
    #print("API Response:", data)  # Print a specific field from the JSON response
    print("Repository Name:", data["name"])  # Print a specific field from the JSON response
    print("Repository Description:", data["description"])  # Print another specific field from the JSON response  
    print("API Response:", data["stargazers_count"])  # Print another specific field from the JSON response
    print("Repository Forks:", data["forks_count"])  # Print another specific field from the JSON response
    print("Default Branch:", data["default_branch"])  # Print another specific field from the JSON response

except requests.RequestException as error:
    print(f"Request Failed: {error}")