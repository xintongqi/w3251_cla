from otter.test_files import test_case

OK_FORMAT = False

name = "p4"
points = 10

@test_case(points=None, hidden=False)
def test_T1_1(np, T1):
    p = np.array([0, 2])
    q = np.array([0, 2, 1])
    assert np.allclose(T1(p), q)
    
@test_case(points=None, hidden=False)
def test_T1_2(np, T1):
    p = np.array([1, 1])
    q = np.array([1, 1, 1])
    assert np.allclose(T1(p), q)
    
@test_case(points=None, hidden=False)
def test_T1_3(np, T1):
    p = np.array([5, 10])
    q = np.array([5, 10, 1])
    assert np.allclose(T1(p), q)
    
