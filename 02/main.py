import part_1
import part_2
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from runner import runner

input_dir = os.path.dirname(os.path.abspath(__file__))

runner("1", part_1.solve, input_dir)
runner("2", part_2.solve, input_dir)
