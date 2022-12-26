from unittest import TestCase
from stack.valid_parentheses import valid_parentheses


class TestValidParentheses(TestCase):
    def test_valid_parentheses_for_bracket(self):
        s = '()'
        self.assertTrue(valid_parentheses(s))
