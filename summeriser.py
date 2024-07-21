import openai

openai.api_key = ''

def summarize_text(text, max_tokens=150):

  response = openai.Completion.create(
      engine="babbage-002",  # Replace with the appropriate model from OpenAI docs
      prompt = f"""
Here's the improved prompt that focuses on text summarization with keypoints:
In a concise and informative way, summarize the following text in {max_tokens} tokens or less, 
ensuring the summary captures the key points and essential concepts:\n{text}
""",
      max_tokens=max_tokens,
      n=1,
      stop=None,
      temperature=0.7,
  )
  summary = response.choices[0].text.strip()
  return summary

# Example usage
text_to_summarize = """Here is the text rewritten as one long story: Artificial Intelligence (AI) refers to the development of computer systems that can perform tasks that typically require human intelligence, such as learning, problem-solving, decision-making, and perception. AI systems aim to simulate human thought processes and behaviors, enabling them to interact with humans and the environment in a more intelligent and autonomous way.
The term "Artificial Intelligence" was coined in 1956 by John McCarthy, a computer scientist and cognitive scientist. Since then, AI has evolved significantly, with various branches and applications emerging over the years.
There are different types of AI, including Narrow or Weak AI, which is designed to perform a specific task, such as playing chess or recognizing faces. General or Strong AI, on the other hand, aims to match human intelligence and perform any intellectual task. Superintelligence is a type of AI that significantly surpasses human intelligence, potentially leading to exponential growth in technological advancements.
AI technologies include Machine Learning, which enables systems to learn from data and improve their performance. Deep Learning is a subset of machine learning, inspired by the human brain's neural networks. Natural Language Processing allows computers to understand, generate, and process human language. Computer Vision enables computers to interpret and understand visual data from images and videos.
AI has numerous applications in various industries. Virtual Assistants, such as Siri, Alexa, and Google Assistant, are examples of AI-powered virtual assistants. Image Recognition is used in security systems, self-driving cars, and medical diagnosis. Chatbots are AI-powered customer service agents that interact with humans. Predictive Analytics is used in finance, healthcare, and marketing to forecast outcomes.
The benefits of AI include automation, which increases efficiency and productivity. AI also enables enhanced decision-making, improved customer experience, and innovation, driving technological advancements and new business models.
However, AI also faces challenges, such as data quality, bias, and ethics. Ensuring AI systems are fair, transparent, and unbiased is crucial. Job displacement is another concern, as automation may lead to job loss in certain sectors. Security and privacy are also essential, as AI systems and data must be protected from cyber threats.
In conclusion, AI has the potential to revolutionize various aspects of our lives, from healthcare and education to entertainment and transportation. As AI continues to evolve, it's essential to address the challenges and ethical considerations surrounding its development and deployment."""

summary = summarize_text(text_to_summarize) 
print(f"\nSummary:\n{summary}")
