import re
import logging
from abc import abstractmethod


class MetaFetcher:
    RE_URL_BROWSE = re.compile(r'https://.+/browse/(?P<browse_id>.+)\??')

    def __init__(self, ytm):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.ytm = ytm

    @abstractmethod
    def fetch(self, id_):
        pass
