import numpy as np

from microsim.samples.utils._bresenham import drawlines_bresenham


def test_bres():
    n = 100

    a: np.ndarray = np.zeros((n, n)).astype(np.int32)
    drawlines_bresenham(np.array([[0, 0, n - 1, n - 1]], dtype=np.int32), a)

    expect: np.ndarray = np.zeros((n, n)).astype(np.int32)
    for i in range(n):
        expect[i, i] = 1

    np.testing.assert_array_equal(a, expect)


def test_bres3():
    n = 100
    a: np.ndarray = np.zeros((n, n, n)).astype(np.int32)
    drawlines_bresenham(np.array([[0, 0, 0, n - 1, n - 1, n - 1]], dtype=np.int32), a)

    expect: np.ndarray = np.zeros((n, n, n)).astype(np.int32)
    for i in range(n):
        expect[i, i, i] = 1

    np.testing.assert_array_equal(a, expect)
