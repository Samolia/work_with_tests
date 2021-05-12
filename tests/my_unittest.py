import unittest
from application.services import add_new_shelf, add_new_doc, move_doc, del_doc, return_name, return_number_shelf


class TestServices(unittest.TestCase):

    def test_add_new_shelf_successfully_1(self):
        print('test_add_new_shelf_successfully_1')
        expected_res = 'Полка успешно добавлена!'
        actual_res = add_new_shelf(4)
        self.assertEqual(expected_res, actual_res)

    def test_failed_to_add_new_shelf_2(self):
        print('test_failed_to_add_new_shelf_2')
        expected_res = 'Полка уже существует!'
        actual_res = add_new_shelf(1)
        self.assertEqual(expected_res, actual_res)

    def test_add_new_doc_successfully_3(self):
        print('test_add_new_doc_successfully_3')
        expected_res = 'Документ с номером успешно добавлен на полку!'
        actual_res = add_new_doc(3)
        self.assertEqual(expected_res, actual_res)

    def test_failed_to_add_new_doc_4(self):
        print('test_failed_to_add_new_doc_4')
        expected_res = 'Такой полки не существует!'
        actual_res = add_new_doc(5)
        self.assertEqual(expected_res, actual_res)

    def test_move_doc_successfully_5(self):
        print('test_move_doc_successfully_5')
        expected_res = 'Документ успешно перемещен!'
        actual_res = move_doc()
        self.assertEqual(expected_res, actual_res)

    def test_move_doc_false_doc_number_6(self):
        print('test_move_doc_false_doc_number_6')
        expected_res = 'Такой полки не существует!'
        actual_res = move_doc(shelf_number=6)
        self.assertEqual(expected_res, actual_res)

    def test_move_doc_false_shelf_number_7(self):
        print('test_move_doc_false_shelf_number_7')
        expected_res = 'Документа с таким номером в базе нет!'
        actual_res = move_doc(doc_number='15321')
        self.assertEqual(expected_res, actual_res)

    def test_del_doc_successfully_8(self):
        print('test_del_doc_successfully_8')
        expected_res = 'Документ успешно удален!'
        actual_res = del_doc()
        self.assertEqual(expected_res, actual_res)

    def test_failed_to_del_doc_9(self):
        print('test_failed_to_del_doc_9')
        expected_res = 'Документа с таким номером в базе нет!'
        actual_res = del_doc(doc_number='23456')
        self.assertEqual(expected_res, actual_res)

    def test_return_name_successfully_10(self):
        print('test_return_name_successfully_11')
        expected_res = 'Документа с таким номером в базе нет!'
        actual_res = return_name(doc_number='24523')
        self.assertEqual(expected_res, actual_res)

    def test_failed_to_return_name_11(self):
        print('test_failed_to_return_name_10')
        expected_res = 'Владелец документа с таким номером найден!'
        actual_res = return_name()
        self.assertEqual(expected_res, actual_res)

    def test_return_number_shelf_successfully_12(self):
        print('test_return_number_shelf_successfully_12')
        expected_res = 'Документ с таким номером хранится на полке №'
        actual_res = return_number_shelf()
        self.assertEqual(expected_res, actual_res)

    def test_failed_to_return_number_shelf_13(self):
        print('test_failed_to_return_number_shelf_13')
        expected_res = 'Документа с таким номером в базе нет!'
        actual_res = return_number_shelf(doc_number='74356')
        self.assertEqual(expected_res, actual_res)
