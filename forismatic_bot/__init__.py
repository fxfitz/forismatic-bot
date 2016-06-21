import json
import os

import requests

WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')
if WEBHOOK_URL is None:
    msg = 'SLACK_WEBHOOK_URL is a required environment variable.'
    raise RuntimeError(msg)

USERNAME = os.getenv('SLACK_USERNAME', 'Smart Guy')
ICON_URL = os.getenv('SLACK_ICON_URL', ('http://images.zap2it.com/assets/'
                                        'p184431_n78810_cc_v4_aa/'
                                        'smart-guy.jpg'))


def get_quote():
    url = 'http://api.forismatic.com/api/1.0/'
    payload = {
        'method': 'getQuote',
        'format': 'json',
        'lang': 'en'
    }

    response = requests.get(url, params=payload)
    return (response.json()['quoteText'], response.json()['quoteAuthor'])


def post_slack():
    quote, author = get_quote()
    if author == '':
        author = 'Unknown'

    payload = json.dumps({
        'text': '"{}" -- {}'.format(quote, author),
        'username': USERNAME,
        'icon_url': ICON_URL
    })

    requests.post(WEBHOOK_URL, data=payload)
