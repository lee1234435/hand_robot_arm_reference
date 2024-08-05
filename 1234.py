import cv2
import mediapipe as mp
import time
# MediaPipe 초기화
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
# 웹캠 초기화
cap = cv2.VideoCapture(0)
prev_x, prev_y = None, None
# 화면 초기화
canvas = None
last_time = time.time()
coordinates = []
initial_hand_position = None
tracking_margin = 100  # 추적할 손의 초기 위치를 기준으로 하는 마진
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)
    current_time = time.time()
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # 랜드마크 중 손목 좌표를 가져옴
            x = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * frame.shape[1])
            y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * frame.shape[0])
            if initial_hand_position is None:
                initial_hand_position = (x, y)
            # 손이 초기 위치에서 일정 범위 내에 있는지 확인
            if initial_hand_position is not None:
                if prev_x is None or prev_y is None:
                    prev_x, prev_y = x, y
                if abs(x - prev_x) < tracking_margin and abs(y - prev_y) < tracking_margin:
                    # 경로를 따라 선 그리기
                    if canvas is None:
                        canvas = frame.copy()
                    else:
                        cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 255, 0), 3)
                    # 1초마다 좌표 표시 및 저장
                    if current_time - last_time >= 1:
                        cv2.putText(canvas, f'({x}, {y})', (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                        coordinates.append((x, y))
                        print(f'Coordinates: ({x}, {y})')
                        last_time = current_time
                    prev_x, prev_y = x, y
                    # 손 랜드마크 그리기
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    if canvas is not None:
        frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# 전체 좌표 출력
print("All coordinates captured:")
for coord in coordinates:
    print(coord)