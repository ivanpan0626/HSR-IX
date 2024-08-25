import enka
import asyncio
from flask import Blueprint

testRoute = Blueprint('testRoute', __name__)

async def main(uid, showcaseNum) -> None:
    async with enka.HSRClient(enka.hsr.Language.ENGLISH) as client:
        showcase = await client.fetch_showcase(uid)
        print(showcase.player.nickname)
        return (showcase.characters[showcaseNum].name)

@testRoute.route('/<uid>/<showcaseNum>', methods=['POST'])
def findUser(uid, showcaseNum):
    #print('hi')
    name = asyncio.run(main(uid, int(showcaseNum)))
    print(name)
    return {'name' : name}