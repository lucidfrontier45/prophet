import os.path
import shutil

import cmdstanpy

model_dir = "python/stan/unix"
model_name = "prophet.stan"
target_name = "prophet_model.bin"
sm = cmdstanpy.CmdStanModel(
    model_name=model_name,
    stan_file=os.path.join(model_dir, model_name),
    stanc_options={"O1": True},
    cpp_options={"O3": True},
)
cmdstan_path = cmdstanpy.cmdstan_path()
tbb_path = os.path.join(cmdstan_path, "stan/lib/stan_math/lib/tbb/libtbb.so.2")

shutil.copy(os.path.join(model_dir, "prophet"), target_name)
shutil.copy(tbb_path, "libtbb.so.2")
