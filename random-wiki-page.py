import requests
import webbrowser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--amount", default=10,
                    help="Number of articles to get")
args = parser.parse_args()


def open_wikipedia_page(title):
    wikipedia_url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
    webbrowser.open(wikipedia_url)


def get_random_wikipedia_page():
    api_url = "https://en.wikipedia.org/w/api.php"

    params = {
        'action': 'query',
        'format': 'json',
        'list': 'random',
        'rnnamespace': 0,  # Limit to main namespace (articles)
        'rnlimit': args.amount
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    for article in data['query']['random']:
        open_wikipedia_page(article["title"])


if __name__ == "__main__":
    get_random_wikipedia_page()
