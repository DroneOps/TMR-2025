import cv2
import numpy as np

# Configuración de la cámara
cap = cv2.VideoCapture(2)

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error: No se puede acceder a la cámara.")
    exit()

# Crear ventanas para ajustar parámetros
cv2.namedWindow('HSV Control')
# Configurar valores iniciales más amplios para azul celeste
cv2.createTrackbar('H min', 'HSV Control', 85, 179, lambda x: None)
cv2.createTrackbar('H max', 'HSV Control', 115, 179, lambda x: None)
cv2.createTrackbar('S min', 'HSV Control', 70, 255, lambda x: None)
cv2.createTrackbar('S max', 'HSV Control', 255, 255, lambda x: None)
cv2.createTrackbar('V min', 'HSV Control', 150, 255, lambda x: None)
cv2.createTrackbar('V max', 'HSV Control', 255, 255, lambda x: None)

cv2.namedWindow('Line Detection')
cv2.createTrackbar('Canny Threshold1', 'Line Detection', 50, 255, lambda x: None)
cv2.createTrackbar('Canny Threshold2', 'Line Detection', 150, 255, lambda x: None)
cv2.createTrackbar('minLineLength', 'Line Detection', 50, 300, lambda x: None)
cv2.createTrackbar('maxLineGap', 'Line Detection', 20, 100, lambda x: None)
cv2.createTrackbar('houghThreshold', 'Line Detection', 20, 100, lambda x: None)
cv2.createTrackbar('min_parallel_dist', 'Line Detection', 30, 400, lambda x: None)  # Distancia mínima entre líneas paralelas
cv2.createTrackbar('max_parallel_dist', 'Line Detection', 200, 400, lambda x: None)  # Distancia máxima entre líneas paralelas
cv2.createTrackbar('px_per_mm', 'Line Detection', 10, 50, lambda x: None)  # Calibración: píxeles por mm

# Para visualización
def draw_crosshair(image, x, y, color=(0, 255, 0), size=10):
    cv2.line(image, (x - size, y), (x + size, y), color, 2)
    cv2.line(image, (x, y - size), (x, y + size), color, 2)

# Función para mejorar la detección de colores en diferentes condiciones de iluminación
def enhance_blue_detection(hsv_image):
    # Extraer cada canal por separado
    h, s, v = cv2.split(hsv_image)
    
    # Mejorar el contraste en el canal H para hacer el azul más distintivo
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    h = clahe.apply(h)
    
    # Mejorar el canal de saturación para hacer los colores más vivos
    s = clahe.apply(s)
    
    # Recombinar los canales
    enhanced_hsv = cv2.merge([h, s, v])
    return enhanced_hsv

