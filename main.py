import uvicorn

from fastapi import FastAPI, HTTPException
from urllib.parse import urlparse
from waybackpy import WaybackMachineSaveAPI, WaybackMachineCDXServerAPI


app = FastAPI()
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"

@app.get("/archive")
async def get_archive_url(url: str):
    """
    Archive the provided URL using archive.is and return the archived URL.
    If the URL is not valid, a 400 error is returned.
    """
    if not is_valid_url(url):
        raise HTTPException(status_code=400, detail="Invalid URL provided")
    try:
        # get newest archive if available
        cdx_api = WaybackMachineCDXServerAPI(url, user_agent)
        archive = cdx_api.newest()
        
        # return 
        if not archive:
            save_api = WaybackMachineSaveAPI(url, user_agent)
            archive = save_api.save()

        return {"archive": archive}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)


if __name__ == '__main__':
    # Starting the app using uvicorn
    uvicorn.run(app, host="0.0.0.0", port=15414)