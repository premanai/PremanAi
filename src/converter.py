# src/converter.py

def flip_image(image_path: str, direction="horizontal") -> str:
    """
    Fungsi simulasi flip gambar.
    direction: "horizontal" atau "vertical"
    Return: path file gambar hasil flip
    """
    # Simulasi logika flip (replace dengan library nyata nanti)
    return f"Image flipped {direction} from {image_path}"

def text_to_pdf(text: str, output_path: str) -> str:
    """
    Fungsi simulasi konversi teks ke PDF.
    Return: path file PDF hasil konversi
    """
    # Simulasi saja
    return f"PDF saved to {output_path}"

if __name__ == "__main__":
    print(flip_image("sample.jpg"))
    print(text_to_pdf("Ini contoh teks", "output.pdf"))
