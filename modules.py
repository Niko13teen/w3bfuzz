import httpx
import logging
from fake_useragent import UserAgent
from typing import List, Dict


logging.basicConfig(
    level=logging.INFO,
    filename="log.txt",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)


class Payload (object):
    def __init__(self, filename) -> str:
        self.wordlist: object = httpx.get(f"{filename}")
        
    def __repr__(self) -> str:
        return f"{self.wordlist.url}"

    def __len__(self) -> int:
        return len(self.wordlist.text.split())
        
    def get_payloads(self) -> List[str]:
        payload: List[str] = [string for string in self.wordlist.text.split()]
        return payload


class Pretesting (object):
    def __init__(self, hostname) -> str:
        self.hostname: str = hostname
        self.ua: object = UserAgent()
        self.headers: str = {"User-Agent": self.ua.random}

    def __repr__(self) -> str:
        return f"{self.hostname}"

    def pretesting(self) -> Dict[str, str]:
        try:
            target: str = self.hostname
            connection: object = httpx.get(target, headers=self.headers)
        except Exception as error:
            logging.error(f"Error : {error}", exc_info=True)
            return f"{target} : Error => log.txt"

        status_code: int = connection.status_code
        negative_case: object = httpx.get(f"{target}/secret_url", headers=self.headers)

        return dict(
            {
                "hostname": self.hostname,
                "user-agent": self.headers,
                "response_status_code": str(status_code),
                "payload": "/secret_url",
                "payload_code": negative_case.status_code,
            }
        )
        
    def user_agent(self):
    	return self.headers

