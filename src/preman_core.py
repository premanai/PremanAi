# src/preman_core.py

from prompt_maker import prompt_text_to_image, prompt_text_to_video, prompt_text_to_audio
from converter import flip_image, text_to_pdf
from removal_tools import remove_background, remove_watermark
from hashtag_gen import generate_normal_hashtags, generate_seo_friendly_hashtags
from video_tools import video_to_audio, video_to_images, video_to_prompt_text

def main():
    print("🔥 PremanAi Core Starting Up 🔥")

    # Tes prompt maker
    img_prompt = prompt_text_to_image("A dark alley with neon lights and a mysterious figure.")
    print(f"Prompt Image: {img_prompt}")

    # Tes converter
    flipped = flip_image("street_view.jpg")
    print(f"Converter Flip: {flipped}")

    # Tes removal tools
    bg_removed = remove_background("portrait.png")
    print(f"Removal BG: {bg_removed}")

    # Tes hashtag
    hashtags = generate_seo_friendly_hashtags("PremanAi")
    print(f"Hashtags SEO Friendly: {hashtags}")

    # Tes video tools
    audio_path = video_to_audio("action_scene.mp4")
    print(f"Video to Audio: {audio_path}")

if __name__ == "__main__":
    main()

