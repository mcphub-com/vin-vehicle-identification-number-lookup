import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/digital-insights-digital-insights-default/api/vin-vehicle-identification-number-lookup'

mcp = FastMCP('vin-vehicle-identification-number-lookup')

@mcp.tool()
def search_vin_vin_vin(vin: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Enter the Vehicle Identification Number for Search'''
    url = 'https://vin-vehicle-identification-number-lookup.p.rapidapi.com/search_vin'
    headers = {'x-rapidapi-host': 'vin-vehicle-identification-number-lookup.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vin': vin,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
