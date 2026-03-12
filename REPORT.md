# The project REPORT is where students will document key learnings, challenges, and reflections on their experience using CoPilot for software development. 

# First Impressions - Initial Take on the Project Assignment

I assumed that the project would involve building a simple game, likely Hangman, based on the context provided in MY_NOTES.md. I also assumed that I would need to define the game states, variables, rules, and potential bugs before implementing the game logic. I expected to use CoPilot to assist with coding the game and to help me think through the design and implementation details.

However, I wasn't really sure what some of the constraints meant, like being pure, no loops and the immutability requirement. I also wasn't sure how to structure the code to meet those constraints while still implementing the game logic effectively. I assumed that I would need to find creative ways to manage state and control flow without traditional loops or mutable variables, which could be a significant challenge.

# Key Learnings

I definitely learned a lot about functional programming concepts, especially immutability and pure functions. I had to think differently about how to manage state and control flow without using loops or mutable variables, which was a great learning experience. I also learned how to use CoPilot more effectively by providing clear and specific prompts, and by iterating on the code it generated to refine it and make it work for my specific use case. I also learned that we shouldn't print directly from the game logic functions, but instead return status strings that can be printed by a separate function, which was a new concept for me. A bit embarrasing, but CoPilot helped me realize that I was adding redundant code in my elif statements already covered in the if statement, which was a good lesson in code efficiency and avoiding unnecessary complexity. I gained a deeper understanding of functional programming principles and how to apply them in practice, as well as how to leverage AI tools like CoPilot to enhance my coding proocess.

# Report on CoPilot Prompting Experience

Initially, I found that prompts that were presented as a student trying to learn and asking for guidance on how to implement certain features or concepts worked well. However, CoPilot started repeating it's responses in terms of questions, even when it was clear I was confused and needed more direct help. This was a bit frustrating because I felt like I was asking for specific guidance, but CoPilot kept responding with questions that didn't directly address my confusion. It seemed like CoPilot was trying to encourage me to think through the problem on my own, which is a good approach in some cases, but in this situation, I needed more concrete help to understand the concepts and how to implement them effectively. 

# Limitations, Hallucinations and Failures

There weren't any limitations or failures per se, definitely no halluncinations, but the quesions that CoPilot kept asking instead of providing direct guidance were a bit frustrating. There were also a few times it didn't fully identify all the problems in my code until I asked it to review the code again, which was a bit of a limitation in terms of its ability to catch all issues in one go. However, once I prompted it to review the code again, it was able to identify the remaining issues and provide suggestions for how to fix them, which was helpful.

# AI Trust

There was never any reason not to trust the AI. It asked good questions and provided helpful suggestions for improving my code. The only time I felt a bit frustrated was when it kept asking questions instead of providing direct guidance.

# What I Learned

In addition to the key learnings mentioned earlier, I learned that software development often involves a lot of iteration and refinement. It's not just about writing code that works, but about writing code that is efficient, maintainable, and follows good design. I had to be very patiient and go through my code several times with CoPilot before I was able to get it right and respect all the constraints. You should double-check AI suggestions, especially when it comes to complex logic or when the AI is making assumptions about the code. However, in my case, it was generally safe to trust the AI's suggestions, as it was able to identify issues and provide helpful guidance for improving my code.

# Reflection

It felt like hours, but ultimately, I think using CoPilot did make me faster in the sense that it helped me identify issues and provided suggestions for how to fix them, which saved me time compared to trying to figure everything out on my own. I didn't always feel in control of the code, especially when CoPilot was asking questions instead of providing direct guidance, which made me feel a bit lost at times. I would definitely use AI in a similar way next time, but I would try to be more specific in my prompts to get more direct guidance from CoPilot, especially when I'm feeling confused or stuck on a particular concept or implementation detail.

# Testing Experience

I have never written tests before, so this was a new experience for me and I had to ask CoPilot (plan mode) to guide me on how to do tests with pytest, including the setup of pytest in the first place. I learned why tests are important and how they can help catch bugs and ensure that my code is working as expected. For guidance, CoPilot made several helpful suggestions and asked good questions to help me figure out where to start from. Writing them however, I had to employ A LOT of help from ChatGPT (I forgot to use CoPilot - bad behaviour) to understand how to write effective tests, especially for edge cases and potential bugs. This is something I definitely need to work on and improve, as writing good tests is an important skill for any software developer.
