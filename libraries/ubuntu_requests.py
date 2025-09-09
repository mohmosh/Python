import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Prompt user for an image URL
    url = input("Enter the image URL: ").strip()

    # Create directory for fetched images
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Try fetching the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises HTTPError for bad responses

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image saved successfully at: {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ The request timed out.")
    except Exception as err:
        print(f"❌ An unexpected error occurred: {err}")

if __name__ == "__main__":
    fetch_image()
