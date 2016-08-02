#!/usr/bin/env python
# coding: utf-8

import tablib


def test_tablib():
    headers = ('first_name', 'last_name')
    data = [('John', 'Adams'), ('George', 'Washington')]
    data = tablib.Dataset(*data, headers=headers)
    print data.json
    print data.yaml
    file_path = './1.xlsx'
    with open(file_path, 'wb') as f:
                f.write(data.xlsx)

def test_tablib2():
    daniel_tests = [('11/24/09', 'Math 101 Mid-term Exam', 56.), ('05/24/10', 'Math 101 Final Exam', 62.)]
    suzie_tests = [('11/24/09', 'Math 101 Mid-term Exam', 56.), ('05/24/10', 'Math 101 Final Exam', 62.)]

    # Create new dataset
    tests = tablib.Dataset()
    tests.headers = ['Date', 'Test Name', 'Grade']

    # Daniel's Tests
    tests.append_separator('Daniel\'s Scores')

    for test_row in daniel_tests:
        tests.append(test_row)

    # Susie's Tests
    tests.append_separator('Susie\'s Scores')

    for test_row in suzie_tests:
        tests.append(test_row)

    # Write spreadsheet to disk
    with open('grades.xls', 'wb') as f:
        f.write(tests.xls)


def main():
    test_tablib()
    test_tablib2()


if __name__ == "__main__":
    main()
