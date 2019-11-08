import csv
import pandas as pd

with open("basic_income_dataset_dalia.csv", newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

#
#
    # before starting the counting in the for loop, the values for males and females are zero

    # male = 0
    # female = 0
    #
    # for row in csvreader:
    #     if row[3] == 'male':
    #         male += 1               # this counts the number of males who took part in the opinion poll
    #     elif row[3] == 'female':
    #         female += 1             # this counts the number of females who took part in the opinion poll
    #
    # print("There are", male, "males who took part in the poll")
    # print("There are", female, "females who took part in the poll")
#
#
    ## The code will do a count the number of country (codes) in my csv file and put them in a list

#     country = []
#     country_num = 0
#     for row in csvreader:
#         if row[0] == 'country_code':
#             pass
#         elif row[0] not in country:
#             country.append(row[0])
#             country_num += 1
#
#
# print(country)
# print(country_num)
#
#
#    ## The code will do a count of people in each counrty who would potentially vote for UBI
#    ##  The v
#     AT = 0
#     BE = 0
#     BG = 0
#     CY = 0
#     CZ = 0
#     DE = 0
#     DK = 0
#     EE = 0
#     ES = 0
#     FI = 0
#     FR = 0
#     GB = 0
#     GR = 0
#     HR = 0
#     HU = 0
#     IE = 0
#     IT = 0
#     LT = 0
#     LU = 0
#     LV = 0
#     MT = 0
#     NL = 0
#     PL = 0
#     PT = 0
#     RO = 0
#     SE = 0
#     SI = 0
#     SK = 0
#
#     for row in csvreader:
#         if row[0] == 'AT' and row[9].find('for') != -1:
#             AT += 1
#             print(row)
#         elif row[0] == 'BE' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             BE += 1
#         elif row[0] == 'BG' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             BG += 1
#         elif row[0] == 'CY' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             CY += 1
#         elif row[0] == 'CZ' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             CZ += 1
#         elif row[0] == 'DE' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             DE += 1
#         elif row[0] == 'DK' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             DK += 1
#         elif row[0] == 'EE' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             EE += 1
#         elif row[0] == 'ES' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             ES += 1
#         elif row[0] == 'FI' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             FI += 1
#         elif row[0] == 'FR' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             FR += 1
#         elif row[0] == 'GB' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             GB += 1
#         elif row[0] == 'GR' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             GR += 1
#         elif row[0] == 'HR' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             HR += 1
#         elif row[0] == 'HU' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             HU += 1
#         elif row[0] == 'IE' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             IE += 1
#         elif row[0] == 'IT' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             IT += 1
#         elif row[0] == 'LT' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             LT += 1
#         elif row[0] == 'LU' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             LU += 1
#         elif row[0] == 'LV' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             LV += 1
#         elif row[0] == 'MT' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             MT += 1
#         elif row[0] == 'NL' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             NL += 1
#         elif row[0] == 'PL' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             PL += 1
#         elif row[0] == 'PT' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             PT += 1
#         elif row[0] == 'RO' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             RO += 1
#         elif row[0] == 'SE' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             SE += 1
#         elif row[0] == 'SI' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             SI += 1
#         elif row[0] == 'SK' and (row[9].find('I would probably vote for it') or row[9].find('I would vote for it')):
#             SK += 1
#
#
#
# print("In AT", AT)
# print("In BE", BE)
# print("In BG", BG)
# print("In CY", CY)
# print("In CZ", CZ)
# print("In DE", DE)
# print("In DK", DK)
# print("In EE", EE)
# print("In ES", ES)
# print("In Finland", FI)
# print("In France", FR)
# print("In Great Britain", GB)
# print("In Germany", GR)
# print("In HR", HR)
# print("In HU", HU)
# print("In IE", IE)
# print("In IT", IT)
# print("In LT", LT)
# print("In LU", LU)
# print("In LV", LV)
# print("In MT", MT)
# print("In NL", NL)
# print("In PL", PL)
# print("In PT", PT)
# print("In RO", RO)
# print("In SE", SE)
# print("In SI", SI)
# print("In SK", SK)
# #

    AT = 0
    BE = 0
    BG = 0
    CY = 0
    CZ = 0
    DE = 0
    DK = 0
    EE = 0
    ES = 0
    FI = 0
    FR = 0
    GB = 0
    GR = 0
    HR = 0
    HU = 0
    IE = 0
    IT = 0
    LT = 0
    LU = 0
    LV = 0
    MT = 0
    NL = 0
    PL = 0
    PT = 0
    RO = 0
    SE = 0
    SI = 0
    SK = 0

######### Checks which  country it is and than proceeds to check whether they would vote "FOR" or "AGAINST"

    for row in csvreader:
        if row[0] == 'AT':
            if row[9].find('vote for it') != -1:
                AT += 1
            elif row[9].find('against it') != -1:
                AT = AT - 1
        elif row[0] == 'BE':
            if row[9].find('vote for it') != -1:
                BE += 1
            elif row[9].find('against it') != -1:
                BE -= 1

        elif row[0] == 'BG':
            if row[9].find('vote for it') != -1:
                BG += 1
            elif row[9].find('I would vote against it') != -1:
                BE -= 1
        elif row[0] == 'CY':
            if row[9].find('vote for it') != -1:
                CY += 1
            elif row[9].find('I would vote against it') != -1:
                CY -= 1

        elif row[0] == 'CZ':
            if row[9].find('vote for it') != -1:
                CZ += 1
            elif row[9].find('I would vote against it') != -1:
                CZ -= 1
        elif row[0] == 'DE':
            if row[9].find('vote for it') != -1:
                DE += 1
            elif row[9].find('I would vote against it') != -1:
                DE -= 1
        elif row[0] == 'DK':
            if row[9].find('vote for it') != -1:
                DK += 1
            elif row[9].find('I would vote against it') != -1:
                DK -= 1
        elif row[0] == 'EE':
            if row[9].find('vote for it') != -1:
                EE += 1
            elif row[9].find('I would vote against it') != -1:
                EE -= 1
        elif row[0] == 'ES':
            if row[9].find('vote for it') != -1:
                ES += 1
            elif row[9].find('I would vote against it') != -1:
                ES -= 1
        elif row[0] == 'FI':
            if row[9].find('vote for it') != -1:
                FI += 1
            elif row[9].find('I would vote against it') != -1:
                FI -= 1
        elif row[0] == 'FR':
            if row[9].find('vote for it') != -1:
                FR += 1
            elif row[9].find('I would vote against it') != -1:
                FR -= 1
        elif row[0] == 'GB':
            if row[9].find('vote for it') != -1:
                GB += 1
            elif row[9].find('I would vote against it') != -1:
                GB -= 1
        elif row[0] == 'GR':
            if row[9].find('vote for it') != -1:
                GR += 1
            elif row[9].find('I would vote against it') != -1:
                GR -= 1
        elif row[0] == 'HR':
            if row[9].find('vote for it') != -1:
                HR += 1
            elif row[9].find('I would vote against it') != -1:
                HR -= 1
        elif row[0] == 'HU':
            if row[9].find('vote for it') != -1:
                HU += 1
            elif row[9].find('I would vote against it') != -1:
                HU -= 1
        elif row[0] == 'IE':
            if row[9].find('vote for it') != -1:
                IE += 1
            elif row[9].find('I would vote against it') != -1:
                IE -= 1
        elif row[0] == 'IT':
            if row[9].find('vote for it') != -1:
                IT += 1
            elif row[9].find('I would vote against it') != -1:
                IT -= 1
        elif row[0] == 'LT':
            if row[9].find('vote for it') != -1:
                LT += 1
            elif row[9].find('I would vote against it') != -1:
                LT -= 1
        elif row[0] == 'LU':
            if row[9].find('vote for it') != -1:
                LU += 1
            elif row[9].find('I would vote against it') != -1:
                LU -= 1
        elif row[0] == 'LV':
            if row[9].find('vote for it') != -1:
                LV += 1
            elif row[9].find('I would vote against it') != -1:
                LV -= 1
        elif row[0] == 'MT':
            if row[9].find('vote for it') != -1:
                MT += 1
            elif row[9].find('I would vote against it') != -1:
                MT -= 1
        elif row[0] == 'NL':
            if row[9].find('vote for it') != -1:
                NL += 1
            elif row[9].find('I would vote against it') != -1:
                NL -= 1
        elif row[0] == 'PL':
            if row[9].find('vote for it') != -1:
                PL += 1
            elif row[9].find('I would vote against it') != -1:
                PL -= 1
        elif row[0] == 'PT':
            if row[9].find('vote for it'):
                PT += 1
            elif row[9].find('I would vote against it') != -1:
                PT -= 1
        elif row[0] == 'RO':
            if row[9].find('vote for it'):
                RO += 1
            elif row[9].find('I would vote against it') != -1:
                RO -= 1
        elif row[0] == 'SE':
            if row[9].find('vote for it'):
                SE += 1
            elif row[9].find('I would vote against it') != -1:
                SE -= 1
        elif row[0] == 'SI':
            if row[9].find('vote for it'):
                SI += 1
            elif row[9].find('I would vote against it') != -1:
                SI -= 1
        elif row[0] == 'SK':
            if row[9].find('vote for it'):
                SK += 1
            elif row[9].find('I would vote against it') != -1:
                SK -= 1

    print("In AT", AT)
    print("In BE", BE)
    print("In BG", BG)
    print("In CY", CY)
    print("In CZ", CZ)
    print("In DE", DE)
    print("In DK", DK)
    print("In EE", EE)
    print("In ES", ES)
    print("In Finland", FI)
    print("In France", FR)
    print("In Great Britain", GB)
    print("In Germany", GR)
    print("In HR", HR)
    print("In HU", HU)
    print("In IE", IE)
    print("In IT", IT)
    print("In LT", LT)
    print("In LU", LU)
    print("In LV", LV)
    print("In MT", MT)
    print("In NL", NL)
    print("In PL", PL)
    print("In PT", PT)
    print("In RO", RO)
    print("In SE", SE)
    print("In SI", SI)
    print("In SK", SK)

## Using Pandas to
# UBI = pd.read_csv('basic_income_dataset_dalia.csv', delimiter=',')
# count_M_F = UBI.count('country_code').groupby('country_code')
# print(count_M_F)

