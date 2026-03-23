import re

def parse_text(texts):

    data = {
        "register_number": None,
        "student_name": None,
        "batch_number": None,
        "academic_year": None,
        "department": None,
        "college_name": "SARANATHAN COLLEGE OF ENGINEERING"
    }

    texts = [t.strip() for t in texts if t.strip() != ""]

    full_text = " ".join(texts).upper()

   
    reg_match = re.search(r'SCE[0-9]{6,}', full_text)

    if reg_match:
        data["register_number"] = reg_match.group()

   
    year_index = None

    for i, t in enumerate(texts):

        year_match = re.search(r'20[0-9]{2}[- ]20[0-9]{2}', t)

        if year_match:
            data["academic_year"] = year_match.group()
            year_index = i
            break

   
    for i, t in enumerate(texts):

        if "BATCH" in t.upper():

            for j in range(i, min(i+3, len(texts))):

                match = re.search(r'[0-9]{6}', texts[j])

                if match:
                    data["batch_number"] = match.group()
                    break

    

    ignore_words = [
        "SCE","ID","BATCH","PRINCIPAL",
        "ENGINEERING","COLLEGE"
    ]

    for t in texts:

        clean = re.sub(r'[^A-Za-z ]', '', t).strip()

        words = clean.split()

        if 1 <= len(words) <= 3:

            if not any(w.upper() in ignore_words for w in words):

                if len(clean) >= 3:

                    data["student_name"] = clean
                    break

    
    departments = [
        "AID","CSE","ECE","EEE","IT","MECH","CIVIL"
    ]

    if year_index is not None:

        for t in texts[year_index:year_index+3]:

            word = t.upper()

            
            word = word.replace("1","I")
            word = word.replace("|","I")

            for dept in departments:

                if dept in word:
                    data["department"] = dept
                    break

    
    if not data["department"]:

        for t in texts:

            word = t.upper()

            word = word.replace("1","I")
            word = word.replace("|","I")

            for dept in departments:

                if dept == word:
                    data["department"] = dept
                    break

    return data