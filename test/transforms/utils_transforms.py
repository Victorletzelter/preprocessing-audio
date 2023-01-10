import pytest
import numpy as np


from praudio.io.signal import Signal


@pytest.fixture
def sample_signal():
    array = np.random.rand(6000)
    return Signal("dummy", 22050, array, "dummy/file/wav")


@pytest.fixture
def sample_2d_signal():
    array = np.random.rand(64, 200)
    return Signal("dummy", 22050, array, "dummy/file/wav")
