def count_vowels(text):
    vowels = 'aeıioöuü'
    vowel_counter = {vowel: 0 for vowel in vowels}

    for char in text:
        if char.lower() in vowel_counter:
            vowel_counter[char.lower()] += 1

    return vowel_counter

def calculate_vowel_statistics(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            vowel_counter = count_vowels(text)

            total_vowels = sum(vowel_counter.values())
            open_vowels = sum(vowel_counter[vowel] for vowel in 'aıou')
            close_vowels = sum(vowel_counter[vowel] for vowel in 'eiöü')
            thickness_ratio = open_vowels / total_vowels if total_vowels > 0 else 0
            thinness_ratio = close_vowels / total_vowels if total_vowels > 0 else 0

            return {
                'vowel_counts': vowel_counter,
                'total_vowels': total_vowels,
                'open_vowels': open_vowels,
                'close_vowels': close_vowels,
                'thickness_ratio': thickness_ratio,
                'thinness_ratio': thinness_ratio
            }

    except FileNotFoundError:
        print(f"{file_path} file not found.")
        return None

def main():
    file_path = "turkish_unisex_names.txt"  # Specify the path of the text file
    statistics = calculate_vowel_statistics(file_path)

    if statistics:
        for vowel, count in statistics['vowel_counts'].items():
            print(f"{vowel}: {count}")
        print(f"Total number of vowels: {statistics['total_vowels']}")
        print("Total number of open vowels: {}".format(statistics['open_vowels']))
        print("Total number of close vowels: {}".format(statistics['close_vowels']))
        print("Thickness ratio: {:.2f}".format(statistics['thickness_ratio']))
        print("Thinness ratio: {:.2f}".format(statistics['thinness_ratio']))

if __name__ == "__main__":
    main()
