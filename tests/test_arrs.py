from utils import arrs
def test_get_from_empty_list():
    try:
        assert arrs.get([], 0, "test") == "test"  # был пустой список
        assert arrs.get([], 1) is none
    except IndexError:
        print("К пустому списку нельзя обратиться по индексу")

def test_get_when_out_of_range():
    try:
        assert arrs.get([2, 10], 5, "test") == "test"
        assert arrs.get([2,10], 5) is None
    #        assert arrs.get([], 0) is None
    #        assert arrs.get([], 5, None) is None
    except IndexError:
        print("Выход индекса за пределы массива не отработан")


def test_get_negative_index():
    try:
      assert arrs.get([5], -3, "test") == "test"
      assert arrs.get([1, 100, -1000], -1) is None
    except:
      print("Работа в get c отрицательными индексами не реализована!")

def test_get_negative_index_from_empty():
    try:
      assert arrs.get([], -1) is None
    except:
      print("Get из пустого списка c отрицательным индексом должен возвращать None (не возвращает!)")

def test_get():
    # with self.assertRaises(ZeroDivisionError):
    #    calc.divide(10, 0)
    assert arrs.get([1, 2, 3], 1, "test") == 2 #не 3

    assert arrs.get([2, 500], 1, "test") == 500
    assert arrs.get([], -3) is None

    assert arrs.get([1, 2, 3], -1, "-") == "-"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([10, 18, 353,0], 1,-1) == [18, 353]
    #assert arrs.my_slice([10, 18, 353, 0], -5, 0) == [10, 18,353,0] #test показал=[], ниже исправил его

    #По условию первого отрицательного индекса две ветви: c выходом за начало списка справа налево:...
    assert arrs.my_slice([10, 18, 353, 0], -5, 0) == []
    #... и без него:
    assert arrs.my_slice([10, 18, 353, 0], -1, 0) == []

    assert arrs.my_slice([10, 18, 353, 0], 0, -3) == [10]
    assert arrs.my_slice([60, 50, 20, 0]) == [60,50,20,0]
    assert arrs.my_slice([],1,10) == []

test_get_from_empty_list()
test_get_when_out_of_range()
test_get_negative_index()
test_get_negative_index_from_empty()
test_get()

test_slice()