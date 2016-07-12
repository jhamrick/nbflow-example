import os
import glob
from nbflow.scons import setup

env = Environment(ENV=os.environ)
setup(env, ["analyses"])

env.PDF("paper/paper.pdf", "paper/paper.tex")
env.Depends(
    "paper/paper.pdf", 
    sorted(glob.glob("results/*.tex")))