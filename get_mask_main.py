import os
from ultralytics import YOLO
from PIL import Image

# YOLO 모델 로드
yolo_model = YOLO("models/Oil_Tank_Shadow_Detect_Model_v3.pt")

# 추론할 이미지가 있는 폴더 경로 지정
image_folder = "Dataset/test/test_A/"  # 원하는 이미지 폴더 경로로 수정

# 결과 이미지를 저장할 폴더 경로 지정
output_folder = "Dataset/test/test_B/"  # 원하는 결과 이미지 폴더 경로로 수정

# 이미지 폴더 내의 모든 이미지 파일에 대해 추론 및 저장
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 이미지 파일 경로
        image_path = os.path.join(image_folder, filename)

        # 이미지 추론
        results = yolo_model.predict(image_path)
        result = results[0]
        masks = result.masks

        # 모든 마스크 이미지를 하나로 병합
        combined_mask = sum(mask.data[0].cpu().numpy() for mask in masks)

        # 이미지로 변환
        combined_mask_img = Image.fromarray(combined_mask.astype('uint8') * 255, "L")

        # 결과 이미지 파일명 지정 (순차적으로 번호 붙임)
        output_filename = f"{filename.split('.')[0]}.png"

        # 결과 이미지 파일 경로
        output_path = os.path.join(output_folder, output_filename)

        # 결과 이미지 저장
        combined_mask_img.save(output_path, format="PNG")
