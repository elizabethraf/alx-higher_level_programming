import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8



class TestStringMethods(unittest.TestCase):
    """Test a Base"""

    @classmethod
    def setup(self):
        Base._Base__nb_objects = 0
        self.assertEqqual(Base._Base__nb_objects, 0)

    def teardownClass(self):
        """Tear Objects"""
        pass

    def test_pep8(self):
        pep8_style = pep8.StyleGuide(quit=True)
        pep_check = pep8_style.check_files(['models/base.py'])
        self.assertEqual(pep_check.total_errors, 0, 'Pep8 Error in file')

    def test_no_id(self):
         """Test id as NONE"""
         b = Base()
         self.assertEqual(b.id, 1)

    def test_upper(self):
        self.assertEqual('Base._Base__nb_objects, 0')
        pass

    def test_is_private(self):
        """nb_object private"""
        print('__nbv_object is private')
        self.assertTrue(hasattr(Base, '_Base__nb_objects'), 0)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """Params"""

        base_instance_1 = Base(12)
        base_instance_2 = Base()
        base_instance_3 = Base()
        base_instance_4 = Base()
        self.assertEqual(base_instance_1.id, 12)
        self.assertEqual(base_instance_2.id, 1)
        self.assertEqual(base_instance_3.id, 2)
        self.assertEqual(base_instance_4.id, 3)


    def test_to_json_string(self):
        """Testing to_json_string()"""

        o1_1 = [{"hi": 1, "yo": "hol"}]
        o1_2 = [{"hello": 3}]
        o1_3 = None
        o1_4 = "a string"
        o1_5 = 123
        o1_6 = [[1, 2, 3]]
        o1_7 = []

        dict1 = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        dict2 = {'id': 89, 'x': 0, 'size': 4, 'y': 3}
        json_string = Base.to_json_string([dict1, dict2])
        jload = json.loads(json_string)
        self.assertEqual(jload, [dict1, dict2])
        self.assertTrue(isinstance(json_string, str))

    def test_from_json_to_str(self):
        json_test = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        json_str = Base.from_json_string(json_test)
        self.assertTrue(isinstance(json_str, list))


if __name__ == '__main__':
    unittest.main()
