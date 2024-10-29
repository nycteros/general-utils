import requests
from bs4 import BeautifulSoup
import re

url = "https://pinterest.com/pin/998039967415759325/"

def scrape_pinterest_video(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:",e)
        return None
    except requests.exceptions.RequestException as e:
        print("Error:",e)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    video_url = None
    for script in soup.find_all("script", {"type": "application/ld+json"}):
        script_content = script.string
        if script_content and '"contentUrl"' in script_content:
            match = re.search(r'"contentUrl":"(https:[^"]+)"', script_content)
            if match:
                video_url = match.group(1)
                break

    if video_url:
        return video_url
    else:
        return 'n/a'

if __name__ == "__main__":
    
    result = scrape_pinterest_video(url)
    if result:
        if result == 'n/a':
            print("No video URL found in the provided link")
        else:
            print("Video URL found:", result)
    else:
        print("Something went wrong")

#                                   888           d88P  .d8888b. 
#                                   888          d88P  d88P  Y88b
#                                   888         d88P        .d88P
#        88888b.  888  888  .d8888b 888888     d88P        8888" 
#        888 "88b 888  888 d88P"    888        Y88b         "Y8b.
#        888  888 888  888 888      888         Y88b   888    888
#        888  888 Y88b 888 Y88b.    Y88b.        Y88b  Y88b  d88P
#        888  888  "Y88888  "Y8888P  "Y888        Y88b  "Y8888P" 
#                      888                                       
#                 Y8b d88P                                       
#                  "Y88P"                                        
