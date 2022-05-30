from main import app
from .models import User

@app.get("/")
async def home():
    u = User(name="Mawuli Deku",  email="fivi@gm.com", age=23, password="1234553")
    await session.add(u)
    await session.commit()
    return {"home": u}