from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
import emoji

def test_emoji():
    print(emoji.emojize("Python is my :red_heart:", variant="emoji_type"))

if __name__ == '__main__':
    print(f'Date time is: {datetime.now()}')
    test_emoji()
    get_employees(6, 2, 3)
    calculate_salary(4)