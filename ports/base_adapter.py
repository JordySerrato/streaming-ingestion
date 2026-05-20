from abc import ABC, abstractmethod
class BaseAdapter(ABC):

    @abstractmethod
    def fetch_data(
        self,
        query,
        chunk_size
    ):
        pass