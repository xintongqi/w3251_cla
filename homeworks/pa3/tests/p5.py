from otter.test_files import test_case

OK_FORMAT = False

name = "p5"
points = 20

@test_case(points=None, hidden=False)
def test_make_equations_1(np, make_equations):
    p_A = np.array([2, 4, 6])
    p_W = np.array([1, 0, 1])
    u = np.array([2, 4, 1, 0, 0, 0, -2, -4, -1])
    v = np.array([0, 0, 0, 2, 4, 1, 0, 0, 0])
    u_out, v_out = make_equations(p_A, p_W)
    assert np.allclose(u, u_out)
    assert np.allclose(v, v_out)
    
@test_case(points=None, hidden=False)
def test_make_equations_2(np, make_equations):
    p_A = np.array([100, 50, 25])
    p_W = np.array([1, 1, 1])
    u = np.array([100, 50, 1, 0, 0, 0, -100, -50, -1])
    v = np.array([0, 0, 0, 100, 50, 1, -100, -50, -1])
    u_out, v_out = make_equations(p_A, p_W)
    assert np.allclose(u, u_out)
    assert np.allclose(v, v_out)
    
