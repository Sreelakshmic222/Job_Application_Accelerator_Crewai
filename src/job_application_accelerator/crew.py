from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import ScrapeWebsiteTool, FileReadTool

@CrewBase
class JobApplicationAccelerator():
    """JobApplicationAccelerator crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def job_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['job_analyst'], # type: ignore[index]
            tools=[ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def resume_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_strategist'], # type: ignore[index]
            tools=[FileReadTool(file_path='resume.md')],
            verbose=True
        )
    @agent
    def cover_letter_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['cover_letter_writer'], # type: ignore[index]
            verbose=True
        )
    
    
    @agent
    def interview_coach(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_coach'], # type: ignore[index]
            verbose=True
        )

    @agent
    def application_critic(self) -> Agent:
        return Agent(
            config=self.agents_config['application_critic'], # type: ignore[index]
            verbose=True
        )

    @task
    def analyze_job_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_job_task'], # type: ignore[index]
        )

    @task
    def tailor_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['tailor_resume_task'], # type: ignore[index]
            output_file='tailored_resume.md'
        )
    
    @task
    def cover_letter_task(self) -> Task:
        return Task(
            config=self.tasks_config['cover_letter_task'], # type: ignore[index]
            output_file='cover_letter.md'
        )

    @task
    def interview_prep_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_prep_task'], # type: ignore[index]
            output_file='interview_prep.md'
        )
    
    @task
    def match_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['match_report_task'], # type: ignore[index]
            output_file='match_report.md'
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the JobApplicationAccelerator crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
