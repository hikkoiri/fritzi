import uvicorn
from src import Controller
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Fritzi API",
    description="Provide an easy-to-use REST interfaces for FRITZ!Box routers.",
    version="1.0.0",
)
app.include_router(Controller.router)

origins = ["http://localhost:3000", "https://carlo-hildebrandt.de"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", port=8001)


if __name__ == "__main__":
    main()
