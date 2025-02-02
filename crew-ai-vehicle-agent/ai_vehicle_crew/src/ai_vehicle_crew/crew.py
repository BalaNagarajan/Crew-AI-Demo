from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool, YoutubeVideoSearchTool

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

load_dotenv()

@CrewBase
class AiVehicleCrew():
	"""AiVehicleCrew crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def vehicle_market_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['vehicle_market_researcher'],
			tools=[SerperDevTool()],
			verbose=True
		)

	@agent
	def vehicle_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['vehicle_analyst'],
			tools=[ScrapeWebsiteTool()],
			verbose=True
		)
	
	@agent
	def vehicle_advisor(self) -> Agent:
		return Agent(
			config=self.agents_config['vehicle_advisor'],
			tools=[],
			verbose=True
		)
	
	@agent
	def vehicle_report_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['vehicle_report_writer'],
			tools=[FileWriterTool()],
			verbose=True
		)
	
	

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def vehicle_researcher_task(self) -> Task:
		return Task(
			config=self.tasks_config['vehicle_researcher_task'],
		)

	@task
	def vehicle_analyst_task(self) -> Task:
		return Task(
			config=self.tasks_config['vehicle_analyst_task'],
			
		)
	
	@task
	def vehicle_advisor_task(self) -> Task:
		return Task(
			config=self.tasks_config['vehicle_advisor_task'],
		)
	
	@task
	def vehicle_report_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['vehicle_report_writer_task'],
			output_file='vehicle_recommendation_report.md'
		)
	

	@crew
	def crew(self) -> Crew:
		"""Creates the AiVehicleCrew crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
