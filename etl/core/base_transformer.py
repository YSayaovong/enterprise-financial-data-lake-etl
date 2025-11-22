from abc import ABC, abstractmethod

class BaseTransformer(ABC):
    @abstractmethod
    def transform(self, raw_data):
        raise NotImplementedError
