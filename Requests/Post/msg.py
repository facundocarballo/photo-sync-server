import base64
from Handlers.Date.date import Date

DATA_KEYWORD = 'data'
DATE_KEYWORD = 'date'
FILENAME_KEYWORD = 'filename'

class Message:
    def __init__(self, req: any) -> None:
        self.req = req
        self.data = self._get_data_from_request()
        self.date = self._get_date_from_request()
        self.filename = self._get_filename_from_request()

    def _get_filename_from_request(self) -> str:
        return self.req[FILENAME_KEYWORD]

    def _get_date_from_request(self) -> Date:
        return Date(self.req[DATE_KEYWORD])

    def _get_data_from_request(self) -> bytes:
        data_string = self.req[DATA_KEYWORD]
        byte_array = bytearray(base64.b64decode(data_string))
        return bytes(byte_array)