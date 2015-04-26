class Config:
	# Reads configuration file and stores configurable variables
	def __init__(self):
		self.state_tracker = None
		self.tasks = ()
	
	def load(self):
		pass

class StateTracker:
	# Creates file on disk and saves objects state on request
	# If no states are saved (e.g. all tasks finished successfully)
	# then the file is deleted
	def __init__(self, tracker_config):
		pass
	
	def save_state(self, state):
		pass
	
	def __enter__(self):
		pass
	
	def __exit__(self, type, value, traceback):
		pass

class Task:
	def __init__(self):
		self._is_done = False
	
	def run(self):
		# Attempt to run task
		#!!stub
		pass
	
	@property
	def is_done(self):
		# Indicates whether task finished successfully or not
		return self._is_done

class TaskManager:
	# Arranges tasks based on their dependencies on each other
	# Upon iteration returns iterable of tasks that can be run in
	# current iteration
	def __init__(self):
		pass
	
	def add(self, task):
		# Adds task to inner list for subsequent build()
		#!!stub
		pass
	
	def build(self):
		# Attempts to build actual task graph based on added tasks and 
		# their dependencies
		#!!stub
		pass
	
	def __iter__(self):
		yield ()

def main():
	config = Config()
	config.load()
	
	with StateTracker(config.state_tracker) as state_tracker:
	
		task_manager = TaskManager()
		for task in config.tasks:
			task_manager.add(task)
		
		task_manager.build()
		
		#run tasks
		for tasks in task_manager:
			for task in tasks:
				task.run()
				if not task.is_done:
					#running task failed. save graph state, report error and quit
					state_tracker.save_state(task_graph)
					exit(1)
	
	return 0

if __name__ == '__main__':
	main()

