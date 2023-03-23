# def main(table):
#     # Удаление пустых столбцов
#     non_empty_columns = [i for i, column in enumerate(zip(*table))
#                          if any(cell is not None for cell in column)]
#     table = [[row[i] for i in non_empty_columns] for row in table]
#
#     # Удаление пустых строк
#     table = [row for row in table if any(cell is not None for cell in row)]
#
#     # Преобразование содержимого ячеек
#     for row in table:
#         # Преобразование email
#         email_parts = row[0].split('[at]')
#         row[0] = email_parts[-1]
#
#         # Преобразование телефона
#         phone = row[1].replace(' ', '').replace('-', '')
#         row[1] = '{}{} {}{}{} {}{}{}-{}{}{}{}'.format(*phone)
#
#         # Преобразование даты
#         date_parts = row[2].split('/')
#         day = int(date_parts[0])
#         month = int(date_parts[1])
#         year = int(date_parts[2])
#         if year > 2000:
#             year -= 2000
#         else:
#             year -= 1900
#         row[2] = '{:02d}.{:02d}.{:02d}'.format(year, month, day)
#     return table


# def main(table):
#     # Удаление пустых столбцов
#     non_empty_columns = []
#     for i, column in enumerate(zip(*table)):
#         if any(cell is not None for cell in column):
#             non_empty_columns.append(i)
#     new_table = []
#     for row in table:
#         new_row = []
#         for i in non_empty_columns:
#             new_row.append(row[i])
#         if any(cell is not None for cell in new_row):
#             new_table.append(new_row)
#
#     # Удаление пустых строк
#     new_table = [row for row in new_table if any(cell is not None for cell in row)]
#
#     # Преобразование содержимого ячеек
#     for row in new_table:
#         # Преобразование email
#         email_parts = row[0].split('[at]')
#         row[0] = email_parts[-1]
#
#         # Преобразование телефона
#         phone = row[1].replace(' ', '').replace('-', '')
#         row[1] = '{}{} {}{}{} {}{}{}-{}{}{}{}'.format(phone[0],
#                                                       phone[1],
#                                                       phone[2],
#                                                       phone[3],
#                                                       phone[4],
#                                                       phone[5],
#                                                       phone[6],
#                                                       phone[7],
#                                                       phone[8],
#                                                       phone[9],
#                                                       phone[10],
#                                                       phone[11])
#
#         # Преобразование даты
#         date_parts = row[2].split('/')
#         day = int(date_parts[0])
#         month = int(date_parts[1])
#         year = int(date_parts[2])
#         if year > 2000:
#             year -= 2000
#         else:
#             year -= 1900
#         row[2] = '{:02d}.{:02d}.{:02d}'.format(year, month, day)
#     return new_table


def remove_empty_columns(table):
    non_empty_columns = []
    for i, column in enumerate(zip(*table)):
        if any(cell is not None for cell in column):
            non_empty_columns.append(i)
    return [[row[i] for i in non_empty_columns] for row in table]


def remove_empty_rows(table):
    return [row for row in table if any(cell is not None for cell in row)]


def transform_email(email):
    return email.split('[at]')[-1]


def transform_phone(phone):
    phone = phone.replace(' ', '').replace('-', '')
    return '{}{} {}{}{} {}{}{}-{}{}{}{}'.format(phone[0],
                                                phone[1],
                                                phone[2],
                                                phone[3],
                                                phone[4],
                                                phone[5],
                                                phone[6],
                                                phone[7],
                                                phone[8],
                                                phone[9],
                                                phone[10],
                                                phone[11])


def transform_date(date):
    date_parts = date.split('/')
    day, month, year = map(int, date_parts)
    year -= 2000 if year >= 2000 else 1900
    return '{:02d}.{:02d}.{:02d}'.format(year, month, day)


def transform_table(table):
    table = remove_empty_columns(table)
    table = remove_empty_rows(table)
    for row in table:
        row[0] = transform_email(row[0])
        row[1] = transform_phone(row[1])
        row[2] = transform_date(row[2])
    return table


def main(table):
    return transform_table(table)


table = [
    ['bubman79[at]rambler.ru', '+7 963 221-51-34', None, '18/02/2000'],
    ['masko62[at]yahoo.com', '+7 163 048-11-86', None, '23/01/2003'],
    [None, None, None, None],
    ['dozanz8[at]yahoo.com', '+7 292 123-59-04', None, '25/10/1999'],
    ['tamumij17[at]rambler.ru', '+7 829 301-92-40', None, '01/01/2001']
]
# table = [
#     ['cazizman83[at]mail.ru', '+7 727 374-18-83', None, '13/07/2002'],
#     ['sulemli30[at]mail.ru', '+7 468 360-25-06', None, '28/11/2002'],
#     ['kelegko20[at]rambler.ru', '+7 356 997-98-57', None, '01/06/1999']
# ]

result = main(table)

for row in result:
    print('\t'.join(str(cell) for cell in row))
