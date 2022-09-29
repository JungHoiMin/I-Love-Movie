import os
import sys
import urllib.request
import json
from boxofficeAPI import getMoviesInfo


def lambda_handler(event, context):
    cards = getMoviesInfo()
    return {
        'version': '1.0',
        'data': 'card',
        'headers': {
            'Access-Control-Allow-Origin': '*',
        },
        'contents': [
            {
                'type': 'card.image',
                'cards': cards
            }
        ]
    }
