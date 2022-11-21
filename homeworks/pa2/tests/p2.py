from otter.test_files import test_case

OK_FORMAT = False

name = "p2"
points = 20

@test_case(points=None, hidden=False)
def test_check_quality_scores_1(np, check_quality_scores):
    N = 4
    L = [((0,1), 1.0), ((1,2), 1.0), ((2,3), 1.0), ((3,0), -3.0)]
    Q = np.array([-3, -2, -1, 0])
    assert(check_quality_scores(N, L, Q))
    assert(check_quality_scores(N, L, Q + 42 * np.ones(N)))
    assert(check_quality_scores(N, L, Q + -27 * np.ones(N)))
    assert(check_quality_scores(N, L, Q + np.array([1, 0, 0, 0])) == False)
        
@test_case(points=None, hidden=False)
def test_check_quality_scores_2(np, check_quality_scores):
    N = 6
    L = [((0,1), 2.0), ((1,2), 2.0), ((2,0), -4.0), ((3,4), 3.0), ((4,5), 3.0), ((5,3), -6.0)]
    Q = np.array([-4, -2, 0, -6, -3, 0])
    assert(check_quality_scores(N, L, Q))
    assert(check_quality_scores(N, L, Q + 42 * np.ones(N)))
    assert(check_quality_scores(N, L, Q + -27 * np.ones(N)))
    assert(check_quality_scores(N, L, Q + np.array([1, 0, 0, 0, 0, 0])) == False)
        
