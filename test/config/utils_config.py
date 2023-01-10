import pytest


@pytest.fixture
def configs():
    configs = {
        "dataset_dir": "path/to/dataset/",
        "save_dir": "/dir/where/to/store/preprocessed/dataset/",
        "file_preprocessor": {
            "loader": {
                "sample_rate": 44100,
                "mono": True
            },
            "transforms_chain": {
                "magnitudespectrogram": {
                    "frame_length": 1024,
                    "hop_length": 512,
                    "win_length": 1024,
                    "window": "hann"
                },
                "log": {},
                "minmaxscaler": {
                    "min": -2,
                    "max": 2
                }
            }
        }
    }
    return configs