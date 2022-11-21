from otter.test_files import test_case

OK_FORMAT = False

name = "p1"
points = 25

@test_case(points=None, hidden=False)
def test_downsample1(np, downsample):
    assert np.array_equal(downsample(np.array([1, 2])), np.array([2]))
    assert np.array_equal(downsample(np.array([2, 4])), np.array([4]))
    assert np.array_equal(downsample(np.array([0, 1])), np.array([1]))
    
@test_case(points=None, hidden=False)
def test_downsample2(np, downsample):
    assert np.array_equal(downsample(np.array([1, 2, 3, 4])), np.array([2, 4]))
    assert np.array_equal(downsample(np.array([2, 4, 6, 8])), np.array([4, 8]))
    assert np.array_equal(downsample(np.array([0, 1, 0, 1])), np.array([1, 1]))
    
@test_case(points=None, hidden=False)
def test_downsample3(np, downsample):
    assert np.array_equal(downsample(np.array([0, 1, 0, 1, 0, 1, 0, 1])), np.array([1, 1, 1, 1]))
    
