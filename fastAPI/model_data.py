from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#definisi struktur data untuk produk menggunakan pydantic basemodel
class Produk(BaseModel):
    nama: str
    harga: float
    stok: int
    deskripsi: str | None = None # parameter opsional (boleh kosong)


