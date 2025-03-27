from urllib.parse import urlparse

import uvicorn
from fastapi import FastAPI, HTTPException
from waybackpy import WaybackMachineSaveAPI, WaybackMachineCDXServerAPI

app = FastAPI()

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"


def is_valid_url(url: str) -> bool:
    """Check if the URL is valid based on its scheme and network location."""
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)


@app.get("/archive")
async def get_archive_url(url: str):
    """
    Archive the provided URL using the Wayback Machine API and return the archived URL.

    If the URL is not valid, a 400 error is returned.
    """
    if not is_valid_url(url):
        raise HTTPException(status_code=400, detail="Invalid URL provided")

    try:
        # Get the newest archive if available
        cdx_api = WaybackMachineCDXServerAPI(url, USER_AGENT)
        archive = cdx_api.newest()

        # If no archive is found, save a new one
        if not archive:
            save_api = WaybackMachineSaveAPI(url, USER_AGENT)
            archive = save_api.save()

        return {"archive": archive}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=15414, reload=True)
