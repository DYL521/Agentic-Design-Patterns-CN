from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import List, Optional
from datetime import date


# --- Pydantic Model Definition (from above) ---
# --- Pydantic 模型定义（来自上文） ---
class User(BaseModel):
    name: str = Field(..., description="The full name of the user.")  # 用户的全名
    email: EmailStr = Field(..., description="The user's email address.")  # 用户的电子邮件地址
    date_of_birth: Optional[date] = Field(None, description="The user's date of birth.")  # 用户的出生日期
    interests: List[str] = Field(default_factory=list, description="A list of the user's interests.")  # 用户的兴趣列表


# --- Hypothetical LLM Output ---
# --- 假设的大语言模型输出 ---
llm_output_json = """
{
    "name": "Alice Wonderland",
    "email": "alice.w@example.com",
    "date_of_birth": "1995-07-21",
    "interests": [
        "Natural Language Processing",
        "Python Programming",
        "Gardening"
    ]
}
"""

# --- Parsing and Validation ---
# --- 解析和验证 ---
try:
    # Use the model_validate_json class method to parse the JSON string.
    # 使用 model_validate_json 类方法解析 JSON 字符串
    # This single step parses the JSON and validates the data against the User model.
    # 这一步同时解析 JSON 并根据 User 模型验证数据
    user_object = User.model_validate_json(llm_output_json)

    # Now you can work with a clean, type-safe Python object.
    # 现在你可以使用一个干净、类型安全的 Python 对象
    print("Successfully created User object!")  # 成功创建用户对象！
    print(f"Name: {user_object.name}")  # 姓名：{user_object.name}
    print(f"Email: {user_object.email}")  # 电子邮件：{user_object.email}
    print(f"Date of Birth: {user_object.date_of_birth}")  # 出生日期：{user_object.date_of_birth}
    print(f"First Interest: {user_object.interests[0]}")  # 第一个兴趣：{user_object.interests[0]}

    # You can access the data like any other Python object attribute.
    # 你可以像访问其他 Python 对象属性一样访问数据
    # Pydantic has already converted the 'date_of_birth' string to a datetime.date object.
    # Pydantic 已将 'date_of_birth' 字符串转换为 datetime.date 对象
    print(f"Type of date_of_birth: {type(user_object.date_of_birth)}")  # date_of_birth 的类型：{type(user_object.date_of_birth)}

except ValidationError as e:
    # If the JSON is malformed or the data doesn't match the model's types,
    # 如果 JSON 格式错误或数据不匹配模型的类型
    # Pydantic will raise a ValidationError.
    # Pydantic 将引发 ValidationError
    print("Failed to validate JSON from LLM.")  # 验证来自大语言模型的 JSON 失败
    print(e)
