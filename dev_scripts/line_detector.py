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
cv2.createTrackbar('minLineLength', 'Line Detection', 20, 200, lambda x: None)
cv2.createTrackbar('maxLineGap', 'Line Detection', 20, 100, lambda x: None)
cv2.createTrackbar('threshold', 'Line Detection', 30, 200, lambda x: None)
cv2.createTrackbar('edge_dist_thresh', 'Line Detection', 5, 30, lambda x: None)  # Umbral para agrupar líneas cercanas
cv2.createTrackbar('line_width_max', 'Line Detection', 30, 100, lambda x: None)  # Ancho máximo esperado de la línea

# Para visualización
def draw_crosshair(image, x, y, color=(0, 255, 0), size=10):
    cv2.line(image, (x - size, y), (x + size, y), color, 2)
    cv2.line(image, (x, y - size), (x, y + size), color, 2)

# Función para agrupar líneas por proximidad
def group_lines_by_proximity(lines, proximity_threshold):
    if not lines:
        return []
        
    # Ordenar líneas por posición x
    lines.sort(key=lambda x: x['midpoint'][0])
    
    groups = []
    current_group = [lines[0]]
    
    for i in range(1, len(lines)):
        current_line = lines[i]
        prev_line = current_group[-1]
        
        # Si la línea actual está muy cerca de la anterior, la consideramos parte del mismo borde
        if abs(current_line['midpoint'][0] - prev_line['midpoint'][0]) <= proximity_threshold:
            current_group.append(current_line)
        else:
            # Si no, iniciamos un nuevo grupo
            groups.append(current_group)
            current_group = [current_line]
    
    # Agregar el último grupo
    if current_group:
        groups.append(current_group)
    
    return groups

# Función para identificar los bordes izquierdo y derecho
def identify_edges(line_groups, max_line_width):
    if not line_groups:
        return None, None
    
    # Si solo hay un grupo, ese es nuestro único borde detectado
    if len(line_groups) == 1:
        # Calcular la posición media de las líneas en este grupo
        avg_x = sum(line['midpoint'][0] for line in line_groups[0]) / len(line_groups[0])
        return [avg_x], None
    
    # Calcular la posición media de cada grupo
    group_positions = []
    for group in line_groups:
        avg_x = sum(line['midpoint'][0] for line in group) / len(group)
        group_positions.append(avg_x)
    
    # Ordenar las posiciones de los grupos
    group_positions.sort()
    
    # Identificar potenciales pares de bordes
    edge_pairs = []
    for i in range(len(group_positions) - 1):
        for j in range(i + 1, len(group_positions)):
            width = group_positions[j] - group_positions[i]
            if width > 0 and width <= max_line_width:
                edge_pairs.append((i, j, width))
    
    # Si no encontramos pares, usamos los dos bordes más cercanos al centro
    if not edge_pairs:
        # Usar los dos grupos más cercanos entre sí que estén dentro del ancho máximo
        min_distance = float('inf')
        left_idx, right_idx = 0, 1  # Por defecto, los dos primeros
        
        for i in range(len(group_positions) - 1):
            distance = group_positions[i+1] - group_positions[i]
            if distance < min_distance and distance <= max_line_width:
                min_distance = distance
                left_idx, right_idx = i, i+1
        
        return [group_positions[left_idx]], [group_positions[right_idx]]
    
    # Ordenar pares por ancho (preferimos los que tienen un ancho razonable)
    edge_pairs.sort(key=lambda x: x[2])
    
    # Seleccionar el mejor par (el que tiene el ancho más apropiado)
    best_pair = edge_pairs[0]
    left_idx, right_idx = best_pair[0], best_pair[1]
    
    return [group_positions[left_idx]], [group_positions[right_idx]]

