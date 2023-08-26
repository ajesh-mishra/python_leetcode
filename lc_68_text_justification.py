class Solution:
    @staticmethod
    def full_justify(words: list[str], maxWidth: int) -> list[str]:
        result: list[str] = []
        line: list[str] = []

        for word in words:
            word_len: int = len(word)
            line_len: int = len(''.join(line))

            if line_len + word_len + len(line) - 1 < maxWidth:
                line.append(word)
                continue

            space_between_words = len(line) - 1

            if space_between_words == 0:
                padding: int = maxWidth - len(line[0])
                result.append(line[0] + ' ' * padding)
            else:
                padded_line = ''
                extra_padding = maxWidth - line_len - space_between_words
                even_space = extra_padding // space_between_words
                odd_space = extra_padding % space_between_words

                for i, w in enumerate(line):
                    if space_between_words == i:
                        padded_line += w
                        continue
                    padded_line += w + ' ' * (even_space + 1)
                    if odd_space > 0:
                        padded_line += ' '
                        odd_space -= 1

                result.append(padded_line)

            line.clear()
            line.append(word)

        if line:
            last_line: str = " ".join(line)
        else:
            last_result: str = result.pop()
            trimmed_last_line = list(filter(lambda x: x != ' ', last_result.split(' ')))
            last_line = " ".join(trimmed_last_line)

        last_line_len = len(last_line)
        padded_last_line = last_line + ' ' * (maxWidth - last_line_len)
        result.append(padded_last_line)

        return result


if __name__ == '__main__':
    assert Solution().full_justify(words=["This", "is", "an", "example", "of", "text", "justification."],
                                   maxWidth=16) == [
               "This    is    an",
               "example  of text",
               "justification.  "
           ]

    assert (Solution().full_justify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16)
            == [
                "What   must   be",
                "acknowledgment  ",
                "shall be        "
            ])

    assert (Solution().full_justify(
        words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
               "Art", "is", "everything", "else", "we", "do"], maxWidth=20) == [
               "Science  is  what we",
               "understand      well",
               "enough to explain to",
               "a  computer.  Art is",
               "everything  else  we",
               "do                  "
           ])
