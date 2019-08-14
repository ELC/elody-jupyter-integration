import json
import subprocess

from lod import lod
object_manager = lod.get_object_manager()

def save_parameters(lod_manager):
    arguments = lod.get_program_arguments()

    with open(arguments['user_parameters_file'].file, 'r') as infile:
        with open('parameters.json', 'w') as outfile:
            json.dump(json.load(infile), outfile)


def load_results(lod_manager):
    with open('result.json', 'r') as infile:
        return json.load(infile)


def main(lod_manager):
    
    save_parameters(lod_manager)

    subprocess.run("jupyter nbconvert --to notebook --inplace --execute app.ipynb".split())

    results = load_results(lod_manager)

    lod.start_message().\
        add_text(f"Predictions {results}").\
        finish()

    lod.tag('!set_status_message', comment="This Scenario is finished.")


with lod.manager(suppress_exceptions_after_logging_them=False, redirect_stdout_to_log=True) as lod_manager:
    main(lod_manager)