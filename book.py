from dataclasses import dataclass
from pathlib import Path
from typing import Union
from poppler import load_from_data, PageRenderer
from thumbnail import Thumbnail

@dataclass
class Book:
    pdfdata: bytes
    title: str
    pages: int
    thumbnail: Thumbnail 
    
    def __len__(self) -> int:
        return self.pages

    @staticmethod
    def from_file(path: Union[Path, str]):
        data = b""
        with open(path, "rb") as fp:
            data = fp.read()
        document = load_from_data(data)
        pages = document.pages
        title = document.title
        renderer = PageRenderer()
        thumbnail = renderer.render_page(document.create_page(0)).data
        thumbnail = Thumbnail(data=thumbnail)
        return Book(pdfdata=data,
                    title=title,
                    pages=pages,
                    thumbnail=thumbnail
        )
