import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from preman_core import prompt_text_to_image

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <text_prompt>")
        sys.exit(1)

    prompt = sys.argv[1]
    result = prompt_text_to_image(prompt)
    print(f"PremanAi Prompt Result: {result}")

if __name__ == "__main__":
    main()
