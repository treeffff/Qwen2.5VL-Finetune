import os
import cv2

def extract_8_frames_from_videos(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4") and filename.startswith("Normal_"):
            video_path = os.path.join(input_dir, filename)
            video_name = os.path.splitext(filename)[0]

            cap = cv2.VideoCapture(video_path)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            if total_frames < 8:
                print(f"⚠️ {filename} 的帧数不足 8，跳过")
                cap.release()
                continue

            # 均匀选取8帧的索引
            frame_indices = [int(i * total_frames / 8) for i in range(8)]

            saved = 0
            current_frame = 0
            next_target = frame_indices[saved]

            while cap.isOpened() and saved < 8:
                ret, frame = cap.read()
                if not ret:
                    break

                if current_frame == next_target:
                    output_filename = f"{video_name}_{saved+1}.jpg"
                    output_path = os.path.join(output_dir, output_filename)
                    cv2.imwrite(output_path, frame)
                    saved += 1
                    if saved < 8:
                        next_target = frame_indices[saved]

                current_frame += 1

            cap.release()
            print(f"✅ 已处理视频 {filename}")

    print(f"\n🎉 所有视频处理完成，图片保存在：{output_dir}")
if __name__ == "__main__":
    input_directory = "/root/autodl-tmp/Qwen2.5-VL/data/data_cyf/video_data"
    output_directory = "/root/autodl-tmp/Qwen2.5-VL/data/data_cyf/frames"

    extract_8_frames_from_videos(input_directory, output_directory)