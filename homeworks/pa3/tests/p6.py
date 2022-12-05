from otter.test_files import test_case

OK_FORMAT = False

name = "p6"
points = 20

@test_case(points=None, hidden=False)
def test_change_of_basis_T2_1(np, change_of_basis_T2, make_equations, w):
    topleft = (np.array([10, 10, 1]), np.array([0, 0, 1]))
    botleft = (np.array([50, 30, 1]), np.array([0, 1, 1]))
    topright = (np.array([40, 20, 1]), np.array([1, 0, 1]))
    botright = (np.array([20, 30, 1]), np.array([1, 1, 1]))
    C = np.array([[1, -2, 10],
                  [0.6, -1.8, 12],
                  [0.6, -2.8, 42]])
    C_out = change_of_basis_T2(topleft, botleft, topright, botright)
    assert np.allclose(C, C_out)
    
@test_case(points=None, hidden=False)
def test_change_of_basis_T2_2(np, change_of_basis_T2, make_equations, w):
    topleft = (np.array([1, 1, 1]), np.array([0, 0, 1]))
    botleft = (np.array([1, 2, 3]), np.array([0, 1, 1]))
    topright = (np.array([0, 2, 1]), np.array([1, 0, 1]))
    botright = (np.array([0, 0, 4]), np.array([1, 1, 1]))
    C = np.array([[1, 0, -1],
                  [0.5, 0.5, -1],
                  [1.5, 0, -1]])
    C_out = change_of_basis_T2(topleft, botleft, topright, botright)
    assert np.allclose(C, C_out)
    
