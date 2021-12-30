import pandas as pd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df = pd.read_excel(r'C:\Users\Gameslay\Documents\GitHub\excel-manipulation\gecko_export_template.xlsx', usecols='A:N')  # convert excel to dataframe

    # assign variables to columns
    alumni_number = df['Alumni number']
    name = df['Full name']
    email = df['Email address']
    phone = df['Telephone']
    linkedin = df['LinkedIn URL']
    address = df['Address']
    address1 = df['Address_1']
    address2 = df['Address_2']
    address3 = df['Address_3']
    address4 = df['Address_4']
    address5 = df['Address_5']
    job_title = df['Job title']
    employer = df['Employer\'s name']
    industry = df['Industry']

    address_import_id = 1  # insert date (291221-01)
    import_id = None
    phone_type = 'mobile updated'
    email_type = 'email updated'
    linkedin_type = 'LinkedIn updated'

    new_df = pd.DataFrame(df, columns=['Alumni number', 'Email address'])
    print(new_df)
