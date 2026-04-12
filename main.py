import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from udemy-langchain-course!")
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is not set")
    else:
        print("All API keys loaded successfully")


if __name__ == "__main__":
    main()
