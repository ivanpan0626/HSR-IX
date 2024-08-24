import enka
import asyncio

async def main() -> None:
    async with enka.HSRClient(enka.hsr.Language.ENGLISH) as client:
        showcase = await client.fetch_showcase(601066866)
        print(showcase.player.nickname)
        print(showcase.characters[0].name)



asyncio.run(main())
