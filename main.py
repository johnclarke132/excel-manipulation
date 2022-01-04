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
def create_phone_type_id(update_type):
    rows = []
    for i in range(len(df.index)):
        rows.append(update_type)
    phone_type_id = pd.DataFrame(rows)
    return phone_type_id


def create_address(main_df):
    return main_df['Address'] + '/n' + main_df['Address_1'] + '/n' + main_df['Address_2']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # convert excel to dataframe
    df = pd.read_excel(r'C:\Users\Gameslay\Documents\GitHub\excel-manipulation\gecko_export_template.xlsx', dtype=str, usecols='A:N')

    # create column data and add to dataframe
    df = pd.DataFrame(df, columns=['Alumni number', 'Email address', 'Telephone', 'LinkedIn URL', 'Address', 'Address_1', 'Address_2'])
    df['PhoneAddrImpID'] = create_addr_imp_id()
    df['PhoneImpID'] = None
    df['Phone Type 1'] = create_phone_type_id('email updated')
    df['Phone Type 2'] = create_phone_type_id('mobile updated')
    df['Phone Type 3'] = create_phone_type_id('LinkedIn updated')
    df['AddrLines'] = create_address(df)

    # rearrange dataframe into desired output
    df = df[['Alumni number',
             'Email address', 'PhoneAddrImpID', 'PhoneImpID', 'Phone Type 1',
             'Telephone', 'PhoneAddrImpID', 'PhoneImpID', 'Phone Type 2',
             'LinkedIn URL', 'PhoneAddrImpID', 'PhoneImpID', 'Phone Type 3',
             'AddrLines']]

    # view full dataframe
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(df)
