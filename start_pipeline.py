import argparse
from tmp_1.perform import some_op
from tmp_2.perform import some_op_1
from tmp_3.perform import some_op_2

from clearml import PipelineController

def pre_main(args):

    pipline = PipelineController("Tmp-pipeline", "Tmp-pipeline1", version="0.0.1")

    with open("tmp_1/docker_setup_script.sh", "r") as f:
        s1_docker_setup_script = f.read()
    pipline.add_function_step(
        "Some_1",
        some_op,
        function_kwargs={
            "a": args.value,
            "b": 2,
            "c": 3,
        },
        function_return=["pow_of_value"],
        task_name='power',
        task_type="inference",
        packages="tmp_1/requirements.txt",
        docker="nvidia/cuda:11.4.0-runtime-ubuntu20.04",
        docker_args="'--ipc=host'",
        docker_bash_setup_script=s1_docker_setup_script,
        execution_queue="onprem.1x1080ti",
        repo="https://github.com/kaichoulyc/tmp-clearml-pipeline",
        repo_commit="3eebe4228d4b7509cf5b3813732f452900bfe429",
        auto_connect_frameworks=False,
        cache_executed_step=True,
    )

    with open("tmp_2/docker_setup_script.sh", "r") as f:
        s2_docker_setup_script = f.read()
    pipline.add_function_step(
        "Some_2",
        some_op_1,
        function_kwargs={
            "a": 2,
            "b": 2,
            "previous_output": "${Some_1.pow_of_value}",
        },
        function_return=["new_pow"],
        task_name=f"power_2",
        task_type="inference",
        packages="tmp_2/requirements.txt",
        docker="nvidia/cuda:11.4.0-runtime-ubuntu20.04",
        docker_args="'--ipc=host'",
        docker_bash_setup_script=s2_docker_setup_script,
        execution_queue="onprem.1x1080ti",
        repo="https://github.com/kaichoulyc/tmp-clearml-pipeline",
        repo_commit="3eebe4228d4b7509cf5b3813732f452900bfe429",
        auto_connect_frameworks=False,
        parents=["Some_1"],
        cache_executed_step=True,
    )

    with open("tmp_3/docker_setup_script.sh", "r") as f:
        s3_docker_setup_script = f.read()
    pipline.add_function_step(
        "Some_3",
        some_op_2,
        function_kwargs={
            "a": 2,
            "b": 2,
            "previous_output": "${Some_1.pow_of_value}",
            "previous_output_2": "${Some_2.new_pow}",
        },
        function_return=["final_pow"],
        task_name=f"power_3",
        task_type="inference",
        packages="tmp_3/requirements.txt",
        docker="nvidia/cuda:11.4.0-runtime-ubuntu20.04",
        docker_args="'--ipc=host'",
        docker_bash_setup_script=s3_docker_setup_script,
        execution_queue="onprem.1x1080ti",
        repo="https://github.com/kaichoulyc/tmp-clearml-pipeline",
        repo_commit="3eebe4228d4b7509cf5b3813732f452900bfe429",
        auto_connect_frameworks=False,
        parents=["Some_1", "Some_2"],
        cache_executed_step=True,
    )

    pipline.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--value", default=1, help="path to config file")
    args = parser.parse_args()
    pre_main(args)