import sys
print(sys.executable)

from bqskit import Circuit
from bqskit import compile 
from bqskit.passes import *
from bqskit.compiler.basepass import BasePass
from bqskit.compiler import BasePass
from bqskit.compiler.passdata import PassData


class MyFirstPass(BasePass):
    def __init__(self):
        super().__init__()

    def run(self, circuit: Circuit, data: PassData) -> None:
        count = circuit.count(CNOTGate)
        print(f"Number of CXGates: {count}")