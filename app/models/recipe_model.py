from pydantic import BaseModel
from typing import List, Dict

class FamilyMember(BaseModel):
    age: int
    gender: str


class RecipeBase(BaseModel):
    family_members: List[FamilyMember]
    dislike_food: List[str]


class RecipeSuggestionResponse(BaseModel):
    weekly_plan: List[Dict[str, Dict]]