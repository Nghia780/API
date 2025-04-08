from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 👇 Cho phép các origin frontend
origins = [
    "http://localhost:3000",
    "http://kingdomvn.com:3000",  # bạn đang dùng domain này
    "https://kingdomvn.com",      # nếu sau này dùng HTTPS
]

# 👇 Thêm middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # hoặc ["*"] để cho tất cả (không khuyến khích cho production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Render!"}
