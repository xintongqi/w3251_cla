from otter.test_files import test_case

OK_FORMAT = False

name = "p3"
points = 25

@test_case(points=None, hidden=False)
def test_generate_design_mat_1(np, generate_design_mat):
    X = np.array([1, 2, 3])
    d = 2
    design_mat = np.array([[1, 1, 1],
                           [1, 2, 4],
                           [1, 3, 9]])
    assert(np.array_equal(generate_design_mat(X, d), design_mat))
        
@test_case(points=None, hidden=False)
def test_generate_design_mat_2(np, generate_design_mat):
    X = np.array([0, 1, 1, 0, 2])
    d = 3
    design_mat = np.array([[1, 0, 0, 0],
                           [1, 1, 1, 1],
                           [1, 1, 1, 1],
                           [1, 0, 0, 0],
                           [1, 2, 4, 8]])
    assert(np.array_equal(generate_design_mat(X, d), design_mat))
        
@test_case(points=None, hidden=False)
def test_generate_design_mat_3(np, generate_design_mat):
    X = np.array([0.5, 1, 1.5, 2])
    d = 3
    design_mat = np.array([[1, 0.5, 0.25, 0.125],
                           [1, 1, 1, 1],
                           [1, 1.5, 2.25, 3.375],
                           [1, 2, 4, 8]])    
    assert(np.array_equal(generate_design_mat(X, d), design_mat))

