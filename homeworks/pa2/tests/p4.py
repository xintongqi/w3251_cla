from otter.test_files import test_case

OK_FORMAT = False

name = "p4"
points = 25

@test_case(points=None, hidden=False)
def test_find_lowest_deg_poly_1(np, find_lowest_deg_poly):
    # 2x^2 + x - 1    
    X = np.array([1, 2, 3])
    Y = 2 * np.power(X, 2) + X - 1
    a_true = np.array([-1, 1, 2])
    
    d, a = find_lowest_deg_poly(X, Y)
    assert(np.array_equal(a, a_true))
    assert(d == 2)
        
@test_case(points=None, hidden=False)
def test_find_lowest_deg_poly_2(np, find_lowest_deg_poly):
    # x^3 + 5x - 2
    X = np.array([1, 2, 3, 4, 5])
    Y = np.power(X, 3) + 5 * X - 2
    a_true = np.array([-2, 5, 0, 1])
    
    d, a = find_lowest_deg_poly(X, Y)
    assert(np.array_equal(a, a_true))
    assert(d == 3)
        
@test_case(points=None, hidden=False)
def test_find_lowest_deg_poly_3(np, find_lowest_deg_poly):
    # 2x^4 + 2x^2 - 10  
    X = np.array([-2, -1, 0, 1, 2])
    Y = 2 * np.power(X, 4) + 2 * np.power(X, 2) - 10
    a_true = np.array([-10, 0, 2, 0, 2])
    
    d, a = find_lowest_deg_poly(X, Y)
    assert(np.array_equal(a, a_true))
    assert(d == 4)
        
