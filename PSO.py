import numpy as np

class Particle:
  def __init__(self, func, dim, vmin, vmax, seed):
    self.rnd = np.random.seed(seed)
    self.velocity = np.zeros(dim)
    self.best_part_pos = np.zeros(dim)
    self.position = np.random.uniform(vmin, vmax, dim)
    self.fitness = func(self.position)
    self.best_part_pos = np.copy(self.position)
    self.best_part_fitness = self.fitness

def pso(func, max_iter, num_particles, dim, vmin, vmax, params):
  wmax = params["wmax"]
  wmin = params["wmin"]
  c1 = params["c1"]
  c2 = params["c2"]
 
  rnd = np.random.seed()

  swarm = [Particle(func, dim, vmin, vmax, i) for i in range(num_particles)]
  best_swarm_pos = np.zeros(dim)
  best_swarm_fitness = np.inf
  for i in range(num_particles):
    if swarm[i].fitness < best_swarm_fitness:
      best_swarm_fitness = swarm[i].fitness
      best_swarm_pos = np.copy(swarm[i].position)
  it = 0
  while it < max_iter:
    if it % 5 == 0:
      print("Iteration = " + str(it) + " best fitness = %f" % best_swarm_fitness)
    w = wmax - ((wmax - wmin)/max_iter)*it
    for i in range(num_particles): 
      swarm[i].velocity = (
                           (w * swarm[i].velocity) +
                           (c1 * np.random.rand(dim) * (swarm[i].best_part_pos - swarm[i].position)) + 
                           (c2 * np.random.rand(dim) * (best_swarm_pos -swarm[i].position))
                         ) 
      for k in range(dim):
        swarm[i].position[k] += swarm[i].velocity[k]
        swarm[i].position[k] = np.maximum(swarm[i].position[k], vmin)
        swarm[i].position[k] = np.minimum(swarm[i].position[k], vmax)
      swarm[i].fitness = func(swarm[i].position)
      if swarm[i].fitness < swarm[i].best_part_fitness:
        swarm[i].best_part_fitness = swarm[i].fitness
        swarm[i].best_part_pos = np.copy(swarm[i].position)
      if swarm[i].fitness < best_swarm_fitness:
        best_swarm_fitness = swarm[i].fitness
        best_swarm_pos = np.copy(swarm[i].position)
    it += 1
  gbest ={}
  gbest["position"] = best_swarm_pos
  gbest["cost"] = best_swarm_fitness
  return gbest