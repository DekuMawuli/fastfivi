from fastapi import FastAPI

app = FastAPI()

from app.views import *
from app.models import *

session: Session = None

def main():
    global session
    session = created_tb()


if __name__ == "__main__":
    main()


