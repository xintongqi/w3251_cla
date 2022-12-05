from otter.test_files import test_case

OK_FORMAT = False

name = "p2"
points = 10

@test_case(points=None, hidden=False)
def test_F2_1(np, F2):
    p = np.array([2, 4, 2])
    q = np.array([1, 2, 1])
    assert np.allclose(F2(p), q)
    
@test_case(points=None, hidden=False)
def test_F2_2(np, F2):
    p = np.array([3, 5, 1])
    q = np.array([3, 5, 1])
    assert np.allclose(F2(p), q)
    
@test_case(points=None, hidden=False)
def test_F2_3(np, F2):
    p = np.array([5, 15, 10])
    q = np.array([0.5, 1.5, 1])
    assert np.allclose(F2(p), q)
    
