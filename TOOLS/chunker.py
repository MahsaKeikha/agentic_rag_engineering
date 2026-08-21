from dataclasses import dataclass
from typing import List

@dataclass
class Chunker:
    chunk_size: int = 800
    overlap: int = 100

    def split(self, text: str) -> List[str]:
        if not text:
            return []
        step = max(1, self.chunk_size - self.overlap)
        return [text[i:i+self.chunk_size] for i in range(0, len(text), step)]
