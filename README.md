# AIRABIC: Arabic Dataset for Performance Evaluation of AI Detectors
# Link to the paper:
https://ieeexplore.ieee.org/document/10459781
## Dataset Characteristics:

Source Diversity: Our human-written texts are sourced from a wide range of materials to ensure objectivity and unbiased content. This includes:

Books: A selection of 40 books covering various topics and periods. Each book contributes unique passages to avoid overlap.

News Articles: Articles from the Aljazeera website, specifically between 2014 and 2016, to ensure there is no potential for synthetic texts.

Sample Size: The dataset is carefully constructed to comply with the character limits of AI detectors. Human-written texts vary in length, with shorter samples padded to meet a 1000-character minimum. AI-generated texts from ChatGPT are tailored to maintain consistency in character count and meaningful content.

Text Variations: To test the adaptability of AI detectors, the dataset includes a diverse range of text structures:
* Single and multi-paragraph compositions.
* Bullet point formats.
* Passages with in-text citations.

This diversity ensures a comprehensive evaluation of AI detectors across different text types and structures.

## License
AIRABIC Dataset is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

**What does this mean?**
- **Attribution**: You must give appropriate credit to the creators of the dataset.
- **ShareAlike**: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
- **Commercial Use**: You are free to use the information for commercial purposes.

---

The AIRABIC dataset comprises two main categories:

1. `AI-generated texts.xlsx` - This dataset represents the collection of 500 examples of AI-generated Arabic texts.
2. `Human-written texts.xlsx` - This dataset represents the collection of 500 examples of Arabic texts written by humans.

## Ready-to-Use Text Files
The dataset is also available in a ready-to-use text file format. Each category (`AI-generated texts` and `Human-written texts`) has been split into individual `.txt` files for ease of use. The `.txt` files are organized in the following folders:

- `output_AI-generated_txt`: Contains 500 AI-generated Arabic texts, each saved as an individual `.txt` file.
- `output_human-written_txt`: Contains 500 human-written Arabic texts, each saved as an individual `.txt` file.

This makes it incredibly straightforward to integrate our dataset into your existing natural language processing pipelines or research projects.

## Codebase

1. `Diacritics.py` - This script provides functionalities for building diacritics upon Arabic texts.
2. `NonDiacritics.py` - This script provides functionalities for removing diacritics from the Arabic texts.
3. `main.py` - main class.
