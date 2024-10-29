import os
import csv
import ollama
import re

# Define the function to load data from CSV
def load_csv_data(input_file='requirements_cleaned.csv'):
    data = []
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'requirement': row['requirement'],
                'configuration': row['configuration']
            })
    return data

# Define the function to generate questions and answers using LLM
def generate_questions_and_answers(requirement, configuration, model='llama3:latest'):
    prompt = (
        f"Given the following requirement and configuration:\n"
        f"Requirement: {requirement}\n"
        f"Configuration: {configuration}\n\n"
        f"Generate a relevant question based on Requirement and create its answer using Configuration, answers should be based on cisco IOS code ever possible."
    )
    response = ollama.chat(
        model=model,
        messages=[
            {'role': 'system', 'content': "You are a helpful assistant that generates questions and answers from given information."},
            {'role': 'user', 'content': prompt}
        ]
    )
    return response['message']['content']

# Define the function to extract the question and answer from the LLM response
def extract_question_and_answer(response):
    question_match = re.search(r"Question:\s*(.*?)\n", response, re.IGNORECASE | re.DOTALL)
    answer_match = re.search(r"Answer:\s*(.*?)$", response, re.IGNORECASE | re.DOTALL)
    if question_match and answer_match:
        question = question_match.group(1).strip()
        answer = answer_match.group(1).strip()
        return {"question": question, "answer": answer}
    return None

# Define the function to save a single Q&A pair to a CSV file
def save_qa_to_csv(data, output_file='requirements_questions.csv'):
    file_exists = os.path.isfile(output_file)
    keys = ['question', 'answer']
    with open(output_file, 'a', newline='', encoding='utf-8') as output_csv:
        dict_writer = csv.DictWriter(output_csv, fieldnames=keys)
        if not file_exists:
            dict_writer.writeheader()  # Write header only if file doesn't exist
        dict_writer.writerow(data)

# Main function to execute the process
def main(input_file='requirements_cleaned.csv', output_file='requirements_questions.csv', model='llama3:latest'):
    # Step 1: Load data from CSV
    data = load_csv_data(input_file)
    
    # Step 2: Generate Q&A pairs
    for i, item in enumerate(data):
        requirement = item['requirement']
        configuration = item['configuration']
        
        # Print the gathered requirement and configuration
        print(f"Item {i+1}:")
        print(f"Requirement: {requirement}")
        print(f"Configuration: {configuration}")
        
        response = generate_questions_and_answers(requirement, configuration, model)
        
        # Print the output from the model
        print("Model Output:")
        print(response)
        
        result = extract_question_and_answer(response)
        if result:
            print(f"Generated Question: {result['question']}")
            print(f"Generated Answer: {result['answer']}")
            
            # Save the generated question and answer to the CSV file
            save_qa_to_csv(result, output_file)
        else:
            print("No question and answer generated.")
        print("="*50)  # Divider for readability
    
    print(f"Q&A pairs have been saved to {output_file}")

# Run the main function
if __name__ == "__main__":
    main()

