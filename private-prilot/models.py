from typing import Optional, Union

from pydantic import BaseModel


class OpenAIinput(BaseModel):
    model: str
    prompt: Optional[str]
    max_tokens: Optional[int] = 16
    temperature: Optional[float] = 0.6
    top_p: Optional[float] = 1.0
    n: Optional[int] = 1
    stream: Optional[bool] = False
    stop: Optional[Union[str, list]] = ["\n"]
    presence_penalty: Optional[float] = 0
    frequency_penalty: Optional[float] = 1
    best_of: Optional[int] = 1
