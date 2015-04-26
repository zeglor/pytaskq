import subprocess as sp
from collections import defaultdict

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
	# Base task class. All tasks should subclass it, reimplementing
	# its methods if necessary
	def __init__(self, uname, depends_on=()):
		self._is_done = False
		self.uname = uname
		self.dependencies = depends_on
	
	def run(self):
		# Attempt to run task
		#!!stub
		pass
	
	@property
	def is_done(self):
		# Indicates whether task finished successfully or not
		return self._is_done

class TaskProcedure(Task):
	def __init__(self, procedure_name, procedure_args, uname, depends_on=()):
		self.procedure_name = procedure_name
		self.procedure_args = procedure_args
		super().__init__(uname, depends_on)
	
	def run(self):
		return sp.call(self.procedure_name, *self.procedure_args)

class TaskManager:
	# Arranges tasks based on their dependencies on each other
	# Upon iteration returns iterable of tasks that can be run in
	# current iteration
	def __init__(self):
		self._runnable_tasks = []
		self._delayed_tasks = []
		self._dependent_tasks = defaultdict(list)
		self._tasks_finished = []
		self.is_done = False
	
	def add(self, task):
		# Adds task to inner list for subsequent build()
		#self._tasks[task.uname] = task
		if len(task.dependencies) == 0:
			self._runnable_tasks.append(task)
		else:
			self._delayed_tasks.append(task)
			for dependency in task.dependencies:
				self._dependent_tasks[dependency].append(task)
	
	def build(self):
		# Attempts to build actual task graph based on added tasks and 
		# their dependencies
		if len(self._runnable_tasks) == 0:
			#!! throw exception
			pass
	
	def start(self):
		while len(self._tasks_finished) < len(self._runnable_tasks) + len(self._delayed_tasks):
			for task in self._runnable_tasks[:]:
				task.run()
				if task.is_done == True:
					# Task finished normally. Add it to finished tasks
					self._tasks_finished.append(task.uname)
					# Notify dependent tasks
					for dependent_task in self._dependent_tasks[task.uname][:]:
						dependent_task.satisfy_dependency(task.uname)
						if len(dependent_task.dependencies) == 0:
							# This task has no more unsatisfied dependencies
							# and therefore can be run normally
							self._runnable_tasks.append(dependent_task)
							self._delayed_tasks.remove(delayed_task)
							self._dependent_tasks[task.uname].remove(depentent_task)
				else:
					#!!stop processing tasks and quit
					break
		self.is_done = True

def main():
	config = Config()
	config.load()
	
	with StateTracker(config.state_tracker) as state_tracker:
	
		task_manager = TaskManager()
		for task in config.tasks:
			task_manager.add(task)
		
		task_manager.build()
		task_manager.start()
		if not task_manager.is_done:
			#running task failed. save manager state, report error and quit
			state_tracker.save_state(task_manager)
			exit(1)
	
	return 0

if __name__ == '__main__':
	main()

