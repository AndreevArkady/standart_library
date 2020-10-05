import string
import itertools


def popular_word_letter():
    input_text = open('input.txt').read().lower().split()
    amount_of_words = len(input_text)
    unique_words = []
    dictionary = {}
    alphabet_lc = string.ascii_lowercase
    for letters in alphabet_lc:
        dictionary[letters] = 0

    for word in input_text:
        for letter in word:
            dictionary[letter] += 1
        if word not in unique_words:        # Get the set of unique words.
            unique_words.append(word)

        # Make a list of (count, unique) tuples.
    counts = []
    for unique in unique_words:
        count = 0  # Initialize the count to zero.
        for word in input_text:  # Iterate over the words.
            if word == unique:  # Is this word equal to the current unique?
                count += 1  # If so, increment the count
        counts.append((count, unique))

    counts.sort()  # Sorting the list puts the lowest counts first.
    counts.reverse()  # Reverse it, putting the highest counts first.

    count, word = counts[0]
    with open("output.txt", 'w') as fout:
        fout.write('The most frequent word "%s" meets %d times \n' % (word, count))
        maximum = 0
        ind_max = 0
        for i in dictionary:
            if dictionary[i] > maximum:
                maximum = max(maximum, dictionary[i])
                ind_max = i
        fout.write('most common letter: "%s" meets %d times \n' % (ind_max, maximum))
        fout.write('average occurrence of a letter "%s" in a word = %.3f' % (ind_max, maximum / amount_of_words))


def get_palindrome_halves(s, n):
    dictionary = set()
    ans = set()
    for i in s:
        dictionary.add(i)
    dictionary.add('')
    dict_perms = list(itertools.combinations_with_replacement(dictionary, n))
    for i in dict_perms:
        s = ''
        for j in i:
            s += str(j)
        ans.add(s)
        s = ''
        for j in reversed(i):
            s += str(j)
        ans.add(s)
    return ans


def reverse(a):
    a = a[::-1]
    return a


def find_palindromes(n):
    s = open('alphabet.txt').read().lower().split()
    palindrome_halves = get_palindrome_halves(s, int((n + 1) / 2))
    palindrome_halves_list = []
    for i in palindrome_halves:
        palindrome_halves_list.append(i)
    palindrome_halves_list.sort()
    all_palindromes = []
    for i in palindrome_halves_list:
        first_half = str(i)
        second_half_full = reverse(i)
        second_half_shortened = reverse(i[0: len(i) - 1:])
        all_palindromes.append(str(first_half + second_half_shortened))
        if len(first_half) + len(second_half_full) <= n:
            all_palindromes.append(str(first_half + second_half_full))
    all_palindromes.sort()
    all_palindromes.remove('')
    with open("palindromes.out", 'w') as fout:
        fout.write('Palindromes of your alphabet that no longer than n:\n')
        for palindrome in all_palindromes:
            fout.write('"%s"\n' % palindrome)


if __name__ == '__main__':
    popular_word_letter()
    find_palindromes(5)
