# Reference
## Reinforcement learning from human feedback
### intro
In machine learning, reinforcement learning from human feedback (RLHF) or reinforcement learning from human preferences is a technique that trains a "reward model" directly from human feedback and uses the model as a reward function to optimize an agent's policy using reinforcement learning (RL) through an optimization algorithm like Proximal Policy Optimization.[1][2] The reward model is trained in advance to the policy being optimized to predict if a given output is good (high reward) or bad (low reward). RLHF can improve the robustness and exploration of RL agents, especially when the reward function is sparse or noisy.[3]

Human feedback is most commonly collected by asking humans to rank instances of the agent's behavior.[4][5][6] These rankings can then be used to score outputs, for example with the Elo rating system.[2] While the preference judgement is widely adopted, there are other types of human feedbacks that provide richer information, such as numerical feedback, natural language feedback, and edit rate.[7]

RLHF is used in tasks where it's difficult to define a clear, algorithmic solution but where humans can easily judge the quality of the model's output. For example, if the task is to generate a compelling story, humans can rate different AI-generated stories on their quality, and the model can use their feedback to improve its story generation skills.

RLHF has been applied to various domains of natural language processing, such as conversational agents, text summarization, and natural language understanding.[8] Ordinary reinforcement learning, where agents learn from their own actions based on a "reward function", is difficult to apply to natural language processing tasks because the rewards are often not easy to define or measure, especially when dealing with complex tasks that involve human values or preferences. RLHF can enable language models to provide answers that align with these complex values, to generate more verbose responses, and to reject questions that are either inappropriate or outside the knowledge space of the model.[9] Some examples of RLHF-trained language models are OpenAI's ChatGPT and its predecessor InstructGPT,[5][10] as well as DeepMind's Sparrow.[11]

RLHF has also been applied to other areas, such as the development of video game bots. For example, OpenAI and DeepMind trained agents to play Atari games based on human preferences.[12][13] The agents achieved strong performance in many of the environments tested, often surpassing human performance.[14]

### challenges and limitations
RLHF suffers from a number of challenges that can be broken down into problems with human feedback, problems with learning a reward model, and problems with optimizing the policy.[15]

One major challenge is the scalability and cost of human feedback, which can be slow and expensive compared to unsupervised learning. The quality and consistency of human feedback can also vary depending on the task, the interface, and the individual preferences of the humans. Even when human feedback is feasible, RLHF models may still exhibit undesirable behaviors that are not captured by human feedback or exploit loopholes in the reward model, which brings to light the challenges of alignment and robustness.[16]

The effectiveness of RLHF is dependent on the quality of human feedback.[17] If the feedback lacks impartiality or is inconsistent or incorrect, the model may become biased.[18] There is also a risk that the model may overfit to the feedback it receives. For instance, if feedback comes predominantly from a specific demographic or if it reflects specific biases, the model may learn not only the general alignment intended in the feedback, but also any peculiarities or noise present therein.[19][20] This excessive alignment to the specific feedback it received (or to the biases of the specific demographic that provided it) can lead to the model performing suboptimally in new contexts or when used by different groups.

Additionally, in some cases, there may be a risk of the model learning to manipulate the feedback process or game the system to achieve higher rewards, rather than genuinely improving its performance, which indicates a fault in the reward function.[21]

Researchers have surveyed a number of additional limitations to RLHF.[22]

### References
* SEE https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback