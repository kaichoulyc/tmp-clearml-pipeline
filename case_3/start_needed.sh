
PROJECT_NAME="Test-project"
EXP_NAME="run"
REPO=https://github.com/kaichoulyc/tmp-clearml-pipeline
GIT_BRANCH=master
ENTRY_POINT=case_3/enter.py
DOCKER_IMAGE=python:3.8
DOCKER_ARGS="'--ipc=host'"
SCRIPT_ARGS="config=case_3/config.yaml train_task_id=1231wds"
OUTPUT_URI=s3://incode-clearml-data/
DOCKER_BASH_SETUP_SCRIPT="docker_setup_script.sh"
QUEUE_NAME="t3.large.storage50Gb_machines"
REQUIREMENTS=case_3/requirements.txt
# Create the task and queue it
clearml-task --project $PROJECT_NAME --name $EXP_NAME --repo $REPO --branch $GIT_BRANCH --script $ENTRY_POINT --docker $DOCKER_IMAGE --docker_args $DOCKER_ARGS --docker_bash_setup_script $DOCKER_BASH_SETUP_SCRIPT --args $SCRIPT_ARGS --output-uri $OUTPUT_URI --task-type inference --queue $QUEUE_NAME --skip-task-init --requirements $REQUIREMENTS
