import json
import httpx
from typing import Generic, TypeVar, Iterator

from .chat_completion_chunk import ChatCompletionChunk

_T = TypeVar("_T")


class Stream(Generic[_T]):
    def __init__(self, response: httpx.Response) -> None:
        self.response = response
        self._iterator = self._iter_events()

    def __next__(self) -> _T:
        return self._iterator.__next__()

    def __iter__(self) -> Iterator[_T]:
        for item in self._iterator:
            yield item

    def _iter_events(self) -> Iterator[_T]:
        for line in self.response.iter_lines():
            stringResponse = str(line, encoding='utf-8').replace("data: ", "")
            if stringResponse != '' and stringResponse != '/n':
                chunk = json.loads(stringResponse)
                if content := chunk.get('choices')[0].get('message').get('content') or "":
                    # Process each line from the stream and yield the data
                    yield ChatCompletionChunk(chunk)

    def __enter__(self) -> 'Stream[_T]':
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()

    def close(self) -> None:
        """
        Close the response and release the connection.

        Automatically called if the response body is read to completion.
        """
        self.response.close()
