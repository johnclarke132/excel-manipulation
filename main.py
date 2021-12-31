import pandas as pd
import datetime


# create unique ID for each row using current date
def create_addr_imp_id():
    rows = []
    counter = 0
    date = datetime.datetime.now().strftime('%d%m%y')

    for i in range(len(df.index)):
        counter += 1
        addr_imp_id = date + '-' + str(counter)
        rows.append(addr_imp_id)
    addr_imp_id = pd.DataFrame(rows)
    return addr_imp_id


# populate each row with comment if mobile given
def create_phone_type_id():
    rows = []
    for i in range(len(df.index)):
        rows.append('mobile updated')
    phone_type_id = pd.DataFrame(rows)
    return phone_type_id


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df = pd.read_excel(r'C:\Users\Gameslay\Documents\GitHub\excel-manipulation\gecko_export_template.xlsx', usecols='A:N')  # convert excel to dataframe

    new_df = pd.DataFrame(df, columns=['Alumni number', 'Email address'])
    new_df['PhoneAddrImpID'] = create_addr_imp_id()
    new_df['PhoneImpID'] = None
    new_df['Phone Type'] = create_phone_type_id()

    # view full dataframe
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(new_df)
