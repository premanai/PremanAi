# src/video_tools.py

def video_to_audio(video_path: str) -> str:
    """
    Simulasi ekstrak audio dari video.
    Return path file audio hasil ekstrak.
    """
    return f"Audio extracted from {video_path}"

def video_to_images(video_path: str) -> list[str]:
    """
    Simulasi ekstrak frame gambar dari video.
    Return list path gambar hasil ekstrak.
    """
    return [f"{video_path}_frame1.jpg", f"{video_path}_frame2.jpg"]

def video_to_prompt_text(video_title: str) -> str:
    """
    Simulasi generate prompt text dari video.
    """
    return f"Detailed cinematic prompt based on video titled '{video_title}'."

if __name__ == "__main__":
    print(video_to_audio("disaster.mp4"))
    print(video_to_images("disaster.mp4"))
    print(video_to_prompt_text("Epic Volcano Eruption"))
