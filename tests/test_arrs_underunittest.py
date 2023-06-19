import unittest
# Импорт модуля, содержащего функции для тестирования
from utils import arrs

# Название класса TestCalc — произвольное
class TestCalc(unittest.TestCase):

    # Внутри пишем нужное количество методов (функций)
    def test_get(self):
        # Пишем нужное количество проверок
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)  # не 3
        #self.assertEqual(arrs.get([], 0, "ПРОБА"), "ПРОБА")  # был пустой список
        try:
          self.assertEqual(arrs.get([], 0, []), [])  # был пустой список
        except IndexError:
          print("К пустому списку нельзя обратиться по индексу")

        try:
          self.assertEqual(arrs.get([2, 10], 5, "test"), "test")
          #self.assertIsNone(arrs.get([2, 10], 5))
          #self.assertIsNone(arrs.get([], 0))  #обрабатывается по умолчательному значению как отсутствие индекса
          #self.assertIsNone(arrs.get([], 5, None),None)

        #with self.assertRaises(IndexError):
        except IndexError:
            print("Выход индекса за пределы массива не отработан")

        self.assertEqual(arrs.get([], -3, "test"), "test")
        self.assertEqual(arrs.get([2, 500], 1, "test"), 500)
        self.assertIsNone(arrs.get([], -3))
        self.assertEqual(arrs.get([1, 2, 3], -1, "-"), "-")

        #with self.assertRaises(ZeroDivisionError):
        #    calc.divide(10, 0)

    def test_my_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        #self.assertEqual(arrs.my_slice([10, 18, 353, 0], 1, -1), [18, 353]) #2-й минусовый индекс не обрабатывается
        #self.assertEqual(arrs.my_slice([10, 18, 353, 0], 1, -1), []) #поэтому возвращается []
        #self.assertEqual(arrs.my_slice([10, 18, 353, 0], -5, 0), [10, 18, 353, 0]) #можно было бы и усеченный хвост возвращать при индексе много<0 за пределами 0-го
        self.assertEqual(arrs.my_slice([10, 18, 353, 0], -5, 0), []) #можно было бы и усеченный хвост возвращать при индексе много<0 за пределами 0-го
        # По условию первого отрицательного индекса две ветви: c выходом за начало списка справа налево (см выше -5),
        # ... и без него:
        self.assertEqual(arrs.my_slice([10, 18, 353, 0], -1, 0), [])

        self.assertEqual(arrs.my_slice([10, 18, 353, 0], 0, -3), [10])
        self.assertEqual(arrs.my_slice([60, 50, 20, 0]), [60, 50, 20, 0])
        self.assertEqual(arrs.my_slice([], 1, 10), [])

#if __name__ == '__main__':
#    unittest.main()

#print(arrs.get([1, 2, 3], 1, "проба"))