while True:
    # Leer valores actuales de los trackbars para HSV
    h_min = cv2.getTrackbarPos('H min', 'HSV Control')
    h_max = cv2.getTrackbarPos('H max', 'HSV Control')
    s_min = cv2.getTrackbarPos('S min', 'HSV Control')
    s_max = cv2.getTrackbarPos('S max', 'HSV Control')
    v_min = cv2.getTrackbarPos('V min', 'HSV Control')
    v_max = cv2.getTrackbarPos('V max', 'HSV Control')
    
    # Leer valores para la detección de líneas
    min_line_length = cv2.getTrackbarPos('minLineLength', 'Line Detection')
    max_line_gap = cv2.getTrackbarPos('maxLineGap', 'Line Detection')
    threshold = cv2.getTrackbarPos('threshold', 'Line Detection')
    edge_proximity_threshold = cv2.getTrackbarPos('edge_dist_thresh', 'Line Detection')
    max_line_width = cv2.getTrackbarPos('line_width_max', 'Line Detection')
    
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo leer el fotograma.")
        break
        
    display_frame = frame.copy()
    
    # Convertir a HSV y aplicar un suavizado para reducir el ruido
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    # Definir rango para azul celeste usando los trackbars
    lower_blue = np.array([h_min, s_min, v_min])
    upper_blue = np.array([h_max, s_max, v_max])
    
    # Crear máscara y aplicar operaciones morfológicas para mejorar la detección
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Operaciones morfológicas para limpiar la máscara
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # Detectar bordes y líneas
    edges = cv2.Canny(mask, 50, 150, apertureSize=3)
    
    # Usar valores ajustados para detectar líneas pequeñas
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold, 
                           minLineLength=min_line_length, 
                           maxLineGap=max_line_gap)
    
    image_center = frame.shape[1] // 2
    image_height = frame.shape[0]
    
    # Dibujar línea central de referencia
    cv2.line(display_frame, (image_center, 0), (image_center, image_height), (255, 0, 0), 1)
    
    x_data = None
    jaw = None
    
    if lines is not None:
        # Extraer todas las líneas detectadas
        all_lines = []
        for line in lines:
            x1, y1, x2, y2 = line[0]
            
            # Calcular ángulo para filtrar líneas horizontales
            angle = abs(np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi)
            
            # Enfocarnos en líneas más verticales (puedes ajustar estos valores)
            if angle < 45 or angle > 135:  # Solo líneas verticales
                # Calcular el punto medio de la línea
                mid_x = (x1 + x2) // 2
                mid_y = (y1 + y2) // 2
                
                # Almacenar línea y sus propiedades
                all_lines.append({
                    'points': (x1, y1, x2, y2),
                    'angle': angle,
                    'midpoint': (mid_x, mid_y),
                    'distance': abs(mid_x - image_center)
                })
        
        # Agrupar líneas que están muy cerca horizontalmente (mismo borde)
        line_groups = group_lines_by_proximity(all_lines, edge_proximity_threshold)
        
        # Identificar los bordes izquierdo y derecho
        left_edge_positions, right_edge_positions = identify_edges(line_groups, max_line_width)
        
        # Si tenemos al menos un borde
        if left_edge_positions:
            # Dibujar y calcular la posición basada en los bordes detectados
            left_edge_position = sum(left_edge_positions) / len(left_edge_positions)
            
            # Dibujar línea en el borde izquierdo
            for group_idx, group in enumerate(line_groups):
                avg_x = sum(line['midpoint'][0] for line in group) / len(group)
                if abs(avg_x - left_edge_position) < 1:  # Si este grupo corresponde al borde izquierdo
                    for line in group:
                        x1, y1, x2, y2 = line['points']
                        cv2.line(display_frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Borde izquierdo en azul
            
            # Si tenemos ambos bordes
            if right_edge_positions:
                right_edge_position = sum(right_edge_positions) / len(right_edge_positions)
                
                # Dibujar línea en el borde derecho
                for group_idx, group in enumerate(line_groups):
                    avg_x = sum(line['midpoint'][0] for line in group) / len(group)
                    if abs(avg_x - right_edge_position) < 1:  # Si este grupo corresponde al borde derecho
                        for line in group:
                            x1, y1, x2, y2 = line['points']
                            cv2.line(display_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Borde derecho en rojo
                
                # Calcular el centro entre los dos bordes
                x_data = (left_edge_position + right_edge_position) / 2
                
                # Calcular el ancho de la línea
                line_width = right_edge_position - left_edge_position
                cv2.putText(display_frame, f"Width: {line_width:.1f}px", (10, 120), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            else:
                # Si solo tenemos el borde izquierdo
                x_data = left_edge_position
            
            # Calcular jaw
            jaw = x_data - image_center
            
            # Encontrar una posición y promedio para dibujar la cruz
            avg_y = 0
            count = 0
            
            for group in line_groups:
                for line in group:
                    mid_x, mid_y = line['midpoint']
                    avg_y += mid_y
                    count += 1
            
            if count > 0:
                avg_y = avg_y / count
                
            # Dibujar cruz en el centro calculado
            draw_crosshair(display_frame, int(x_data), int(avg_y), color=(0, 255, 255))
            
            # Información sobre la línea detectada
            num_edges = 2 if right_edge_positions else 1
            cv2.putText(display_frame, f"Edges: {num_edges}", (10, 90), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            
            # Mostrar datos en la imagen
            cv2.putText(display_frame, f"x: {x_data:.1f}, jaw: {jaw:.1f}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            print(f"x: {x_data:.1f}, jaw: {jaw:.1f}")
        else:
            cv2.putText(display_frame, "No edges detected", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print("x: None, jaw: None")
    else:
        cv2.putText(display_frame, "No lines detected", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print("x: None, jaw: None")
    
    # Mostrar imágenes
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Edges", edges)
    cv2.imshow("Line Detection", display_frame)
    
    # Mostrar valores HSV actuales
    hsv_info = f"HSV Range: [{h_min},{s_min},{v_min}] to [{h_max},{s_max},{v_max}]"
    cv2.putText(display_frame, hsv_info, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
