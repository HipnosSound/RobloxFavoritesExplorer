# app/api.py

from __future__ import annotations

import requests

from app.settings import REQUEST_TIMEOUT


class RobloxAPI:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": "RobloxFavoritesExplorer"
        })

    def get(self, url, **kwargs):

        response = self.session.get(
            url,
            timeout=REQUEST_TIMEOUT,
            **kwargs
        )

        response.raise_for_status()

        return response.json()

    def post(self, url, json):

        response = self.session.post(
            url,
            json=json,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()
