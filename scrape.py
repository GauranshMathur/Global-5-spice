import requests

def download_json(agency_name, base_url, params):
    page = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    print(f"trying to access{base_url}" )
    while True:
        params['page'] = page
        print(f"getting {base_url}{params}")
        response = requests.get(base_url, params=params, headers=headers)
        if page == 10:
            break
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code}")
            break
        data = response.json()
        if not data:
            print("No more data to fetch.")
            break
        if data:
            print("")
        with open(f"./data/{agency_name}_data_page_{page}.json", 'w', encoding="utf-8") as file:
            file.write(response.text)
        print(f"Downloaded page {page}")
        page += 1   

# Base URL without the query parameters
base_url = "https://ask.gov.sg/"

# Initial query parameters
params = {
    "_data": "routes/$agencyCode/index"
}

with open('./data/agencies.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Strip newline characters and print the agency name
        agency_name = line.strip()
        agency_base_url = base_url + agency_name
        download_json(agency_name, agency_base_url, params)
