from pydantic import BaseModel

class User(BaseModel):
    id: int | None = None
    is_bot: bool | None = None
    first_name: str | None = None
    username: str | None = None
    last_name: str | None = None
    language_code: str | None = None

class Chat(BaseModel):
    id: int | None = None
    type: str | None = None
    title: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None

class BotMessageResponse(BaseModel):
    message_id: int | None = None
    from_user: User
    chat: Chat | None = None
    date: int | None = None
    text: str | None = None
