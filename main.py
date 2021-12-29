import pandas as pd


def open_file():
    df = pd.read_excel(r'C:\Users\Gameslay\Downloads\car inventory.xlsx', usecols='A')
    print(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    open_file()
