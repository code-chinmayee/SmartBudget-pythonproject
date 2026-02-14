from database import create_tables
from frontend import handle_user_choice

def main():
    create_tables()
    handle_user_choice()

if __name__ == "__main__":
    main()
