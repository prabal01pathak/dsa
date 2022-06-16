#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def reverseWords(self, s: str) -> str:
        first = 0
        last = 0
        new_str = ""
        for index, value in enumerate(s):
            last = index
            if (value == " " and index != 0):
                for j in range((last-first)):
                    new_str += s[last -j -1]
                new_str += " "
                first = index + 1
            if index == len(s) - 1:
                for j in range((last-first)+1):
                    new_str += s[last -j]
        return new_str


def test_reverse_words_string_3():
    s = Solution()
    assert s.reverseWords("the sky is blue") == "eht yks si eulb"
    assert s.reverseWords("hello world!") == "olleh !dlrow"
    assert s.reverseWords("a") == "a"
    assert s.reverseWords("") == ""
    print("-------------------------- Test 3: reverse_words_string_3 --------------------------")


if __name__ == "__main__":
    test_reverse_words_string_3()