# Función para detectar líneas en la máscara usando HoughLinesP
def detect_lines_in_mask(mask, display_image=None):
    # Aplicar detección de bordes Canny a la máscara
    canny_threshold1 = cv2.getTrackbarPos('Canny Threshold1', 'Line Detection')
    canny_threshold2 = cv2.getTrackbarPos('Canny Threshold2', 'Line Detection')
    edges = cv2.Canny(mask, canny_threshold1, canny_threshold2)
    
    # Mostrar bordes para depuración
    if display_image is not None:
        # Crear una copia temporal para mostrar bordes Canny
        canny_debug = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
        # Mostrar el resultado de Canny en una esquina pequeña
        h, w = display_image.shape[:2]
        small_canny = cv2.resize(canny_debug, (w//4, h//4))
        display_image[0:h//4, 0:w//4] = small_canny
    
    # Detectar líneas usando HoughLinesP
    min_line_length = cv2.getTrackbarPos('minLineLength', 'Line Detection')
    max_line_gap = cv2.getTrackbarPos('maxLineGap', 'Line Detection')
    threshold = cv2.getTrackbarPos('houghThreshold', 'Line Detection')
    
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold, None, min_line_length, max_line_gap)
    
    # Lista para almacenar información de líneas
    line_info = []
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            
            # Calcular longitud, pendiente y ángulo
            length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            
            # Evitar división por cero para líneas horizontales
            if x2 - x1 == 0:
                angle = 90.0
            else:
                slope = (y2 - y1) / (x2 - x1)
                angle = np.degrees(np.arctan(slope))
            
            # Calcular punto medio
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            
            # Agregar información de la línea
            line_info.append({
                'points': (x1, y1, x2, y2),
                'length': length,
                'angle': angle,
                'midpoint': (mid_x, mid_y)
            })
            
            # Dibujar línea para depuración
            if display_image is not None:
                cv2.line(display_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    return line_info

# Función para agrupar líneas por orientación (verticales u horizontales)
def group_lines_by_orientation(lines, angle_threshold=15):
    vertical_lines = []
    horizontal_lines = []
    
    for line in lines:
        angle = line['angle']
        # Ajustar ángulos negativos
        if angle < 0:
            angle += 180
        
        # Clasificar como vertical u horizontal
        if (0 <= angle < angle_threshold) or (180 - angle_threshold < angle <= 180):
            horizontal_lines.append(line)
        elif (90 - angle_threshold < angle < 90 + angle_threshold):
            vertical_lines.append(line)
    
    # Ordenar líneas horizontales por coordenada y
    horizontal_lines.sort(key=lambda l: l['midpoint'][1])
    
    # Ordenar líneas verticales por coordenada x
    vertical_lines.sort(key=lambda l: l['midpoint'][0])
    
    return vertical_lines, horizontal_lines

# Función para encontrar pares de líneas paralelas
def find_parallel_line_pairs(lines, min_distance, max_distance):
    if len(lines) < 2:
        return None
    
    valid_pairs = []
    
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            line1 = lines[i]
            line2 = lines[j]
            
            # Calcular distancia entre líneas (usando puntos medios)
            if abs(line1['angle'] - line2['angle']) < 10:  # Asegurarse que sean aproximadamente paralelas
                # Para líneas verticales, comparar coordenada x
                distance = abs(line1['midpoint'][0] - line2['midpoint'][0])
                
                # Verificar si la distancia está dentro del rango deseado
                if min_distance <= distance <= max_distance:
                    valid_pairs.append((line1, line2, distance))
    
    # Si encontramos pares válidos, devolver el mejor (el más cercano al promedio de distancia deseada)
    if valid_pairs:
        target_distance = (min_distance + max_distance) / 2
        best_pair = min(valid_pairs, key=lambda p: abs(p[2] - target_distance))
        return best_pair
    
    return None

while True:
    # Leer valores actuales de los trackbars para HSV
    h_min = cv2.getTrackbarPos('H min', 'HSV Control')
    h_max = cv2.getTrackbarPos('H max', 'HSV Control')
    s_min = cv2.getTrackbarPos('S min', 'HSV Control')
    s_max = cv2.getTrackbarPos('S max', 'HSV Control')
    v_min = cv2.getTrackbarPos('V min', 'HSV Control')
    v_max = cv2.getTrackbarPos('V max', 'HSV Control')
    
    # Leer valores para la detección de líneas paralelas
    min_parallel_dist = cv2.getTrackbarPos('min_parallel_dist', 'Line Detection')
    max_parallel_dist = cv2.getTrackbarPos('max_parallel_dist', 'Line Detection')
    px_per_mm = cv2.getTrackbarPos('px_per_mm', 'Line Detection') / 10.0  # Ajuste a decimales
    
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo leer el fotograma.")
        break
        
    display_frame = frame.copy()
    debug_frame = frame.copy()  # Para visualización de depuración
    
    # Convertir a HSV y mejorar la detección de color
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    # Mejorar la detección del color azul
    enhanced_hsv = enhance_blue_detection(hsv)
    
    # Definir rango para azul celeste usando los trackbars
    lower_blue = np.array([h_min, s_min, v_min])
    upper_blue = np.array([h_max, s_max, v_max])
    
    # Crear máscara y aplicar operaciones morfológicas para mejorar la detección
    mask = cv2.inRange(enhanced_hsv, lower_blue, upper_blue)
    
    # Operaciones morfológicas para limpiar la máscara
    kernel = np.ones((5, 5), np.uint8)  # Kernel más grande para conectar mejor
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)  # Dilatación adicional
    
    # Detectar líneas usando Hough
    detected_lines = detect_lines_in_mask(mask, debug_frame)
    
    # Dimensiones de la imagen
    image_center_x = frame.shape[1] // 2
    image_height = frame.shape[0]
    image_width = frame.shape[1]
    
    # Dibujar línea central de referencia vertical
    cv2.line(display_frame, (image_center_x, 0), (image_center_x, image_height), (255, 0, 0), 1)
    
    # Valores por defecto
    x_data = None
    jaw = None
    status = "No edges detected"
    
    if detected_lines:
        # Agrupar líneas por orientación
        vertical_lines, horizontal_lines = group_lines_by_orientation(detected_lines)
        
        # Intentar encontrar un par de líneas verticales paralelas
        vertical_pair = find_parallel_line_pairs(vertical_lines, min_parallel_dist, max_parallel_dist)
        
        if vertical_pair:
            left_line, right_line, distance = vertical_pair
            
            # Asegurarse de que left_line es realmente la línea izquierda
            if left_line['midpoint'][0] > right_line['midpoint'][0]:
                left_line, right_line = right_line, left_line
            
            # Dibujar las líneas detectadas
            x1_left, y1_left, x2_left, y2_left = left_line['points']
            cv2.line(display_frame, (x1_left, y1_left), (x2_left, y2_left), (255, 0, 0), 2)  # Línea izquierda en azul
            
            x1_right, y1_right, x2_right, y2_right = right_line['points']
            cv2.line(display_frame, (x1_right, y1_right), (x2_right, y2_right), (0, 0, 255), 2)  # Línea derecha en rojo
            
            # Calcular el centro entre las dos líneas
            left_x = left_line['midpoint'][0]
            right_x = right_line['midpoint'][0]
            x_data = (left_x + right_x) / 2
            avg_y = (left_line['midpoint'][1] + right_line['midpoint'][1]) / 2
            
            # Calcular jaw (desviación horizontal)
            jaw = x_data - image_center_x
            
            # Dibujar cruz en el centro calculado
            draw_crosshair(display_frame, int(x_data), int(avg_y), color=(0, 255, 255))
            
            # Calcular el ancho en píxeles y en cm
            line_width_px = distance  # Ya calculamos esta distancia en find_parallel_line_pairs
            line_width_cm = (line_width_px / px_per_mm) / 10.0 if px_per_mm > 0 else 0
            
            # Determinar estado
            status = "OK"
            
            # Mostrar información
            cv2.putText(display_frame, f"x: {x_data:.1f}, jaw: {jaw:.1f}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            cv2.putText(display_frame, f"Edges: 2", (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            
            cv2.putText(display_frame, f"Width: {line_width_px:.1f}px ({line_width_cm:.1f}cm)", (10, 90), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            
            # Mostrar estado
            cv2.putText(display_frame, status, (10, 120), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            print(f"x: {x_data:.1f}, jaw: {jaw:.1f}, status: {status}, width: {line_width_cm:.1f}cm")
        else:
            cv2.putText(display_frame, "Insufficient parallel edges", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print("x: None, jaw: None, status: Insufficient parallel edges")
    else:
        cv2.putText(display_frame, "No edges detected", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print("x: None, jaw: None, status: No edges detected")
    
    # Mostrar imágenes
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Debug View", debug_frame)
    cv2.imshow("Line Detection", display_frame)
    
    # Mostrar valores HSV y calibración actuales
    hsv_info = f"HSV: [{h_min},{s_min},{v_min}] to [{h_max},{s_max},{v_max}]"
    cv2.putText(display_frame, hsv_info, (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    calib_info = f"Range: {min_parallel_dist}-{max_parallel_dist}px, Cal: {px_per_mm:.1f}px/mm"
    cv2.putText(display_frame, calib_info, (10, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()