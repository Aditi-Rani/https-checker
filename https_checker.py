import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def check_https(url):
    if not url.startswith("https://"):
        print(f"❌ The website {url} is not using HTTPS.")
        return

    print(f"✅ The website {url} is using HTTPS.\n")

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        resources = soup.find_all(["link", "script", "img"])
        insecure_resources = []

        for tag in resources:
            src = tag.get("src") or tag.get("href")
            if src and src.startswith("http://"):
                full_url = urljoin(url, src)
                insecure_resources.append(full_url)

        if insecure_resources:
            print("⚠️ Found external resources served over HTTP:")
            for resource in insecure_resources:
                print(f"  - {resource}")
        else:
            print("🎉 All resources are loaded over HTTPS.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch the page: {e}")

if __name__ == "__main__":
    url = input("Enter the website URL (e.g., https://example.com): ").strip()
    check_https(url)
