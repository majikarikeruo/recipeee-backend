
from app.model import RecipeBase


def make_prompt(recipe_base: RecipeBase, day: int, days: int, policy: str):

    family_members = ", ".join(
        f"{member.age}歳の{member.gender}" for member in recipe_base.family_members)
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
    ・別途展開するJSON Schemaに基づいてJSONデータで返却してください
    '''

    return user_input


json_schema = {
    "type": "object",
    "properties": {
        "morning": {
            "type": "object",
            "properties": {
                "staple_food": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主食のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主食のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "main_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "side_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "副菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "副菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "ingredients": {"type": "string"}
            },
            "required": ["staple_food", "main_dish", "side_dish", "ingredients"]
        },
        "lunch": {
            "type": "object",
            "properties": {
                "staple_food": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主食のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主食のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "main_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "side_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "副菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "副菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "ingredients": {"type": "string"}
            },
            "required": ["staple_food", "main_dish", "side_dish", "ingredients"]
        },
        "dinner": {
            "type": "object",
            "properties": {
                "staple_food": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主食のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主食のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "main_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "side_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "副菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "副菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "ingredients": {"type": "string"}
            },
            "required": ["staple_food", "main_dish", "side_dish", "ingredients"]
        }
    },
    "required": ["morning", "lunch", "dinner"]
}
