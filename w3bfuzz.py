import argparse
import logging
import aiohttp
import asyncio
from typing import List, Dict, NoReturn
from modules import Payload, Pretesting
from modules import information_banner


logging.basicConfig(
    level=logging.INFO,
    filename="log.txt",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)


@information_banner
async def main_function(hostname: str) -> NoReturn:
    filename: object = Payload()
    target: object = Pretesting(hostname)
    payload: List[str] = filename.get_payloads()
    pretesting: Dict[str, int] = target.pretesting()
    logging.info(f"All payloads: {len(payload)}\nPretesting INFO: {pretesting}")

    async with aiohttp.ClientSession() as session:
        if pretesting["payload_code"] != 200:
            print(
                f"[*] Hostname: {target}\n[*] Status: {pretesting['response_status_code']}\n[*] Testing payload: {pretesting['payload']}\n[*] Payload Code: {pretesting['payload_code']}\n\n[+] Working... \n\n"
            )
            for string in payload:
                async with session.get(
                    f"{str(target)}/{string}", headers=target.user_agent()
                ) as response:
                    logging.info(f"{str(target)}/{string} : {response.status}")
                    if response.status != 404:
                        print(f"[+] {str(target)}/{string} : {response.status}")
        else:
            logging.info(f"Payload Code : {pretesting['payload_code']}, Aborted!")
            print("In Development :)")  # TODO
            exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target",
        "-t",
        action="store",
        dest="target",
        help="input hostname : https://example.site",
    )
    args = parser.parse_args()
    asyncio.run(main_function(args.target))
