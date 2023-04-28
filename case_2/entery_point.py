from threading import Thread
from allegroai import Task
import time


class SecondStart(Thread):
    def __init__(self, changing_param):
        super.__init__()

        self.overwrite_config = {"sm_2": changing_param}

    def overwrite_params(
        self, task: Task, overwrite_params: dict, param_prefix="General"
    ):
        for param_name, param_value in overwrite_params.items():
            param_name = f"{param_prefix}/{param_name}"
            if isinstance(param_value, dict):
                self.overwrite_params(
                    task=task,
                    overwrite_params=param_value,
                    param_prefix=param_name,
                )
            else:
                task.set_parameter(param_name, param_value)

        return task

    def create_task(self):
        task = Task.create(
            project_name="Test",
            task_name="test_2",
            repo="https://github.com/kaichoulyc/tmp-clearml-pipeline.git",
            commit="",
            script="case_2/second_start_point.py",
            requirements_file="case_2/requirements.txt",
            docker="python:3.8",
            docker_args="'--ipc=host'",
            docker_bash_setup_script="docker_setup_script.sh",
            argparse_args=[
                "config=case_2/config.yaml",
                "start_as_task=True",
            ],
        )
        if self.overwrite_config is not None:
            task = self.overwrite_params(
                task=task, overwrite_params=self.overwrite_config
            )
        Task.enqueue(task=task, queue_name="onprem.1x1080ti")

        return task.task_id

    def run(self):
        while True:
            task_id = self.create_task()
            print(task_id)
            time.sleep(6000)


def main():
    sr = 1

    random_config = {"sm": sr}

    task = Task.init("Tests", "test_1")
    task.connect(random_config)

    other_starter = SecondStart(changing_param=5)
    other_starter.start()


if __name__ == "__main__":
    main()
