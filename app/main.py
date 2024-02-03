
from fastapi import FastAPI
import asyncio


from app.model import RecipeBase
from app.config import client
from app.prompt import json_schema,make_prompt,system_prompt
import json 

# 環境変数を読み込みするためにj必要


app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


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

    # 同期API呼び出しをラムダ関数でラップして非同期実行
    response = await loop.run_in_executor(
        None, 
        lambda: make_api_call(
            "gpt-3.5-turbo-1106",
            [{"role": "system", "content": system_prompt},
             {"role": "user", "content": user_input}]
        )
    )
    return json.loads(response.choices[0].message.function_call.arguments)

@app.post("/recipe/suggestions")
async def get_recipe_suggestions(recipe_base: RecipeBase, days: int, policy: str):
    loop = asyncio.get_event_loop()
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for day in range(1, days + 1):
            task = tg.create_task(get_daily_plan(day, days, recipe_base, policy, loop))
            tasks.append(task)
    
    weekly_plan = [await task for task in tasks]
    return {"weekly_plan": weekly_plan}

