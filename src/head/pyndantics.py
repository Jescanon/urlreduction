from pydantic import BaseModel, HttpUrl, ConfigDict


class Url(BaseModel):
    url: HttpUrl

    model_config = ConfigDict()