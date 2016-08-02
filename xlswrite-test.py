#!/usr/bin/env python
# coding:utf-8

from datetime import datetime
import xlsxwriter


def sparklines2():
    workbook = xlsxwriter.Workbook('sparklines2.xlsx')

    worksheet1 = workbook.add_worksheet()
    worksheet2 = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    row = 1

    # Set the columns widths to make the output clearer.
    worksheet1.set_column('A:A', 14)
    worksheet1.set_column('B:B', 50)
    worksheet1.set_zoom(150)

    # Headings.
    worksheet1.write('A1', 'Sparkline', bold)
    worksheet1.write('B1', 'Description', bold)

    ###############################################################################
    #
    text = 'A default "line" sparkline.'

    worksheet1.add_sparkline('A2', {'range': 'Sheet2!A1:J1'})

    worksheet1.write(row, 1, text)
    row += 1


    ###############################################################################
    #
    text = 'A default "column" sparkline.'

    worksheet1.add_sparkline('A3', {'range': 'Sheet2!A2:J2',
                                    'type': 'column'})

    worksheet1.write(row, 1, text)
    row += 1


    ###############################################################################
    #
    text = 'A default "win/loss" sparkline.'

    worksheet1.add_sparkline('A4', {'range': 'Sheet2!A3:J3',
                                    'type': 'win_loss'})

    worksheet1.write(row, 1, text)
    row += 2


    ###############################################################################
    #
    text = 'Line with markers.'

    worksheet1.add_sparkline('A6', {'range': 'Sheet2!A1:J1',
                                    'markers': True})

    worksheet1.write(row, 1, text)
    row += 1


    ###############################################################################
    #
    text = 'Line with high and low points.'
    worksheet1.add_sparkline('A7', {'range': 'Sheet2!A1:J1',
                                    'high_point': True,
                                    'low_point': True})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'Line with first and last point markers.'
    worksheet1.add_sparkline('A8', {'range': 'Sheet2!A1:J1',
                                    'first_point': True,
                                    'last_point': True})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'Line with negative point markers.'
    worksheet1.add_sparkline('A9', {'range': 'Sheet2!A1:J1',
                                    'negative_points': True})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'Line with axis.'
    worksheet1.add_sparkline('A10', {'range': 'Sheet2!A1:J1',
                                     'axis': True})
    worksheet1.write(row, 1, text)
    row += 2

    ###############################################################################
    #
    text = 'Column with default style (1).'
    worksheet1.add_sparkline('A12', {'range': 'Sheet2!A2:J2',
                                     'type': 'column'})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'Column with style 2.'
    worksheet1.add_sparkline('A13', {'range': 'Sheet2!A2:J2',
                                     'type': 'column',
                                     'style': 2})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'Column with style 3.'
    worksheet1.add_sparkline('A14', {'range': 'Sheet2!A2:J2',
                                     'type': 'column',
                                     'style': 3})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'Column with style 4.'
    worksheet1.add_sparkline('A15', {'range': 'Sheet2!A2:J2',
                                     'type': 'column',
                                     'style': 4})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'Column with style 5.'
    worksheet1.add_sparkline('A16', {'range': 'Sheet2!A2:J2',
                                     'type': 'column',
                                     'style': 5})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'Column with style 6.'
    worksheet1.add_sparkline('A17', {'range': 'Sheet2!A2:J2',
                                     'type': 'column',
                                     'style': 6})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'Column with a user defined color.'
    worksheet1.add_sparkline('A18', {'range': 'Sheet2!A2:J2',
                                     'type': 'column',
                                     'series_color': '#E965E0'})
    worksheet1.write(row, 1, text)
    row += 2

    ###############################################################################
    #
    text = 'A win/loss sparkline.'
    worksheet1.add_sparkline('A20', {'range': 'Sheet2!A3:J3',
                                     'type': 'win_loss'})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'A win/loss sparkline with negative points highlighted.'
    worksheet1.add_sparkline('A21', {'range': 'Sheet2!A3:J3',
                                     'type': 'win_loss',
                                     'negative_points': True})
    worksheet1.write(row, 1, text)
    row += 2

    ###############################################################################
    #
    text = 'A left to right column (the default).'
    worksheet1.add_sparkline('A23', {'range': 'Sheet2!A4:J4',
                                     'type': 'column',
                                     'style': 20})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'A right to left column.'
    worksheet1.add_sparkline('A24', {'range': 'Sheet2!A4:J4',
                                     'type': 'column',
                                     'style': 20,
                                     'reverse': True})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    text = 'Sparkline and text in one cell.'
    worksheet1.add_sparkline('A25', {'range': 'Sheet2!A4:J4',
                                     'type': 'column',
                                     'style': 20})
    worksheet1.write(row, 0, 'Growth')
    worksheet1.write(row, 1, text)
    row += 2

    ###############################################################################
    #
    text = 'A grouped sparkline. Changes are applied to all three.'
    worksheet1.add_sparkline('A27', {'location': ['A27', 'A28', 'A29'],
                                     'range': ['Sheet2!A5:J5',
                                               'Sheet2!A6:J6',
                                               'Sheet2!A7:J7'],
                                     'markers': True})
    worksheet1.write(row, 1, text)
    row += 1

    ###############################################################################
    #
    # Create a second worksheet with data to plot.
    #
    worksheet2.set_column('A:J', 11)
    data = [
        # Simple line data.
        [-2, 2, 3, -1, 0, -2, 3, 2, 1, 0],
        # Simple column data.
        [30, 20, 33, 20, 15, 5, 5, 15, 10, 15],
        # Simple win/loss data.
        [1, 1, -1, -1, 1, -1, 1, 1, 1, -1],
        # Unbalanced histogram.
        [5, 6, 7, 10, 15, 20, 30, 50, 70, 100],
        # Data for the grouped sparkline example.
        [-2, 2, 3, -1, 0, -2, 3, 2, 1, 0],
        [3, -1, 0, -2, 3, 2, 1, 0, 2, 1],
        [0, -2, 3, 2, 1, 0, 1, 2, 3, 1],
    ]

    # Write the sample data to the worksheet.
    worksheet2.write_row('A1', data[0])
    worksheet2.write_row('A2', data[1])
    worksheet2.write_row('A3', data[2])
    worksheet2.write_row('A4', data[3])
    worksheet2.write_row('A5', data[4])
    worksheet2.write_row('A6', data[5])
    worksheet2.write_row('A7', data[6])

    workbook.close()


