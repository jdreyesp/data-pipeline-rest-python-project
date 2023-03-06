from typing import Dict
from datetime import datetime

class Weight:
    def __init__(self, mass_kg: int, last_measured: datetime):
        self.mass_kg = mass_kg
        self.last_measured = last_measured

    def serialize(self) -> Dict:
        return {"mass_kg": self.mass_kg,
                "last_measured": str(self.last_measured)
                }


def weight_decoder(weight_dict: Dict):
    return Weight(mass_kg=weight_dict.get("mass_kg"),
                  last_measured=weight_dict.get("last_measured"))


class Feeding:
    def __init__(self, amount_kg: int, cron_schedule: str, last_measured: datetime):
        self.amount_kg = amount_kg
        self.cron_schedule = cron_schedule
        self.last_measured = last_measured

    def serialize(self) -> Dict:
        return {"amount_kg": self.amount_kg,
                "cron_schedule": self.cron_schedule,
                "last_measured": str(self.last_measured)
                }


def feeding_decoder(feeding_dict: Dict):
    return Feeding(amount_kg=feeding_dict.get("amount_kg"),
                   cron_schedule=feeding_dict.get("cron_schedule"),
                   last_measured=feeding_dict.get("last_measured"))


class MilkProduction:
    def __init__(self, last_milk: datetime, cron_schedule: str, amount_l: int):
        self.last_milk = last_milk
        self.cron_schedule = cron_schedule
        self.amount_l = amount_l

    def serialize(self) -> Dict:
        return {"last_milk": str(self.last_milk),
                "cron_schedule": self.cron_schedule,
                "amount_l": self.amount_l
                }


def milk_production_decoder(milk_production_dict: Dict):
    return MilkProduction(last_milk=milk_production_dict.get("last_milk"),
                          cron_schedule=milk_production_dict.get("cron_schedule"),
                          amount_l=milk_production_dict.get("amount_l"))

class Cow:
    def __init__(self,
                 name: str, sex: str, birthdate: datetime, condition: str, weight: Weight,
                 feeding: Feeding,
                 milk_production: MilkProduction,
                 has_calves: bool):
        self.name = name
        self.sex = sex
        self.birthdate = birthdate
        self.condition = condition
        self.weight = weight
        self.feeding = feeding
        self.milk_production = milk_production
        self.has_calves = has_calves

    def serialize(self) -> Dict:
        return {"name": self.name,
                "sex": self.sex,
                "birthdate": str(self.birthdate),
                "condition": self.condition,
                "weight": self.weight.serialize(),
                "feeding": self.feeding.serialize(),
                "milk_production": self.milk_production.serialize(),
                "has_calves": self.has_calves
                }


def cow_decoder(cow_dict: Dict):
    return Cow(name=cow_dict.get("name"),
               sex=cow_dict.get("sex"),
               birthdate=cow_dict.get("birthdate"),
               condition=cow_dict.get("condition"),
               weight=weight_decoder(cow_dict.get("weight")),
               feeding=feeding_decoder(cow_dict.get("feeding")),
               milk_production=milk_production_decoder(cow_dict.get("milk_production")),
               has_calves=cow_dict.get("has_calves"))
