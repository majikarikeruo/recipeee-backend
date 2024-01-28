
from app.models.recipe_model import RecipeBase
from app.shared.shared_data import past_recipes


def make_prompt(recipe_base: RecipeBase, day: int, days: int, policy: str):

    family_members = ", ".join(
        f"{member.age}歳の{member.gender}" for member in recipe_base.family_members)
    dislike_food = ", ".join(recipe_base.dislike_food)

    user_input = f'''
    ## 依頼内容
    {days}日間のうちの{day}日目のレシピを提案してください。
    
    ## 条件
    ・各食事には、主食・主菜・副菜をしっかりと含めるようにしてください。
    ・主食には麺・パン・ご飯のいずれかを含めるようにしてください。
    ・野菜を全く食べないレシピはないようにしてください。
    ・主菜には肉・魚のいずれかを必ず含めるようにしてください。
    ・ざっくりしたレシピ名は避けるようにしてください。例えば「パスタ」だけなのはNGです。「ミートソースパスタ」ならOKです。
    ・家族構成は、{family_members}です。年齢と性別にあった栄養バランスの良いレシピを提案してください。
    ・3食分のレシピを提案してください。レシピの作り方はかなり細かく工程を書くようにしてください。
    ・食材は、{family_members}に合わせた分量を提案するようにしてください。
    ・{past_recipes}にあるレシピとはなるべく重複しないようにしてください。ただし栄養のバランスを考えて重複しても仕方がない場合はこの限りではありません。
    ・レシピのポリシーとしては{policy}に従ったレシピを提案してください。
    ・苦手な食べ物は{dislike_food}なので、これはレシピに含めないようにしてください。
    ・必要な食材一覧（ingredients）には、「ブロッコリー　分量：2個」「鶏胸肉　分量：300g」のように必要な分量も含めて食材名を記載してください。

    ## 参考の書き方
    レシピや食材一覧に関する参考例を以下に示します。

    ### レシピ名の書き方事例
    茄子と挽肉のミートソースパスタ
    
    ### レシピの作り方の書き方事例
    1. 茄子と赤ピーマンは細かく切り、赤玉ねぎはみじん切りにします。
    2. フライパンにオリーブオイルをひき、牛挽肉を炒めます。挽肉がきつね色になったら、茄子、赤玉ねぎ、赤ピーマンを加えます。
    3. 野菜がしんなりとしてきたら、(A)のトマトソース、バルサミコ酢、ブラウンシュガー、チキンブイヨン、にんにく、赤唐辛子、ハーブミックスを加えてよく炒め合わせ、10分程度煮込みます。
    4. 別の鍋でお湯を沸かし、塩を加えた後にスパゲティを入れてパッケージの指示通りにゆでます。
    5. ゆであがったスパゲティを湯切りし、ソースが絡まるようにフライパンで軽く炒め合わせます。
    6. 盛り付けたパスタにソースをかけ、お好みで粉チーズやパセリ、黒こしょうをトッピングして完成です。


    ### 材料の書き方事例
    スパゲティ: 200g
    お湯 (ゆでる用): 約2リットル
    塩 (ゆでる用): 大さじ1
    牛挽肉: 250g
    赤玉ねぎ: 1個
    赤ピーマン: 1個
    茄子: 1個 (大サイズ)
    (A)トマトソース: 200ml
    (A)バルサミコ酢: 大さじ2
    (A)ブラウンシュガー: 小さじ2
    (A)チキンブイヨン: 1個
    (A)にんにく（みじん切り）: 小さじ1
    (A)赤唐辛子（みじん切り）: 小さじ1/2
    (A)ハーブミックス（タイム、バジル、オレガノ）: 各少々
    オリーブオイル: 大さじ2



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
                        },
                        "ingredients": {
                            "type": "string",
                            "description": "副菜のレシピを作るために必要な食材を分量付きで記載してください。"
                        }
                    },
                    "required": ["name", "how_to_cook", "ingredients"]
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
                        },
                        "ingredients": {
                            "type": "string",
                            "description": "主菜のレシピを作るために必要な食材を分量付きで記載してください。"
                        }
                    },
                    "required": ["name", "how_to_cook", "ingredients"]
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
                        },
                        "ingredients": {
                            "type": "string",
                            "description": "副菜のレシピを作るために必要な食材を分量付きで記載してください。"
                        }
                    },
                    "required": ["name", "how_to_cook", "ingredients"]
                },
            },
            "required": ["staple_food", "main_dish", "side_dish"]
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
                        },
                        "ingredients": {
                            "type": "string",
                            "description": "副菜のレシピを作るために必要な食材を分量付きで記載してください。"
                        }
                    },
                    "required": ["name", "how_to_cook", "ingredients"]
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
                        },
                        "ingredients": {
                            "type": "string",
                            "description": "主菜のレシピを作るために必要な食材を分量付きで記載してください。"
                        }
                    },
                    "required": ["name", "how_to_cook", "ingredients"]
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
                        },
                        "ingredients": {
                            "type": "string",
                            "description": "副菜のレシピを作るために必要な食材を分量付きで記載してください。"
                        }
                    },
                    "required": ["name", "how_to_cook", "ingredients"]
                },
            },
            "required": ["staple_food", "main_dish", "side_dish"]
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
                        },
                        "ingredients": {
                            "type": "string",
                            "description": "副菜のレシピを作るために必要な食材を分量付きで記載してください。"
                        }
                    },
                    "required": ["name", "how_to_cook", "ingredients"]
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
                        },
                        "ingredients": {
                            "type": "string",
                            "description": "主菜のレシピを作るために必要な食材を分量付きで記載してください。"
                        }
                    },
                    "required": ["name", "how_to_cook", "ingredients"]
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
                        },
                        "ingredients": {
                            "type": "string",
                            "description": "副菜のレシピを作るために必要な食材を分量付きで記載してください。"
                        }
                    },
                    "required": ["name", "how_to_cook", "ingredients"]
                },
            },
            "required": ["staple_food", "main_dish", "side_dish"]
        }
    },
    "required": ["morning", "lunch", "dinner"]
}
