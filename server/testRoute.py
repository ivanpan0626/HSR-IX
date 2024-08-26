import enka
import asyncio
from flask import Blueprint, jsonify

testRoute = Blueprint('testRoute', __name__)

async def main(uid, showcaseNum) -> None:
    async with enka.HSRClient(enka.hsr.Language.ENGLISH) as client:
        showcase = await client.fetch_showcase(uid)
        #print(showcase.player.nickname)
        #return (showcase.characters[showcaseNum].name)
        res = []
        for chars in showcase.characters:
            res.append(chars.name)
        return res

@testRoute.route('/<uid>/<showcaseNum>', methods=['POST'])
def findUser(uid, showcaseNum):
    val = asyncio.run(main(uid, int(showcaseNum)))
    return {'showcase': val}
