import cv2

# Variables globales
clicked = False
r = g = b = x_pos = y_pos = 0

# Función para manejar clics del mouse
def mouse_callback(event, x, y, flags, param):
    global b, g, r, x_pos, y_pos, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = frame[y, x]

# Captura de cámara
cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

cv2.namedWindow("Color Detector")
cv2.setMouseCallback("Color Detector", mouse_callback)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if clicked:
        # Dibujar un rectángulo con el color detectado
        cv2.rectangle(frame, (20, 20), (300, 60), (int(b), int(g), int(r)), -1)
        text = f"RGB: ({r}, {g}, {b})"
        cv2.putText(frame, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (255 - int(b), 255 - int(g), 255 - int(r)), 2)

    cv2.imshow("Color Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
