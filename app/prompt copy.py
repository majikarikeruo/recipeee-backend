
from app.model import RecipeBase


def make_prompt(recipe_base: RecipeBase, day: int, days: int, policy: str):

    family_members = ", ".join(f"{member.age}歳の{member.gender}" for member in recipe_base.family_members)
    dislike_food = ", ".join(recipe_base.dislike_food)

    user_input = f'''
    {days}日間うちの{day}日目のレシピを提案してください。
    
    ##条件
    ・各食事には、主食・主菜・副菜をしっかりと含めるようにしてください。
    ・家族構成は、{family_members}です。年齢と性別にあった栄養バランスの良いレシピを提案してください。
    ・苦手な食べ物は{dislike_food}なので、これはレシピに含めないようにしてください。
    ・3食分のレシピを提案してください。
    ・外食の場合は特にレシピ提案は不要です。
    ・他の日とのレシピ被りはあまりないようにしてください。
    ・レシピのポリシーとしては{policy}に従ったレシピを提案してください。

    ## 表示形式
    # ・以下のような表記にしてください。
    
    # ■{day}日目
    # 【レシピ】
    # 主食：〇〇
    # 主菜：〇〇
    # 副菜：〇〇

    # 【作り方・主食：〇〇】
    # ### ここに主食：〇〇の作り方を記載する。レシピごとに工程をしっかりと書くようにすること。

    # 【作り方・主菜：〇〇】
    # ### ここに主菜：〇〇の作り方を記載する。レシピごとに工程をしっかりと書くようにすること。

    # 【作り方・副菜：〇〇】
    # ### ここに副菜：〇〇の作り方を記載する。レシピごとに工程をしっかりと書くようにすること。

    # 【必要な食材リスト一覧】
    # ###  主食：〇〇、主菜：〇〇、副菜：〇〇の全てのレシピを作るのに必要は食材をもれなく入力する。
    # 「ブロッコリー　分量：2個」「鶏胸肉　分量：300g」のように食材には必要な分量も含めて記載すること。
    # 各食材の正確な分量を含めて、詳細な食材リストを提供してください。
    '''

    return user_input


def schema_function():
    json_schema = {
        "type": "object",
        "properties": {
            "morning": {
            "type": "object",
            "properties": {
                "staple_food": {
                "type": "object",
                "properties": {
                    "name": { "type": "string" },
                    "how_to_cook": { "type": "string" }
                },
                "required": ["name", "how_to_cook"]
                },
                "main_dish": {
                "type": "object",
                "properties": {
                    "name": { "type": "string" },
                    "how_to_cook": { "type": "string" }
                },
                "required": ["name", "how_to_cook"]
                },
                "side_dish": {
                "type": "object",
                "properties": {
                    "name": { "type": "string" },
                    "how_to_cook": { "type": "string" }
                },
                "required": ["name", "how_to_cook"]
                },
                "ingredients": { "type": "string" }
            },
            "required": ["staple_food", "main_dish", "side_dish", "ingredients"]
            },
            "lunch": {
            "$ref": "#/properties/morning"
            },
            "dinner": {
            "$ref": "#/properties/morning"
            }
        },
        "required": ["morning", "lunch", "dinner"]
    }
    return json_schema