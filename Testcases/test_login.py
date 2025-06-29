import pytest
from utils import excel
import os



class TestLogin():
    @pytest.mark.usefixtures("setup")
    def test_go_to_vnexpress(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        file_path = os.path.join(parent_dir, "testdata", "testdata.xlsx")
        excel_instance = excel.Excel(file_path, "url")
        url = excel_instance.read_excel()[0][0]
        self.driver.get(url)
        print("test")
        assert True, "This is a placeholder test to ensure pytest runs correctly."

    def test_list(self):
        list_data = []
        
