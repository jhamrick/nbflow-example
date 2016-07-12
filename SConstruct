import os
import glob
from nbflow.scons import setup

env = Environment(ENV=os.environ)
setup(env, ["analyses"])

results = sorted(glob.glob("results/*.tex"))
figures = sorted(glob.glob("figures/*.pdf"))
env.PDF("paper/paper.pdf", "paper/paper.tex")
env.Depends("paper/paper.pdf", results + figures)
