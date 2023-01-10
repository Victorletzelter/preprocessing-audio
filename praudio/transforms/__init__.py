"""
Importing transforms at transform dir level for ease of import in other
modules.
"""

import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/victorletzelter/Documents/GitHub/praudio/')

from praudio.transforms.log import Log
from praudio.transforms.magnitudespectrogram import MagnitudeSpectrogram
from praudio.transforms.melspectrogram import MelSpectrogram
from praudio.transforms.mfcc import MFCC
from praudio.transforms.powerspectrogram import PowerSpectrogram
from praudio.transforms.stft import STFT
from praudio.transforms.scaling.minmaxscaler import MinMaxScaler
from praudio.transforms.scaling.rowstandardiser import RowStandardiser
from praudio.transforms.scaling.standardiser import Standardiser
