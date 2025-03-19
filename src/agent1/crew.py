
from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool,ScrapeWebsiteTool

api_key = "AIzaSyBmJ8zlaygJaeMYsxL88e-PzGke70gGFEI"


@CrewBase
class Agent1():
    """Agent1 crew"""

    llm = LLM(
    api_key=api_key,
    model="gemini/gemini-1.5-flash",
	)

   
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			verbose=True,
			llm=self.llm
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm=self.llm
        )

    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            output_file='report5.md'
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report6.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Agent1 crew"""
       
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
