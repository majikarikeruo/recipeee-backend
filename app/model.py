from pydantic import BaseModel
from typing import List

class FamilyMember(BaseModel):
    age: int
    gender: str


class RecipeBase(BaseModel):
    family_members: List[FamilyMember]
    dislike_food: List[str]