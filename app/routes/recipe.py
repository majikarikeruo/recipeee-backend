from fastapi import APIRouter, Depends
from app.models.recipe_model import RecipeBase, RecipeSuggestionResponse
from app.services.recipe_service import get_recipe_suggestions

router = APIRouter()

@router.post("/recipe/suggestions", response_model=RecipeSuggestionResponse)
async def recipe_suggestions_endpoint(recipe_base: RecipeBase, days: int, policy: str):
    return await get_recipe_suggestions(recipe_base, days, policy)