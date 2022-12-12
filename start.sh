
export PROJECT_NAME="Tmp-pipeline"
export EXP_NAME="Tmp-pipeline"
export REPO=https://github.com/kaichoulyc/tmp-clearml-pipeline
export GIT_BRANCH=master
export ENTRY_POINT=/start_pipeline_after_change.py
export DOCKER_IMAGE=python:3.8
export DOCKER_ARGS="'--ipc=host'"
export OUTPUT_URI=s3://incode-clearml-data/
export DOCKER_BASH_SETUP_SCRIPT="docker_setup_script.sh"
export QUEUE_NAME="t3.large.storage50Gb_machines"

# Create the task and queue it
clearml-task --project $PROJECT_NAME --name $EXP_NAME --repo $REPO --branch $GIT_BRANCH --script $ENTRY_POINT --docker $DOCKER_IMAGE --docker_args $DOCKER_ARGS --output-uri $OUTPUT_URI --queue $QUEUE_NAME --skip-task-init
