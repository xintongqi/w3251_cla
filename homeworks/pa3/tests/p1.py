from otter.test_files import test_case

OK_FORMAT = False

name = "p1"
points = 24

@test_case(points=None, hidden=False)
def test_F3_1(np, F3):
    q = np.array([0, 1, 1])
    assert np.array_equal(F3(q), np.array([0, 1]))
    
@test_case(points=None, hidden=False)
def test_F3_2(np, F3):
    q = np.array([1, 2, 3])
    assert np.array_equal(F3(q), np.array([1, 2]))
    
@test_case(points=None, hidden=False)
def test_F3_mat_1(np, F3, F3_mat):
    A = np.array([[1/100, 0, 0],
                  [0, 1/100, 0],
                  [0, 0, 1]])
    C = np.array([[1/100, 0],
                  [0, 1/100]])
    M = np.array([[1, 0, 0],
                  [0, 1, 0]])
    assert np.allclose(F3_mat(A, C), M)

@test_case(points=None, hidden=False)
def test_F3_mat_2(np, F3, F3_mat):
    A = np.array([[1, 1, 1],
                  [0, 1, 1],
                  [0, 0, 1]])
    C = np.array([[2, 2],
                  [0, 2]])
    M = np.array([[0.5, 0, 0],
                  [0, 0.5, 0.5]])
    assert np.allclose(F3_mat(A, C), M)

