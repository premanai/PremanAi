# src/hashtag_gen.py

def generate_normal_hashtags(topic: str) -> list[str]:
    """Hashtag standar berdasarkan topik"""
    tags = [f"#{topic}", f"#{topic}Life", f"#{topic}Vibes"]
    return tags

def generate_absurd_hashtags(topic: str) -> list[str]:
    """Hashtag absurd dan lucu"""
    tags = [f"#{topic}Ngaceng", f"#{topic}SokJago", f"#{topic}GakJelas"]
    return tags

def generate_seo_friendly_hashtags(topic: str) -> list[str]:
    """Hashtag SEO friendly yang relevan"""
    tags = [f"#{topic}", f"#{topic}Tutorial", f"#{topic}Tips", f"#{topic}HowTo"]
    return tags

def generate_auto_scan_video_hashtags(video_title: str) -> list[str]:
    """Simulasi auto scan video buat generate hashtag"""
    # Nanti diintegrasi AI scan konten video sebenarnya
    base = video_title.lower().replace(" ", "")
    tags = [f"#{base}", f"#{base}Viral", f"#{base}Trending"]
    return tags

if __name__ == "__main__":
    topic = "PremanAi"
    print("Normal:", generate_normal_hashtags(topic))
    print("Absurd:", generate_absurd_hashtags(topic))
    print("SEO:", generate_seo_friendly_hashtags(topic))
    print("Auto Scan:", generate_auto_scan_video_hashtags("Epic Disaster Video"))
