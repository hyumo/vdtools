import streamlit as st
from pydantic import BaseModel, Field, HttpUrl, root_validator
from pydantic.color import Color

import streamlit_pydantic as sp


class ExampleModel(BaseModel):
    url: HttpUrl
    color: Color
    email: str = Field(..., max_length=100, regex=r"^\S+@\S+$")
    a: int
    b: int

    @root_validator
    def check_a(cls, values):
        a = values.get("a")
        b = values.get("b")
        if a > b:
            raise ValueError("a must be less than b")
        return values



data = sp.pydantic_form(key="my_form", model=ExampleModel)
if data:
    st.json(data.json())