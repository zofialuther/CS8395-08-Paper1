from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from util import *
import os
import json
import re
import importlib.util
from pathlib import Path
import types
from tqdm import tqdm
import concurrent.futures


import sys

from llm_test_helpers import get_llm, get_args

def handler(signum, frame):
    raise TimeoutError()

def get_llm(llm_name):
    if llm_name == "chatgpt-latest":
        return ChatOpenAI()
    elif llm_name == "openai-latest":
        return OpenAI()
    elif llm_name == "openai-latest-1024":
        return OpenAI(max_tokens=1024)
    elif llm_name == "text-ada":
        return OpenAI(model='text-ada-001')
    elif llm_name == 'gpt-3.5':
        return ChatOpenAI(model='gpt-3.5-turbo-1106')
    
    raise ValueError(f"LLM '{llm_name}' not found!")

def direct_translation(llm, json_content):
    problem_index = json_content['problem_index']
    java_code = json_content['java_code']
    parameters = json_content['parameters']
    return_values = json_content['return_values']

    prompt = "Given the following Java code and associated parameter(s) and return value(s), write equivalent Python code. Do not include any explanation or description."
    prompt += f"\nJava: {java_code} \n\n Parameter(s): {parameters} \n\n Return value(s): {return_values}"

    solution = generate_code(llm, prompt)

    folder_name = "direct_translations"
    file_name = f"problem_{problem_index}.py"
    path = os.path.join(folder_name, file_name)

    with open(path, 'w') as file:
        file.write(solution)

def produce_pseudocode(llm, json_content):
    problem_index = json_content['problem_index']
    java_code = json_content['java_code']
    parameters = json_content['parameters']
    return_values = json_content['return_values']

    prompt = "Given the following Java code and associated parameter(s) and return value(s), generate pseudocode in plain text."
    prompt += f"\nJava: {java_code} \n\n Parameter(s): {parameters} \n\n Return value(s): {return_values}"

    pseudocode = generate_pseudocode(llm, prompt)

    folder_name = "pseudocodes"
    file_name = f"problem_{problem_index}.txt"
    path = os.path.join(folder_name, file_name)

    with open(path, 'w') as file:
        file.write(pseudocode)

def produce_description(llm, json_content):
    problem_index = json_content['problem_index']
    java_code = json_content['java_code']
    parameters = json_content['parameters']
    return_values = json_content['return_values']

    prompt = "Given the following Java code and associated parameter(s) and return value(s), generate a semantic description for the program in plain text."
    prompt += f"\nJava: {java_code} \n\n Parameter(s): {parameters} \n\n Return value(s): {return_values}"

    description = generate_description(llm, prompt)

    folder_name = "descriptions"
    file_name = f"problem_{problem_index}.txt"
    path = os.path.join(folder_name, file_name)

    with open(path, 'w') as file:
        file.write(description)

def generate_baseline_and_reps(llm):
    for filename in tqdm(os.listdir('source_probs')):
        file_path = os.path.join('source_probs', filename) 

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                try:
                    # Load and process JSON content
                    json_content = json.load(file)
                    direct_translation(llm, json_content)
                    produce_pseudocode(llm, json_content)
                    produce_description(llm, json_content)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {filename}")
    return

def pseudocode_to_python(llm, pseudocode, problem_index):
    prompt = "Given the following pseudocode, write an equivalent Python function. Do not include any explanation or description."
    prompt += f"\nPseudocode: {pseudocode}"

    solution = generate_code(llm, prompt)
    
    folder_name = "pseudocode_to_python"
    file_name = f"problem_{problem_index}.py"
    path = os.path.join(folder_name, file_name)

    with open(path, 'w') as file:
        file.write(solution)

def pseudo_and_code_to_python(llm, pseudocode, java_code, problem_index):
    prompt = "Given the following Java code and associated pseudocode, write an equivalent Python function. Do not include any explanation or description."
    prompt += f"\nJava code: {java_code}"
    prompt += f"\nPseudocode: {pseudocode}"

    solution = generate_code(llm, prompt)

    folder_name = "pseudo_and_code_to_python"
    file_name = f"problem_{problem_index}.py"
    path = os.path.join(folder_name, file_name)

    with open(path, 'w') as file:
        file.write(solution)

def desc_and_code_to_python(llm, description, java_code, problem_index):
    prompt = "Given the following Java code and associated description, write an equivalent Python function. Do not include any explanation or description."
    prompt += f"\nJava code: {java_code}"
    prompt += f"\nDescription: {description}"

    solution = generate_code(llm, prompt)

    folder_name = "desc_and_code_to_python"
    file_name = f"problem_{problem_index}.py"
    path = os.path.join(folder_name, file_name)

    with open(path, 'w') as file:
        file.write(solution)

def run_experiment_pseudo_and_code(llm):
    for filename in tqdm(os.listdir('source_probs')):
        file_path = os.path.join('source_probs', filename) 

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                try:
                    # Load and process JSON content
                    json_content = json.load(file)
                    java_code = json_content['java_code']
                    problem_index = json_content['problem_index']
                    pseudocode_path = os.path.join('pseudocodes', f"problem_{problem_index}.txt")
                    if os.path.isfile(pseudocode_path):
                        with open(pseudocode_path, 'r') as file:
                            pseudocode = file.read()
                            pseudo_and_code_to_python(llm, pseudocode, java_code, problem_index)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {filename}")

def run_experiment_desc_and_code(llm):
    for filename in tqdm(os.listdir('source_probs')):
        file_path = os.path.join('source_probs', filename) 

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                try:
                    # Load and process JSON content
                    json_content = json.load(file)
                    java_code = json_content['java_code']
                    problem_index = json_content['problem_index']
                    desc_path = os.path.join('descriptions', f"problem_{problem_index}.txt")
                    if os.path.isfile(desc_path):
                        with open(desc_path, 'r') as file:
                            description = file.read()
                            desc_and_code_to_python(llm, description, java_code, problem_index)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {filename}")
    
