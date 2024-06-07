import argparse
import logging
import aiohttp
import asyncio
from colorama import Fore
from typing import List, Dict, NoReturn
from modules import banner, Payload, Pretesting


logging.basicConfig(
    level=logging.INFO,
    filename="log.txt",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)

async def main_function(hostname: str, wordlist: str) -> NoReturn:
    filename:   object = Payload(wordlist)
    target:     object = Pretesting(hostname)
    payload:    List[str] = filename.get_payloads()
    pretesting: Dict[str, int] = target.pretesting()
    logging.info(f"All payloads: {len(payload)}\nPretesting INFO: {pretesting}")
    print(f"\n{banner}\n[+] All Payloads: {Fore.CYAN}{len(Payload(filename))}{Fore.GREEN}\n[+] TG Author: {Fore.CYAN}https://t.me/niko13teen\n")

    if pretesting["payload_code"] != 200:
        print(
            f"{Fore.GREEN}[*] Hostname: {Fore.CYAN}{target}\n{Fore.GREEN}[*] Status: {Fore.CYAN}{pretesting['response_status_code']}{Fore.GREEN}\n[*] Testing payload: {Fore.CYAN}{pretesting['payload']}{Fore.GREEN}\n[*] Payload Code: {Fore.CYAN}{pretesting['payload_code']}\n\n"
        )
        async with aiohttp.ClientSession() as session:
            for directory in payload:
                try:
                    async with session.get(
                        f"{str(target)}/{directory}", headers=target.user_agent()
                    ) as response:
                        logging.info(f"{str(target)}/{directory} : {response.status}")
                        if response.status != 404 and response.status != 429:
                            print(f"{Fore.GREEN}[+] {str(target)}/{directory} : {Fore.CYAN}{response.status}")
                except Exception as error:
                    logging.info(f"{str(target)}/{directory} : {response.status}")
                    pass
    else:
        print('Incorrected payload code!')
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
    parser.add_argument(
        "--wordlist",
        "-2",
        action="store",
        dest="wordlist",
        help="input link raw wordlist",
        default="https://raw.githubusercontent.com/six2dez/OneListForAll/main/onelistforallmicro.txt"
    )
    args = parser.parse_args()
    asyncio.run(main_function(args.target, args.wordlist))
