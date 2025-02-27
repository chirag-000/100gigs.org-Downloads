import requests
import re

def extract_data():
    # URL of the JavaScript file containing all the content's links
    url = "https://100gigs.org/_nuxt/DuFK2s2m.js"

    try:
        # Fetch the JavaScript file content
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch the URL. Status code: {response.status_code}")
            return

        # Store the raw content of the response (JavaScript code)
        js_content = response.text

        # Write the extracted data to a text file
        with open("download_links.txt", "w", encoding="utf-8") as f:
            f.write("=== 100gigs.org ===" + "\n" * 3)

            # Find all instances where relative_path and download_url appear in the original order
            combined_pattern = r'relative_path:"([^"]+)".*?download_url:"([^"]+)"'
            combined_matches = re.findall(combined_pattern, js_content, re.DOTALL)

            for i, (path, url) in enumerate(combined_matches, 1):
                f.write(f"{i}.\t {path}\n {"\t" * 3} URL: {url}\n\n")

        print(f"Successfully extracted {len(combined_matches)} download URLs.")
        print("Data has been written to 'download_links.txt'")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    extract_data()
