import asyncio
from time import sleep
import httpx
from django.http import HttpResponse


# Função assíncrona
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get('https://httpbin.org')
        print(r)


# View assíncrona
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking HTTP request')


# Função síncrona
def http_sync_view():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get('https://httpbin.org')
    print(r)


# View Síncrona
def sync_view(request):
    http_sync_view()
    return HttpResponse('Blocking HTTP request')
