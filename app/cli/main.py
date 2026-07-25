from app.config.settings import load_settings


def main():
    settings = load_settings()

    print("Media Organiser")
    print("================")
    print(settings)


if __name__ == "__main__":
    main()

