# src/removal_tools.py

def remove_background(image_path: str) -> str:
    """
    Simulasi hapus background gambar.
    Return path gambar hasil tanpa background.
    """
    # Nanti pake API atau library sebenarnya
    return f"Background removed from {image_path}"

def remove_watermark(image_path: str) -> str:
    """
    Simulasi unlock watermark dari gambar.
    Return path gambar hasil tanpa watermark.
    """
    # Hati-hati bro, ini rahasia preman
    return f"Watermark removed from {image_path}"

if __name__ == "__main__":
    print(remove_background("sample.jpg"))
    print(remove_watermark("sample_watermark.jpg"))
