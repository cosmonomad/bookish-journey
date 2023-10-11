#!/usr/bin/env python
def dont_test_get_radec():
    try:
        from mymodule import sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return



def test_get_radec():
    from mymodule import sky_sim 
    expected = (14.215420962967535, 41.26916666666667)
    answer = sky.sim.get_radec()
    if not ((expected[0] == answer[0]) & expected[1] == answer[1])
        raise AssertionError(f"get_radecf gives {answer} instead of {expected}")
    return
