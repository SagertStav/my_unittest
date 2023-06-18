from utils import arrs
def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2 #не 3
    assert arrs.get([], 0, "test") == "test" #был пустой список
    assert arrs.get([], -3, "test") == "test"
    assert arrs.get([2,10], 5, "test") == "test"
    assert arrs.get([2, 500], 1, "test") == 500
    assert arrs.get([2,10], 5) is None
    assert arrs.get([], 0) is None
    assert arrs.get([], -3) is None
    assert arrs.get([], 5, None) is None
    assert arrs.get([1, 2, 3], -1, "-") == "-"
def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([10, 18, 353,0], 1,-1) == [18, 353]
    assert arrs.my_slice([10, 18, 353, 0], -5, 0) == [10, 18,353,0]
    assert arrs.my_slice([10, 18, 353, 0], 0, -3) == [10]
    assert arrs.my_slice([60, 50, 20, 0]) == [60,50,20,0]
    assert arrs.my_slice([],1,10) == []

test_get()
test_slice()