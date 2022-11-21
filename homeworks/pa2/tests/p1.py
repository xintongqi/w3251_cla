from otter.test_files import test_case

OK_FORMAT = False

name = "p1"
points = 30

@test_case(points=None, hidden=False)
def test_find_quality_scores_1(np, find_quality_scores):
    N = 3
    L = [((0,1), 2), ((1,2), 4), ((2,0), 6)]
    consistent, qualities = find_quality_scores(N, L)
    assert(consistent == False)
    
@test_case(points=None, hidden=False)
def test_find_quality_scores_2(np, find_quality_scores):
    N = 3
    L = [((0,1), 2.0), ((1,2), 4.0), ((2,0), -6.0)]
    A = np.array([[-1, 1, 0],
                  [0, -1, 1],
                  [1, 0, -1]])
    b = np.array([2, 4, -6])
    consistent, qualities = find_quality_scores(N, L)
    assert(consistent == True)
    assert(np.allclose(A @ qualities, b))
    
@test_case(points=None, hidden=False)
def test_find_quality_scores_3(np, find_quality_scores):
    N = 5
    L = [((0,1), 1.0), ((1,2), 1.0), ((2,0), -2.0), ((3, 4), 3.0)]
    A = np.array([[-1, 1, 0, 0, 0],
                  [0, -1, 1, 0, 0],
                  [1, 0, -1, 0, 0],
                  [0, 0, 0, -1, 1]])
    b = np.array([1, 1, -2, 3])
    consistent, qualities = find_quality_scores(N, L)
    assert(consistent == True)
    assert(np.allclose(A@qualities, b))
    
