from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LevelItem(BaseModel):
    level_id: str
    level_name: str
    host: str
    publish: str
    co_creators: list[str]
    verifier: str
    progress: str
    description: str
    difficulty: list[int]
    difficulty_votes: dict[str, list[int]]
    victory: list[str]

class LevelListItem(BaseModel):
    name: str
    long_name: str
    levels: list[str]
    parent: str | None
    isparent: bool

db_level: dict[str, LevelItem] = {
    "140644686": LevelItem(**{
        "level_id": "140644686",
        "level_name": "Subplex Final",
        "host": "이슬우",
        "publish": "이슬우",
        "co_creaters": [],
        "verifier": "이슬우",
        "progress": "Unknown",
        "description": "",
        "difficulty": [2, 0],
        "difficulty_votes": {"이슬우": [2, 0]},
        "victory": []
    })
}

db_level_list: dict[str, LevelListItem] = {
    "ULL": LevelListItem(**{
        "name": "ULL",
        "long_name": "Unverified Level List / 언베리파이드 레벨 순위",
        "levels": [
            "140644686"
        ],
        "parent": "FLL",
        "isparent": bool
    })
}

@app.get("/api/levels", response_model=dict[str, LevelItem])
async def get_levels():
    return db_level

@app.post("/api/levels")
async def update_levels(new_data: dict[str, LevelItem]):
    db_level.update(new_data)
    return {"success": True}

@app.get("/api/lists", response_model=dict[str, LevelItem])
async def get_level_lists():
    return db_level_list

@app.post("/api/lists")
async def update_level_lists(new_data: dict[str, LevelListItem]):
    db_level_list.update(new_data)
    return {"success": True}