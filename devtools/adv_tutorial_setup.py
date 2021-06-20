#!/usr/bin/env python

import openpathsampling as paths
from openpathsampling.engines import toy as toys

import numpy as np

pes = (
    toys.OuterWalls(sigma=[1.0, 1.0], x0=[0.0, 0.0])
    + toys.Gaussian(A=-1.0, alpha=[12.0, 5.0], x0=[-0.6, 0.0])
    + toys.Gaussian(A=-1.0, alpha=[12.0, 5.0], x0=[0.6, 0.0])
)

topology = toys.Topology(n_spatial=2, masses=[1.0, 1.0], pes=pes)
integ = toys.LangevinBAOABIntegrator(dt=0.02, temperature=0.1, gamma=2.5)
options = {
    'integ': integ,
    'n_frames_max': 5000,
    'n_steps_per_frame': 1
}

engine = toys.Engine(options, topology).named("toy_engine")

cv = paths.CoordinateFunctionCV("x", lambda snap: snap.xyz[0][0])
state_A = paths.CVDefinedVolume(cv, float("-inf"), -0.6).named("A")
state_B = paths.CVDefinedVolume(cv, 0.6, float("inf")).named("B")

snap = toys.Snapshot(velocities=np.array([[0.0, 0.0]]),
                     coordinates=np.array([[0.0, 0.0]]),
                     engine=engine)

randomizer = paths.RandomVelocities(beta=10.0, engine=engine)

committor_storage = paths.Storage("toy_committor.nc", mode='w')

committor = paths.CommittorSimulation(
    storage=committor_storage,
    engine=engine,
    states=[state_A, state_B],
    randomizer=randomizer,
    initial_snapshots=[snap],
    direction=1
)

committor.run(10)

committor_storage.close()



committor_storage = paths.Storage("toy_committor.nc", mode='r')
spa = paths.ShootingPointAnalysis(committor_storage.steps, [state_A, state_B])

end_A = [step for step in committor_storage.steps if state_A(step.change.canonical.trials[0][-1])]

end_B = [step for step in committor_storage.steps if state_B(step.change.canonical.trials[0][-1])]

part_A = end_A[-1].change.canonical.trials[0].trajectory.reversed
part_B = end_B[-1].change.canonical.trials[0].trajectory

traj = part_A + part_B[1:]

equil_network = paths.TPSNetwork(state_A, state_B)
scheme = paths.OneWayShootingMoveScheme(network=equil_network, engine=engine)
init_conds = scheme.initial_conditions_from_trajectories(traj)

sim = paths.PathSampling(
    storage=None,
    move_scheme=scheme,
    sample_set=init_conds
)

sim.run_until_decorrelated()

sim.run(100)

setup_nc = paths.Storage("2_state_toy.nc", mode='w')
setup_nc.tags['initial_conditions'] = sim.sample_set
#setup_nc.save(sim.sample_set[0].trajectory)
setup_nc.save(state_A)
setup_nc.save(state_B)
setup_nc.save(engine)
setup_nc.close()
