import os
from nbflow.scons import setup

env = Environment(ENV=os.environ)
setup(env, ["analyses"])

import glob
all_results = sorted(glob.glob("results/*.tex"))
env.PDF("paper/paper.pdf", "paper/paper.tex")
env.Depends("paper/paper.pdf", all_results)