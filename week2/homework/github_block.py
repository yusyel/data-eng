from prefect.deployments import Deployment
from prefect.filesystems import GitHub
from prefect import flow, task
from web_to_gcs import etl_web_to_gcs


github_block = GitHub.load("github")


github_dep = Deployment.build_from_flow(
    flow=etl_web_to_gcs,
    work_queue_name = "q5",
    name='github-flow')
if __name__=="__main__":
    github_dep.apply()