def sparklines1():
    workbook = xlsxwriter.Workbook('sparklines1.xlsx')
    worksheet = workbook.add_worksheet()


    # Some sample data to plot.
    data = [
        [-2, 2, 3, -1, 0],
        [30, 20, 33, 20, 15],
        [1, -1, -1, 1, -1],
    ]

    # Write the sample data to the worksheet.
    worksheet.write_row('A1', data[0])
    worksheet.write_row('A2', data[1])
    worksheet.write_row('A3', data[2])

    # Add a line sparkline (the default) with markers.
    worksheet.add_sparkline('F1', {'range': 'Sheet1!A1:E1',
                                   'markers': True})

    # Add a column sparkline with non-default style.
    worksheet.add_sparkline('F2', {'range': 'Sheet1!A2:E2',
                                   'type': 'column',
                                   'style': 12})

    # Add a win/loss sparkline with negative values highlighted.
    worksheet.add_sparkline('F3', {'range': 'Sheet1!A3:E3',
                                   'type': 'win_loss',
                                   'negative_points': True})
    workbook.close()


def test_3():
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Expenses03.xlsx')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1})

    # Add a number format for cells with money.
    money_format = workbook.add_format({'num_format': '$#,##0'})

    # Add an Excel date format.
    date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

    # Adjust the column width.
    worksheet.set_column(1, 1, 50)

    # Write some data headers.
    worksheet.write('A1', 'Item', bold)
    worksheet.write('B1', 'Date', bold)
    worksheet.write('C1', 'Cost', bold)

    # Some data we want to write to the worksheet.
    expenses = (
        ['Rent', '2013-01-13', 1000],
        ['Gas', '2013-01-14', 100],
        ['Food', '2013-01-16', 300],
        ['Gym', '2013-01-20', 50],
    )

    # Start from the first cell below the headers.
    row = 1
    col = 0

    for item, date_str, cost in expenses:
        # Convert the date string into a datetime object.
        date = datetime.strptime(date_str, "%Y-%m-%d")
        worksheet.write_string(row, col, item)
        worksheet.write_datetime(row, col + 1, date, date_format)
        worksheet.write_number(row, col + 2, cost, money_format)
        row += 1

    # Write a total using a formula.
    worksheet.write(row, 0, 'Total', bold)
    worksheet.write(row, 2, '=SUM(C2:C5)', money_format)

    workbook.close()


def test_2():
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Expenses02.xlsx')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Add a number format for cells with money.
    money = workbook.add_format({'num_format': '$#,##0'})

    # Write some data headers.
    worksheet.write('A1', 'Item', bold)
    worksheet.write('B1', 'Cost', bold)

    # Some data we want to write to the worksheet.
    expenses = (
        ['Rent', 1000],
        ['Gas', 100],
        ['Food', 300],
        ['Gym', 50],
    )

    # Start from the first cell below the headers.
    row = 1
    col = 0

    # Iterate over the data and write it out row by row.
    for item, cost in (expenses):
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, cost, money)
        row += 1

    # Write a total using a formula.
    worksheet.write(row, 0, 'Total', bold)
    worksheet.write(row, 1, '=SUM(B2:B5)', money)

    workbook.close()


def test_1():
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    worksheet1 = workbook.add_worksheet(u'中文 ')        # Defaults to Sheet1.
    worksheet2 = workbook.add_worksheet('Data')  # Data.
    worksheet3 = workbook.add_worksheet(u'en中文')        # Defaults to Sheet3.

    # Some data we want to write to the worksheet.
    expenses = (
        [u'中文', 1000],
        ['Gas', 100],
        ['Food', 300],
        ['Gym', 50],
    )

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    # Iterate over the data and write it out row by row.
    for item, cost in (expenses):
        worksheet1.write(row, col, item)
        worksheet1.write(row, col + 1, cost)
        row += 1

    workbook.define_name('Exchange_rate', '=0.96')
    worksheet1.write('B3', '=B2*Exchange_rate')
    # Write a total using a formula.
    worksheet1.write(row, 0, 'Total')
    worksheet1.write(row, 1, '=SUM(B1:B4)')

    workbook.close()


def simple():
    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Hello world')
    workbook.close()


def main():
    #test_1()
    #test_2()
    #test_3()
    #sparklines1()
    sparklines2()


if __name__ == '__main__':
    main()
