import json

class PersonalityHandler:
    name                : str
    gender              : str
    age                 : int
    ethnicity           : str
    education           : str
    employment          : str
    household_size      : str
    housing_ownership   : str
    housing_type        : str
    ideology            : str
    income              : str
    internet_access     : str
    location            : str
    marital_status      : str
    metro_status        : str
    party_id            : str
    phone_service       : str

    def __init__(self, jsonData : any):
        try:
            self.name = jsonData['name']
            self.gender = jsonData['gender']
            self.age = jsonData['age']
            self.ethnicity = jsonData['ethnicity']
            self.education = jsonData['education']
            self.employment = jsonData['employment']
            self.household_size = jsonData['household_size']
            self.housing_ownership = jsonData['housing_ownership']
            self.housing_type = jsonData['housing_type']
            self.ideology = jsonData['ideology']
            self.income = jsonData['income']
            self.internet_access = jsonData['internet_access']
            self.location = jsonData['location']
            self.marital_status = jsonData['marital_status']
            self.metro_status = jsonData['metro_status']
            self.party_id = jsonData['party_id']
            self.phone_service = jsonData['phone_service']
        except Exception:
            print(f"Creation of PersonalityHandler failed.")
        pass

    def ToJson(self) -> dict:
        data = {
            "name" : self.name,
            "gender" : self.gender,
            "age" : self.age,
            "ethnicity" : self.ethnicity,
            "education" : self.education,
            "employment" : self.employment,
            "household_size" : self.household_size,
            "housing_ownership" : self.housing_ownership,
            "housing_type" : self.housing_type,
            "ideology" : self.ideology,
            "income" : self.income,
            "internet_access" : self.internet_access,
            "location" : self.location,
            "marital_status" : self.marital_status,
            "metro_status" : self.metro_status,
            "party_id" : self.party_id,
            "phone_service" : self.phone_service
            }
        return data