import asyncio
import requests
from datetime import datetime


## código roda de forma assíncrona;
def get_url(n):
    print("%s - %s" % (n, datetime.now()))
    response = requests.get('https://swapi.co/api/people/?search=?').json()


async def process(loop):
    for n in range(10):
        loop.run_in_executor(None, get_url, n)
        

loop = asyncio.get_event_loop()
loop.run_until_complete(process(loop))


# código roda de forma síncrona:
def dois():
    for n in range(10):
        future1 = requests.get('https://swapi.co/api/people/?search=?').json()
        print(n, '-', datetime.now())

dois()



