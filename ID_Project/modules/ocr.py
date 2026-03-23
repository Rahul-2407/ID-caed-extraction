import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image):
    results = reader.readtext(image)

    texts = []
    for (bbox, text, prob) in results:
        texts.append(text)

    return texts