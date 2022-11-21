from otter.test_files import test_case

OK_FORMAT = False

name = "p3"
points = 25

@test_case(points=None, hidden=False)
def test_reverse1(np, reverse):
    assert np.array_equal(reverse(np.array([1])), np.array([1]))
    assert np.array_equal(reverse(np.array([2])), np.array([2]))
    assert np.array_equal(reverse(np.array([3])), np.array([3]))
    
@test_case(points=None, hidden=False)
def test_reverse2(np, reverse):    
    assert np.array_equal(reverse(np.array([1, 2, 3])), np.array([3, 2, 1]))
    assert np.array_equal(reverse(np.array([0, 1, 0])), np.array([0, 1, 0]))
    assert np.array_equal(reverse(np.array([1, 0, 0])), np.array([0, 0, 1]))
    
@test_case(points=None, hidden=False)
def test_reverse3(np, reverse):    
    assert np.array_equal(reverse(np.array([1, 1, 1])), np.array([1, 1, 1]))
    assert np.array_equal(reverse(np.array([0, 1, 0, 1, 0])), np.array([0, 1, 0, 1, 0]))
    assert np.array_equal(reverse(np.array([-1, 3.14, 8.5])), np.array([8.5, 3.14, -1]))
    
