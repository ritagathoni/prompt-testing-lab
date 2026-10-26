import unittest
from src.evaluator import assess,run_cases
class PromptTests(unittest.TestCase):
 def test_word_limit(self):
  self.assertTrue(assess('One two', [{'type':'max_words','value':2}])['passed'])
 def test_json_fences_fail(self):
  self.assertFalse(assess('```json\n{}\n```',[{'type':'json_only'}])['passed'])
 def test_samples_present(self):
  self.assertEqual(len(run_cases('data/cases.json')),5)
if __name__=='__main__': unittest.main()
