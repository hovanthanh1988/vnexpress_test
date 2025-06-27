import openpyxl

class Excel:
    def __init__(self, file_path, sheet_name=None):
        """
        Initializes the Excel class with a file path.

        :param file_path: Path to the Excel file.
        """
        global workbook
        global sheet
        if None not in (file_path, sheet_name):
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook[sheet_name]

    def read_excel(self):

        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(list(row))

        return data