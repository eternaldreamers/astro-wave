import openai
from typing import List

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
    
    def teach(self, message: str) -> str:
        """
        Generate a response based on the given message, teaching.
        """
        responses = self._generate_text(prompt=message, num_options=1, temperature=self.temperature)
        return responses[0] if responses else ""
    
    def interpret_differences(self, differences):
        explanations = {
            "moons": "number of moons",
            "gravity": "force of gravity",
            "temperature": "average temperature",
            "rings": "presence of rings",
            "water": "amount of water",
            "craters": "number of craters",
            "radiation": "level of radiation",
            "density": "density",
            "size": "size",
            "volcanoes": "number of volcanoes",
            "auroras": "number of auroras"
        }

        interpretation = "The answer you chose is incorrect because, "

        for key, (correct_val, incorrect_val) in differences.items():
            if key in explanations:
                if isinstance(correct_val, (int, float)) and isinstance(incorrect_val, (int, float)):
                    if correct_val > incorrect_val:
                        interpretation += f"the {explanations[key]} is higher, "
                    else:
                        interpretation += f"the {explanations[key]} is lower, "
                else:
                    interpretation += f"the {explanations[key]} is different, "

        interpretation = interpretation.rstrip(", ") + "."
        return interpretation