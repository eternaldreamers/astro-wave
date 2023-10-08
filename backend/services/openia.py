import openai
import re
from typing import List
import datetime
from database import get_patient_prescriptions_and_details, create_reminder

class Openia:
    def __init__(self, api_key: str, eccentric: bool = True):
        openai.api_key = api_key
        self.model_engine = "text-davinci-003"
        self.temperature = 0.5
        self.eccentric = eccentric

    def set_model_engine(self, model_engine: str):
        self.model_engine = model_engine

    def set_temperature(self, temperature: float):
        self.temperature = temperature

    def _generate_text(self, prompt: str, length: int = 1024, num_options: int = 1, temperature: float = 0.5) -> List[str]:
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=length,
            n=num_options,
            temperature=self.temperature
        )
        options = [choice.text.strip() for choice in response.choices]
        return options