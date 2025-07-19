# src/prompt_maker.py

def prompt_text_to_image(desc: str) -> str:
    return f"Generate a hyper-realistic image based on this idea: {desc}. Use cinematic lighting and high detail."

def prompt_text_to_video(desc: str, veo_version="veo3") -> str:
    return f"[{veo_version.upper()}][9:16][1080p60] A cinematic video showing: {desc}. Add dynamic camera, real footage style, and tension."

def prompt_text_to_audio(desc: str) -> str:
    return f"Create a sound effect that matches: {desc}. Include ambient tone and dramatic elements."

def prompt_video_to_prompt_text(video_title: str) -> str:
    return f"Extract the visual and emotional essence from video titled '{video_title}' into a detailed cinematic prompt."

if __name__ == "__main__":
    print(prompt_text_to_image("A skull-faced AI preman standing in an alley with glowing eyes and smoke."))
