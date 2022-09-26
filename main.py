import aiohttp
import time
import asyncio

URL = 'https://pokeapi.co/api/v2/pokemon/'


async def get_one_pokemon(session, p_id):
    async with session.get(URL + str(p_id)) as resp:
        pokemon = await resp.json()
        return {'name': pokemon['name'],
                'id': p_id}


async def main():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for pok_id in range(1, 905):
            tasks.append(asyncio.create_task(get_one_pokemon(session, pok_id)))
        original_p_name = await asyncio.gather(*tasks)
        for pokemon in original_p_name:
            print(f'Pokemon name:{pokemon["name"]} and id:{pokemon["id"]}')
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
