def get_option_letters(n):
    return [chr(i) for i in range(ord('a'), ord('a') + n)]


def mark_correct_answer(answers, idx):
    if idx is not None:
        answers[idx] = f"*{answers[idx]}"
    return answers


def get_correct_answer_index(options, correct_answer):
    return options.index(correct_answer) if correct_answer else None


def format_question(q, index):
    options = q['mc_options']
    if q['question_type'] == 'TF':
        options = ['True', 'False']

    idx = get_correct_answer_index(options, q['correct_answer'])
    answers = mark_correct_answer([f"{char}. {option}\n" for char, option in zip(get_option_letters(len(options)), options)], idx)
    return f"{index}. {q['question']}\n{''.join(answers)}"


def write_formatted_questions(questions, filename="output.txt"):
    formatted_questions = [format_question(q, idx+1)
                           for idx, q in enumerate(questions)]
    with open(filename, "w") as file:
        for item in formatted_questions:
            file.write(f"{item}\n")