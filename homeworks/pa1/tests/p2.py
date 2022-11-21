from otter.test_files import test_case

OK_FORMAT = False

name = "p2"
points = 25

@test_case(points=None, hidden=False)
def test_lengthen1(np, lengthen):
    assert np.allclose(lengthen(np.array([1, 2, 3, 4])), np.array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4.]))
    
@test_case(points=None, hidden=False)
def test_lengthen2(np, lengthen):
    assert np.allclose(lengthen(np.array([1, 2])), np.array([1., 1.5, 2.]))
    
@test_case(points=None, hidden=False)
def test_lengthen3(np, lengthen):
    assert np.allclose(lengthen(np.array([-1, 1])), np.array([-1.,  0.,  1.]))
    
