def algoritm(text, pattern,prime_number, number_of_characters):
    global symbol_index
    text_len = len(text)
    pattern_len = len(pattern)
    pattern_hash = 0
    text_window_hash = 0
    answer_index = []
    answer_index_test = []
    for symbol_index in range(pattern_len):
        pattern_hash = (prime_number * pattern_hash + ord(pattern[symbol_index])) % number_of_characters
        text_window_hash = (prime_number * text_window_hash + ord(text[symbol_index])) % number_of_characters
    for window_index in range(text_len - pattern_len + 1):
        if pattern_hash == text_window_hash:
            symbol_index = check_symbol_by_symbol(pattern, pattern_len, symbol_index, text, window_index)
            if symbol_index == pattern_len:
                answer_index.append(f'({window_index}, {window_index + pattern_len - 1})')
                answer_index_test.append((window_index, window_index + pattern_len - 1))
        if window_index < text_len - pattern_len:
            text_window_hash = (prime_number * (text_window_hash - ord(text[window_index]) *
                                           (pow(prime_number, pattern_len - 1)) % number_of_characters) +
                                ord(text[window_index + pattern_len])) % number_of_characters
    with open("output.txt", "w") as output_file:
        for item in answer_index:
            output_file.write("%s\n" % item)

    return answer_index_test


def check_symbol_by_symbol(pattern, pattern_len, symbol_index, text, window_index):
    for symbol_index in range(pattern_len):
        if pattern[symbol_index] != text[window_index + symbol_index]:
            break
        else:
            symbol_index += 1
    return symbol_index

if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        text_from_input, pattern_from_input = [line.rstrip() for line in input_file]
    algoritm(text_from_input, pattern_from_input, 1, 2)