import cv2
from pyzbar import pyzbar

def decode_and_save_qr(frame):
    decoded_objects = pyzbar.decode(frame, symbols=[pyzbar.ZBarSymbol.QRCODE])
    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')
        return qr_data  # Return QR code data

    return None  # No QR code found

def main():
    cap = cv2.VideoCapture(0)
    qr_code_data = None

    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        qr_code_data = decode_and_save_qr(frame)

        cv2.imshow('QR Code Scanner', frame)

        if qr_code_data:
            print(f"QR Code detected: {qr_code_data}")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()