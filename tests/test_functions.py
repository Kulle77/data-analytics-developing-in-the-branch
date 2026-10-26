import unittest
import pickle
from pathlib import Path


class TestGitIgnore(unittest.TestCase):
    def setUp(self):
        self.gitignore = Path(__file__).parent.parent / ".gitignore"

    def test_gitignore_exists(self):
        assert self.gitignore.exists(), (
            "❌ .gitignore not found in the challenge directory. "
            "Did you accidentally delete it? Create one with `touch .gitignore` and add `*.sqlite` and `data/`."
        )

    def test_gitignore_covers_sqlite(self):
        content = self.gitignore.read_text()
        assert "*.sqlite" in content, (
            "❌ .gitignore does not contain `*.sqlite`. "
            "Did you add it? Open .gitignore in VS Code and add a line with `*.sqlite`."
        )

    def test_gitignore_covers_data_folder(self):
        content = self.gitignore.read_text()
        assert "data/" in content, (
            "❌ .gitignore does not contain `data/`. "
            "Did you add it? Open .gitignore in VS Code and add a line with `data/`."
        )


class TestFunctions(unittest.TestCase):
    def test_daily_turnover(self):
        with open('tests/daily_turnover.pkl', 'rb') as f:
            result, query = pickle.load(f)
        if "desc" in query:
            expected = [('2021-08-31', 66640.0), ('2021-08-30', 78497.0), ('2021-08-29', 77845.0), ('2021-08-28', 41405.0), ('2021-08-27', 50601.0)]
            self.assertEqual(result, expected, f'Daily turnover mismatch. First output is {result[0]}. Expected is {expected[0]}.')
        elif "round" in query:
            expected = [('2021-03-01', 113698), ('2021-03-02', 98370), ('2021-03-03', 83869), ('2021-03-04', 91452), ('2021-03-05', 81196)]
            self.assertEqual(result, expected, f'Daily turnover mismatch. First output is {result[0]}. Expected is {expected[0]}.')
        else:
            expected = [('2021-03-01', 113697.94), ('2021-03-02', 98369.79), ('2021-03-03', 83869.03), ('2021-03-04', 91451.79), ('2021-03-05', 81196.18)]
            self.assertEqual(result, expected, f'Daily turnover mismatch. First output is {result[0]}. Expected is {expected[0]}.')

    def test_purchase_cost(self):
        with open('tests/purchase_cost.pkl', 'rb') as f:
            result, query = pickle.load(f)
        if "desc" in query:
            expected = [('2021-08-31', 66640.0, 45791.0), ('2021-08-30', 78497.0, 54633.0), ('2021-08-29', 77845.0, 52790.0), ('2021-08-28', 41405.0, 27847.0), ('2021-08-27', 50601.0, 33978.0)]
            self.assertEqual(result, expected, f'Purchase cost mismatch. First output is {result[0]}. Expected is {expected[0]}.')
        elif "round" in query:
            expected = [('2021-03-01', 113698, 77046), ('2021-03-02', 98370, 65695), ('2021-03-03', 83869, 55733), ('2021-03-04', 91452, 61487), ('2021-03-05', 81196, 54650)]
            self.assertEqual(result, expected, f'Purchase cost mismatch. First output is {result[0]}. Expected is {expected[0]}.')
        else:
            expected = [('2021-03-01', 113697.94, 77045.57), ('2021-03-02', 98369.79, 65695.05), ('2021-03-03', 83869.03, 55733.16), ('2021-03-04', 91451.79, 61487.12), ('2021-03-05', 81196.18, 54650.29)]
            self.assertEqual(result, expected, f'Purchase cost mismatch. First output is {result[0]}. Expected is {expected[0]}.')

    def test_rounding(self):
        with open('tests/rounding.pkl', 'rb') as f:
            result, query = pickle.load(f)
        if "desc" in query:
            expected = [('2021-08-31', 66640.0, 45791.0), ('2021-08-30', 78497.0, 54633.0), ('2021-08-29', 77845.0, 52790.0), ('2021-08-28', 41405.0, 27847.0), ('2021-08-27', 50601.0, 33978.0)]
            self.assertEqual(result, expected, f'Rounding mismatch. First output is {result[0]}. Expected is {expected[0]}.')
        else:
            expected = [('2021-03-01', 113698, 77046), ('2021-03-02', 98370, 65695), ('2021-03-03', 83869, 55733), ('2021-03-04', 91452, 61487), ('2021-03-05', 81196, 54650)]
            self.assertEqual(result, expected, f'Rounding mismatch. First output is {result[0]}. Expected is {expected[0]}.')

    def test_date_sort(self):
        with open('tests/date_sort.pkl', 'rb') as f:
            result = pickle.load(f)
        expected = [('2021-08-31', 66640.0, 45791.0), ('2021-08-30', 78497.0, 54633.0), ('2021-08-29', 77845.0, 52790.0), ('2021-08-28', 41405.0, 27847.0), ('2021-08-27', 50601.0, 33978.0)]
        self.assertEqual(result, expected, f'Date sorting mismatch. First output is {result[0]}. Expected is {expected[0]}.')