def run_experiment_pseudocode(llm):
    for filename in tqdm(os.listdir('pseudocodes')):
        file_path = os.path.join('pseudocodes', filename) 

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                pseudocode = file.read()
                match = re.search(r'problem_(\d+)\.txt', filename)
                problem_index = match.group(1)

                pseudocode_to_python(llm, pseudocode, problem_index)

def description_to_python(llm, description, problem_index):
    prompt = "Given the following description, write an equivalent Python function. Do not include any explanation or description."
    prompt += f"\nDescription: {description}"

    solution = generate_code(llm, prompt)
    
    folder_name = "description_to_python"
    file_name = f"problem_{problem_index}.py"
    path = os.path.join(folder_name, file_name)

    with open(path, 'w') as file:
        file.write(solution)
                
def run_experiment_description(llm):
    for filename in tqdm(os.listdir('descriptions')):
        file_path = os.path.join('descriptions', filename) 

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                description = file.read()
                match = re.search(r'problem_(\d+)\.txt', filename)
                problem_index = match.group(1)

                description_to_python(llm, description, problem_index)

def run_tests(solution_path, tests):
    # Load the Python file as a module
    module_name = Path(solution_path).stem
    spec = importlib.util.spec_from_file_location(module_name, solution_path)
    func_to_test = None
    # Try to load the module
    # print("before load")
    try:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        # Handle the exception in a way that makes sense for your application
        print(f"Error loading module in {solution_path}: {e}")


    # If the module loaded successfully, detect the function to test
    else:
        
        for name, item in vars(module).items():
            if isinstance(item, types.FunctionType) and item.__module__ == module_name:
                func_to_test = item
                break


    # if not func_to_test:
    #     print(f"No valid function found in the provided Python file: {solution_path}")
    #     func_to_test = None
    # timeout_seconds = 0.2
    # print("before run")
    results = {}
    total_passed = 0
    for i, test in enumerate(tests):
        input_data = test['input']
        expected_output = test['output']
        passed = False
        # actual_output = None

        try:
            actual_output = func_to_test(input_data)
            passed = actual_output == expected_output
        except Exception as e:
            # print(f"Function raised an exception: {e}")
            actual_output = None

        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     future = executor.submit(func_to_test, input_data)
        #     try:
        #         actual_output = future.result(timeout=timeout_seconds)
        #         passed = actual_output == expected_output
        #     except concurrent.futures.TimeoutError:
        #         print(f"Function call timed out after {timeout_seconds} seconds.")
        #         actual_output = None
        #         future.cancel()
        #     except Exception as e:
        #         print(f"Function raised an exception: {e}")
        #         actual_output = None
        #     finally:
        #         executor.shutdown(wait=False)

        results[i] = {
                'expected': expected_output,
                'actual': actual_output,
                'passed': passed
            }
        if passed:
            total_passed += 1

    results["totals"] = {
        "total_tests": len(tests),
        "passed": total_passed
    }

    return results

def evaluate_solutions():
    result_maps = {"direct_translations":{}, "pseudocode_to_python": {}, "description_to_python":{}, "pseudo_and_code_to_python": {}, "desc_and_code_to_python": {}}
    for filename in os.listdir('source_probs'):
        file_path = os.path.join('source_probs', filename) 

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                try:
                    json_content = json.load(file)
                    tests = json_content['tests']
                    problem_index = json_content['problem_index']

                    for folder in ["direct_translations", "pseudocode_to_python", "description_to_python", "pseudo_and_code_to_python", "desc_and_code_to_python"]:
                        # print(folder)
                        solution_path = os.path.join(folder, f"problem_{problem_index}.py")
                        if os.path.isfile(solution_path):
                            results = run_tests(solution_path, tests)
                            result_maps[folder][problem_index] = results
                            # print(f"Results for {folder}: {results['totals']}")
                        else:
                            print(f"Error opening solution code for {solution_path}")

                    
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {filename}")
    return result_maps


def report_results(results):
    passed_counts = {category: sum([problem['totals']['passed'] for problem in info.values()]) for category, info in results.items()}
    total_counts = {category: sum([problem['totals']['total_tests'] for problem in info.values()]) for category, info in results.items()}

    data = {
        'output': passed_counts['direct_translations']/total_counts['direct_translations']
    }
    
    for category in results:
        data[f"\n{category}:"] = {
            'total_passed_tests' : f"{passed_counts[category]}",
            'total_tests' : f"{total_counts[category]}",
            'accuracy' : f"{passed_counts[category] / total_counts[category]}"
        }

    with open('output.json', "w") as file:
        json.dump(data, file, indent=4)

def main():
    # model_name = input("LLM model? ")
    # generate = input("Generate new solutions? y/n ")

    args = get_args(sys.argv)


    # if generate=='y':
    # original_llm = get_llm(args.model)
    # generate_baseline_and_reps(original_llm)

    # pseudocode_llm = get_llm(args.model)
    # run_experiment_pseudocode(pseudocode_llm)

    # description_llm = get_llm(args.model)
    # run_experiment_description(description_llm)

    # pseudo_code_llm = get_llm(args.model)
    # run_experiment_pseudo_and_code(pseudo_code_llm)

    # desc_code_llm = get_llm(args.model)
    # run_experiment_desc_and_code(desc_code_llm)

    results = evaluate_solutions()
    # print(results)
    report_results(results)
    # print(results)
    return

if __name__ == "__main__":
    main()

    
