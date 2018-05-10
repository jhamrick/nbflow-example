import os
import glob
from nbflow.scons import setup

env = Environment(ENV=os.environ)
setup(env, ["analyses"], ARGUMENTS)

results = ["results/model_v_human.tex"]
figures = ["figures/human_averages.pdf", "figures/model_v_human.pdf"]
env.PDF("paper/paper.pdf", "paper/paper.tex")
env.Depends("paper/paper.pdf", results + figures)
