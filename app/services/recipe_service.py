import json
import asyncio

from app.config import client
from app.models.recipe_model import RecipeBase, RecipeSuggestionResponse
from app.shared.shared_data import past_recipes
from app.utils.prompt import make_prompt, json_schema


async def get_recipe_suggestions(recipe_base: RecipeBase, days: int, policy: str)->RecipeSuggestionResponse:
    loop = asyncio.get_event_loop()
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for day in range(1, days + 1):
            task = tg.create_task(get_daily_plan(day, days, recipe_base, policy, loop))
            tasks.append(task)
    
    weekly_plan = [await task for task in tasks]

    return {"weekly_plan": weekly_plan}


def make_api_call(model, messages):
    return client.chat.completions.create(
        model=model, 
        messages=messages,
        functions=[
            {"name": "get_recipes", "parameters": json_schema}
        ],
        function_call="auto",
    )

async def get_daily_plan(day, days, recipe_base, policy, loop):
    user_input = make_prompt(recipe_base, day, days, policy)

    response = await loop.run_in_executor(
        None, 
        lambda: make_api_call(
            "gpt-3.5-turbo-1106",
            [{"role": "system", "content": "あなたは食事プランとレシピ、そしてレシピを作るに必要な食材が何かの情報を提供する親切なアシスタントです。"},
             {"role": "user", "content": user_input}]
        )
    )

    json_data = json.loads(response.choices[0].message.function_call.arguments)

    for meal in ["morning", "lunch", "dinner"]:
        for dish_type in ["staple_food", "main_dish", "side_dish"]:
            recipe_name = json_data[meal][dish_type]["name"]
            past_recipes.append(recipe_name)

    return json_data

