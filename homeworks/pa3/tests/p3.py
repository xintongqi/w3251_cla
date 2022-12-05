from otter.test_files import test_case

OK_FORMAT = False

name = "p3"
points = 16

@test_case(points=None, hidden=False)
def test_F1_1(np, F1):
    basis = np.array([[1/100, 0, 0],
                      [0, 1/100, 0],
                      [0, 0, 1]])
    points = np.array([[1],
                       [2],
                       [3]])
    points_basis = np.array([[100],
                             [200],
                             [3]])
    
    assert np.allclose(F1(points, basis), points_basis)
    
@test_case(points=None, hidden=False)
def test_F1_2(np, F1):
    basis = np.array([[1/100, 0, 0],
                      [0, 1/100, 0],
                      [0, 0, 1]])
    points = np.array([[1, 0],
                       [0, 2],
                       [3, 2]])
    points_basis = np.array([[100, 0],
                             [0, 200],
                             [3, 2]])
    
    assert np.allclose(F1(points, basis), points_basis)
    
@test_case(points=None, hidden=False)
def test_F1_3(np, F1):
    basis = np.array([[-1, 0, 0],
                      [0, -2, 0],
                      [0, 0, 1]])
    points = np.array([[1],
                       [2],
                       [3]])
    points_basis = np.array([[-1],
                             [-1],
                             [3]])
    
    assert np.allclose(F1(points, basis), points_basis)
    
@test_case(points=None, hidden=False)
def test_F1_4(np, F1):
    basis = np.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]])
    points = np.array([[1],
                       [2],
                       [3]])
    points_basis = np.array([[1],
                             [2],
                             [3]])
    
    assert np.allclose(F1(points, basis), points_basis)
    
