import re
import tempfile
import json
import multiprocessing
import os


def extract_code(response: str) -> str:
	# Try to find the last Python code block
	python_blocks = re.findall(r'``` ?python\n(.*?)\n```', response, re.DOTALL)
	if python_blocks:
		return python_blocks[-1].strip()
		
	# If no Python code block is found, try to find the last generic code block
	generic_blocks = re.findall(r'``` ?\n(.*?)\n```', response, re.DOTALL)
	if generic_blocks:
		return generic_blocks[-1].strip()
		
	return response


def generate_code(llm, problem_input) -> str:
	prompt = problem_input
		
	# Add additional instructions for automated prompting
	prompt += "\n\nAfter analyzing the problem, provide your solution as a SINGLE function in a Markdown code block. Do NOT include tests nor examples in the Markdown code block. The last Markdown code block in your response will be directly executed for testing."
		
	#print(f"***Prompt:\n{prompt}")

	output = llm.predict(prompt)

	#print(f"***Response:\n{output}")
	solution = extract_code(output)
		
	# print(f"***Extracted solution:\n{solution}")
	return solution


def generate_pseudocode(llm, problem_input) -> str:

	prompt = problem_input
	prompt += "\n\nAfter analyzing the problem, provide your pseudocode solution in a Markdown block. Do not include tests in the Markdown block."
	output = llm.predict(prompt)

	solution = extract_code(output)
		
	# print(f"***Extracted solution:\n{solution}")
	return solution


def generate_description(llm, problem_input) -> str:

	prompt = problem_input
	prompt += "\n\nAfter analyzing the problem, provide your semantic description in a Markdown block. Do not include tests in the Markdown block."
	output = llm.predict(prompt)

	solution = extract_code(output)
		
	# print(f"***Extracted solution:\n{solution}")
	return solution


# def execute_function(function_code, parameters, iterations):
# 	try:
# 		# Create temporary files for function_code, parameters, config, and result
# 		function_code_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.py')
# 		parameters_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json')
# 		config_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json')
# 		result_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json')
		
# 		# Write function_code and parameters to temporary files
# 		function_code_file.write(function_code)
# 		function_code_file.close()  # Close the file to ensure it's written to disk
		
# 		json.dump(parameters, parameters_file)
# 		parameters_file.close()  # Close the file to ensure it's written to disk
	
# 		# Write configuration to temporary file
# 		config_data = {
# 			"iterations": iterations
# 		}
# 		json.dump(config_data, config_file)
# 		config_file.close()  # Close the file to ensure it's written to disk
		
# 		# Create a separate Python process to run the executor_script
# 		process = multiprocessing.Process(target=executor_script, args=(function_code_file.name, parameters_file.name, config_file.name, result_file.name))
# 		process.start()
# 		process.join(timeout=5)  # Add a timeout of 5 seconds
		
# 		# If the process is still alive after the timeout, terminate it
# 		if process.is_alive():
# 			process.terminate()
# 			return None
		
# 		# Load the result from the result file
# 		with open(result_file.name, 'r') as file:
# 			result_data = json.load(file)
		
# 		try:
# 			# Clean up temporary files
# 			os.unlink(function_code_file.name)
# 			os.unlink(parameters_file.name)
# 			os.unlink(config_file.name)
# 			os.unlink(result_file.name)
# 		except Exception as e:
# 			print(f"Failed to unlink temporary files: {str(e)}")
		
# 		# Construct the result object
# 		return result_data.get('result')
		
# 	except Exception as e:
# 		return e