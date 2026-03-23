import json
import datetime

def save_to_json(data):

    result = {
        "student_name": data["student_name"],
        "register_number": data["register_number"],
        "batch_number": data["batch_number"],
        "department": data["department"],
        "academic_year": data["academic_year"],
        "college_name": data["college_name"],
        "timestamp": str(datetime.datetime.now())
    }

    with open("output.json", "w") as file:
        json.dump(result, file, indent=4)

    return result