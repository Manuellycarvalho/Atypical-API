from fastapi import FastAPI, HTTPException, status, Path, Header, Depends
from typing import Optional, Any, List
from model import Personagem


app = FastAPI()

personagens = {
    1: {"Nome": "Casey Gardner", "Idade": 15},
    2: {"Nome": "Sam Gardner", "Idade": 18},
    3: {"Nome": "Izzie Taylor", "Idade": 15}
}


@app.get("/personagens")
async def get_personagens():
    return personagens


@app.get("/personagens/{personagem_id}")
async def get_personagem(personagem_id: int):
    if personagem_id not in personagens:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    return personagens[personagem_id]


@app.post("/personagens")
async def post_personagem(personagem: Personagem):
    if personagem.id not in personagens:
        nextid = len(personagens) + 1
        personagens[nextid] = personagem
        del personagem.id
        return personagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"personagem não encontrado")


@app.put("/personagens/{personagem_id}")
async def update_personagem(personagem_id: int, personagem: Personagem):
    if personagem_id in personagens:
        personagens[personagem_id] = personagem
        personagem.id = personagem_id
        del personagem.id
        return personagem
    else:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")


@app.delete("/personagens/{personagem_id}")
async def delete_personagem(personagem_id: int):
    if personagem_id not in personagens:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    del personagens[personagem_id]
    return {"message": "Personagem excluído com sucesso"}

@app.patch("/personagens/{personagem_id}")
async def update_item(personagem_id: int, personagem: Personagem):
    if personagem_id in personagens:
        del personagem.id
        personagens[personagem_id].update(personagem.dict())
        return personagem
    else:
        return {"error": "Item not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="10.234.93.203", port=8000, log_level="info", reload=True)