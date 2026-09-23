from fastapi import FastAPI
from model_data import Produk

app = FastAPI()

#endpoint utama (Root)
@app.get("/")

def read_root():
    return {"Hello World!"}

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
def read_items(item_id: int):   
        return {"Item id": item_id}

@app.get("/users/{user_id}/orders")
def read_user_orders(user_id: int, status: str = "Pending", limit: int = 10):
     return {
          "User ID ": user_id,
          "Status": status,
          "Limit": limit
     }
#endpoint POST
@app.post("/produk/")
def tambah_produk(produk: Produk):
    total_nilai_stok = produk.harga * produk.stok
    return{
        "Pesan": "Produk berhasil ditambahkan",
        "data_diterima": produk,
        "total_nilai_stok": total_nilai_stok

    }