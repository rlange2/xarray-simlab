import numpy as np

from xsimlab.stores import InMemoryOutputStore


def test_in_memory_output_store():
    out_store = InMemoryOutputStore()
    key = ('some_process', 'some_var')

    arr = np.array([1, 2, 3])
    out_store.append(key, arr)
    arr[:] = [4, 5, 6]
    out_store.append(key, arr)

    expected = np.array([[1, 2, 3],
                         [4, 5, 6]])

    assert np.all(out_store[key] == expected)