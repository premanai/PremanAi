import argparse
from src import preman_core

def main():
    parser = argparse.ArgumentParser(description="PremanAi CLI - Bot AI gaya preman")
    
    parser.add_argument("--image-prompt", type=str, help="Buat prompt text to image")
    parser.add_argument("--flip-image", type=str, help="Flip gambar, contoh: --flip-image street.jpg")
    parser.add_argument("--remove-bg", type=str, help="Hapus background gambar")
    parser.add_argument("--generate-hashtag", type=str, help="Generate hashtag dari topik")

    args = parser.parse_args()

    if args.image_prompt:
        result = preman_core.prompt_text_to_image(args.image_prompt)
        print(f"[PremanAi] Prompt Image: {result}")

    elif args.flip_image:
        result = preman_core.flip_image(args.flip_image)
        print(f"[PremanAi] Flipped Image: {result}")

    elif args.remove_bg:
        result = preman_core.remove_background(args.remove_bg)
        print(f"[PremanAi] Background Removed: {result}")

    elif args.generate_hashtag:
        tags = preman_core.generate_seo_friendly_hashtags(args.generate_hashtag)
        print(f"[PremanAi] Hashtags: {' '.join(tags)}")

    else:
        print("[PremanAi] Gak ngerti bro, cobain opsi lain. Ketik --help buat liat menu.")

if __name__ == "__main__":
    main()
