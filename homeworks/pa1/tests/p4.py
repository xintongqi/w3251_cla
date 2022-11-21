from otter.test_files import test_case

OK_FORMAT = False

name = "p4"
points = 25

@test_case(points=None, hidden=False)
def test_super_creep1(np, super_creep):
    assert np.allclose(super_creep(np.array([1, 2, 3])), np.array([3, 2.5, 2, 1.5, 1]))
    
@test_case(points=None, hidden=False)
def test_super_creep2(np, super_creep):
    assert np.allclose(super_creep(np.array([3, 2, 1])), np.array([1, 1.5, 2, 2.5, 3]))
    
@test_case(points=None, hidden=False)
def test_super_creep3(np, super_creep):
    assert np.allclose(super_creep(np.array([0])), np.array([0]))
    
