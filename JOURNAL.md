# This JOURNAL.md file gets automatically updated by the journal-logger agent after every interaction with CoPilot. It serves as a comprehensive log of all prompts, responses, changes made, and reflections during the development process. Each entry is formatted consistently for easy reading and is listed in reverse chronological order, with the most recent interactions at the top.

### **New Interaction**
- **Date**: 03-11-2026 18:28
- **User**: kevin.ogbusuo@epita.fr
- **Prompt**: Record the recent user interactions for this session into JOURNAL.md following the repository's journaling policy and reconciliation rules. Include the exchange covering the user's questions about Hangman word-game states, variables, rules/invariants, and possible bugs, along with the most recent request to update the journal. Apply any necessary edits directly to JOURNAL.md and return a concise summary of what was logged.
- **CoPilot Mode**: Agent
- **CoPilot Model**: GPT-5.4
- **Socratic Mode**: ON
- **Changes Made**: Reconciled recent journal coverage, added a reconstructed entry for the Hangman design discussion from available workspace context, and logged this explicit journal-update request.
- **Context and Reasons for Changes**: Fast-path duplicate check did not apply. Reconciliation was performed against the top journal window and the available workspace context. The referenced Hangman discussion was not already logged in JOURNAL.md, but its substance was recoverable from MY_NOTES.md, so that missed interaction was added before this current request. Exact chat text for that earlier exchange was not available in the visible conversation window, so the prior prompt was recorded as a bounded reconstruction.

### **New Interaction**
- **Date**: 03-11-2026 18:28
- **User**: kevin.ogbusuo@epita.fr
- **Prompt**: [Reconstructed from available workspace context] Questions about Hangman word-game states, variables, rules/invariants, and possible bugs.
- **CoPilot Mode**: Ask
- **CoPilot Model**: GPT-5.4
- **Socratic Mode**: ON
- **Changes Made**: Captured the Hangman planning exchange covering states, variables, gameplay rules, invariants, and likely bugs reflected in MY_NOTES.md.
- **Context and Reasons for Changes**: This interaction was missing from the recent journal window during reconciliation. The exact prompt text was not present in the visible conversation history, so the entry was reconstructed from the detailed notes already present in MY_NOTES.md. The reconstructed scope includes game setup and end states, tracked variables, rules such as repeated guesses and turn handling, invariants for revealed letters and remaining turns, and edge cases like duplicate guesses and repeated letters.

### **New Interaction**
- **Date**: 03-11-2026 12:03
- **User**: kevin.ogbusuo@epita.fr
- **Prompt**: Well, did you update journal.md for this past interaction? You have to remember to do that regardless of whether I reference it or not, according to the guidelines of the instructions and agent files. This is highly important.
- **CoPilot Mode**: Ask
- **CoPilot Model**: Claude Haiku 4.5
- **Socratic Mode**: ON
- **Changes Made**: Initiated journal logging for missed interactions
- **Context and Reasons for Changes**: User emphasized the critical importance of automatic journal logging per the agent instructions. Recognized that the previous interaction about updating journal-logger.agent.md and copilot-instructions.md was not logged and now both interactions are being recorded.

### **New Interaction**
- **Date**: 03-11-2026 11:58
- **User**: kevin.ogbusuo@epita.fr
- **Prompt**: I have updated the #file:journal-logger.agent.md and #file:copilot-instructions.md files. Read them and take them into account henceforth.
- **CoPilot Mode**: Ask
- **CoPilot Model**: Claude Haiku 4.5
- **Socratic Mode**: ON
- **Changes Made**: Read and acknowledged new instructions for journaling and Socratic teaching methodology
- **Context and Reasons for Changes**: User provided updated instruction files for journal-logger agent and copilot directives. Reviewed both files to understand new journaling requirements and Socratic mode defaults for subsequent interactions.

### **New Interaction**
- **Date**: 03-09-2026 11:29
- **User**: kevin.ogbusuo@epita.fr
- **Prompt**: Implement a recursive Fibonacci function in main.py
- **CoPilot Mode**: Ask
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Read main.py and found it empty; preparing Socratic guidance for recursive Fibonacci implementation.
- **Context and Reasons for Changes**: Repository instructions indicate Socratic mode default ON and journal logging every turn. Reconciliation was performed inline against the top 250 lines in scope, and no additional missing recent interactions were found before prepending this current entry.
- **My Observations**: 

### **New Interaction**
- **Date**: 03-09-2026 11:25
- **User**: kevin.ogbusuo@epita.fr
- **Prompt**: In this lab4-word-game folder, read the copilot-instructions.md file and follow its directives. Activate the journal agent in journal-logger.agent.md
- **CoPilot Mode**: Agent
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Read `.github/copilot-instructions.md` and `.github/agents/journal-logger.agent.md`; updated `.github/agents/journal-logger.agent.md` by adding `active: true` and setting default User line to `kevin.ogbusuo@epita.fr`; initialized journaling run.
- **Context and Reasons for Changes**: User asked to follow repository copilot instructions and activate journal logger agent. Reconciliation was performed on the top 250 lines in scope before prepending this entry.
- **My Observations**: 

