import uvicorn
from src import Controller
from fastapi import FastAPI

app = FastAPI(
    title="Fritzi API",
    description="Provide an easy-to-use REST interfaces for FRITZ!Box routers.",
    version="1.0.0"
)
app.include_router(Controller.router)

def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0")


if __name__ == "__main__":
    main()