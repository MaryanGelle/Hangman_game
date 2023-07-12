import gspread
from google.oath2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman-game')

# Access the worksheet within the spreadsheet
worksheet = SHEET.Score

# Read top ten ranks from the leaderboard
def read_top_ten():
    top_ten = worksheet.get('A2:C11')  
    return top_ten

# Update the top ten ranks and user's score
def update_leaderboard(name, score):
    top_ten = worksheet.get('A2:C11') 

    # Check if the user's score qualifies for the top ten
    if score > top_ten[-1][2]:
        # Insert the user's score in the correct position
        for i, row in enumerate(top_ten):
            if score > row[2]:
                top_ten.insert(i, [i+1, name, score])
                break

        # Remove the lowest score to maintain the top ten ranks
        top_ten.pop()

        # Update the leaderboard in the spreadsheet
        cell_list = worksheet.range('A2:C11')
        for i, cell in enumerate(cell_list):
            cell.value = top_ten[i // 3][i % 3]
        worksheet.update_cells(cell_list)

# Example usage
top_ten_data = read_top_ten()
print(top_ten_data)

user_name = "Maay"
user_score = 40
update_leaderboard(user_name, user_score)