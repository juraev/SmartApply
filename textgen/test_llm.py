import unittest
from textgen.llm import ChatGPT, Llama2

class TestChatGPT(unittest.TestCase):
    def setUp(self):
        self.chat_gpt = ChatGPT()

    def test_generate_text(self):
        prompt = [
                {
                    "role": "user",
                    "content" : "Hello, how are you?"
                }
            ]
        response = self.chat_gpt.generate_text(prompt)
        self.assertIsInstance(response, str)

    def test_load_model(self):
        with self.assertRaises(NotImplementedError):
            self.chat_gpt.load_model("model_path")

    def test_save_model(self):
        with self.assertRaises(NotImplementedError):
            self.chat_gpt.save_model("save_path")

    def test_train_model(self):
        with self.assertRaises(NotImplementedError):
            self.chat_gpt.train_model("data_path")

class TestLlama2(unittest.TestCase):
    def setUp(self):
        self.llama = Llama2("weights/llama-2-7b.bin")

    def test_generate_text(self):
        prompt = "Hello, how are you?"
        max_length = 100
        response = self.llama.generate_text(prompt, max_length)
        self.assertIsInstance(response, str)
        self.assertLessEqual(len(response), max_length)

    def test_load_model(self):
        self.llama.load_model("model_path")
        self.assertIsNotNone(self.llama.model)

    def test_save_model(self):
        with self.assertRaises(NotImplementedError):
            self.llama.save_model("save_path")

    def test_train_model(self):
        with self.assertRaises(NotImplementedError):
            self.llama.train_model("data_path")

if __name__ == "__main__":
    unittest.main()