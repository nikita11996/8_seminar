import fastapi
import uvicorn
from src.routers import phonebook_router_v1



def main():
    app = fastapi.FastAPI()
    # app.add_event_handler("startup", startup)
    app.include_router(phonebook_router_v1, prefix='/api/v1')
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")


if __name__ == '__main__':
    main()
