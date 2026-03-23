import cv2

from modules.webcam import start_camera, get_frame
from modules.ocr import extract_text
from modules.parser import parse_text
from modules.json_export import save_to_json
from modules.database import save_to_database


def is_valid(data):

    required_fields = [

        "student_name",
        "register_number",
        "batch_number",
        "academic_year",
        "department",
        "college_name"

    ]

    for field in required_fields:

        if data.get(field) is None or data.get(field) == "":

            return False

    return True



# start webcam
cap = start_camera()


print("\n==============================")
print(" AI ID CARD OCR SYSTEM ")
print("==============================")
print("\nPress S to scan ID card")
print("Press ESC to exit\n")


while True:

    frame = get_frame(cap)

    if frame is None:
        break


    cv2.imshow("Live Camera", frame)


    key = cv2.waitKey(1) & 0xFF


    # press S to scan
    if key == ord('s'):

        print("\n📸 Capturing ID card...")


        img = frame.copy()


        img = cv2.resize(img, (640, 480))


        height, width, _ = img.shape


        roi = img[int(height * 0.40):height, 0:width]


        cv2.imshow("Captured ID Region", roi)


        print("\n⏳ Running OCR...")


        texts = extract_text(roi)


        print("\n📄 OCR TEXT:")
        print(texts)


        data = parse_text(texts)


        print("\n📊 EXTRACTED DATA:")

        for field, value in data.items():

            print(f"{field} : {value}")


        # validation check
        if not is_valid(data):

            print("\n❌ ERROR: Some fields not detected properly")

            print("⚠ Please adjust ID position and scan again")

            print("TIP:")

            print("• keep ID straight")
            print("• ensure good lighting")
            print("• avoid blur")
            print("• avoid shadow")

            print("\n-----------------------------")

            continue


        # save json
        save_to_json(data)

        print("\n💾 JSON file saved")


        # save database
        saved = save_to_database(data)


        if saved:

            print("🗄 Stored in database")

        else:

            print("⚠ Duplicate record not stored")


        print("\n----------------------------------\n")


    # press ESC to exit
    if key == 27:

        print("\nExiting system...")

        break


cap.release()

cv2.destroyAllWindows()