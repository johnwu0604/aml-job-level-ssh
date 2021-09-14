from azureml.core import Workspace
from azureml.core import RunConfiguration
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig
from azureml.core.runconfig import ApplicationEndpointConfiguration

workspace = Workspace(subscription_id='<SUBSCRIPTION ID>',
                      resource_group='<RESOURCE GROUP>',
                      workspace_name='<WORKSPACE NAME>')

experiment = Experiment(workspace, 'job-level-ssh')

env = Environment(name='windows-env') 
env.docker.base_image = 'mcr.microsoft.com/azureml/3.5dotnet-ltsc2019:latest'
env.python.user_managed_dependencies = True

run_config = RunConfiguration()
run_config.environment = env
run_config.docker.use_docker = True 
run_config.target ='windows-cluster' 
run_config.services['SSH'] = ApplicationEndpointConfiguration(
    type='SSH',
    properties={'sshPublicKeys': '<SSH PUBLIC KEY'}
)

script_config = ScriptRunConfig(source_directory='.', script='script.py', run_config=run_config) 
experiment.submit(script_config) 

 