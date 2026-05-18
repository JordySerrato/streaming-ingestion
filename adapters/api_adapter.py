import requests

class APIAdapter:

    def fetch_data(
        self,
        url,
        chunk_size=None
    ):

        response = requests.get(url)

        data = response.json()

        chunk = []

        for item in data:

            chunk.append((
                item["id"],
                item["name"],
                item["email"],
                item["address"]["city"]
            ))

            if len(chunk) == chunk_size:

                yield chunk

                chunk = []

        if chunk:
            yield chunk